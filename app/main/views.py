from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from time import gmtime, strftime
from . import main
from ..auth.forms import LoginForm, ChangePasswordForm, ChangeEmailForm, PaymentForm, \
    MemberRegistrationForm, MD5Form, UploadForm
from ..models import User, Member
from .. import db
from ..json_reader import GetFile
from ..email import send_email
from .. import storage


@main.route('/' , methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.dashboard'))
        flash('Invalid username or password.')
    return render_template('index.html', form=form)




@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    user = User.query.filter_by(id=current_user.id).first()
    admin_settings = GetFile('admin_settings.json').Read()    
    site_data = {
        "payed": user.fee_payed,
        "registered": user.team_registered,
        "download_questions_time": admin_settings['download_questions_time'],
        "zip_password_time":admin_settings['zip_password_time'],
        "code_submission_time":admin_settings['code_submission_time'],
        "solution_upload_time":admin_settings['solution_upload_time'],
        "check_solution_time":admin_settings['check_solution_time']
    }
    template_name='选手首页'
    return render_template('dashboard/home.html', template_name=template_name, site_data=site_data)




@main.route('/dashboard/pay', methods=['GET', 'POST'])
@login_required
def pay():
    template_name='网上缴费'
    form = PaymentForm()
    if request.method == "POST":
        if form.validate_on_submit():
            current_user.fee_payed = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            db.session.add(current_user)
            db.session.commit()
            flash('缴费成功！')
        else:
            flash('缴费出错！！！')
    return render_template('dashboard/pay.html', template_name=template_name, form=form)




@main.route('/dashboard/team_info', methods=['GET', 'POST'])
@login_required
def team():
    template_name='编辑资料'
    # the registration form will dissapear when the whole team is registered
    visible = 'true'
    members_ammount = Member.query.count()
    members = Member.query.filter_by(group_id=current_user.id)
    if members_ammount >= 3:
        visible = 'none'
        if current_user.team_registered == False:
            current_user.team_registered = True 
            db.session.add(current_user)
            db.session.commit()
        
    form = MemberRegistrationForm()
    if request.method == "POST":        
        if form.validate_on_submit():
            member = Member(group_id=current_user.id,\
            phone=form.phone.data,\
            email=form.email.data,\
            name=form.name.data,\
            student_number=form.student_number.data,\
            sex = form.sex.data,\
            ethnic=form.ethnic.data,\
            student_type=form.student_type.data,\
            province=form.province.data,\
            school=form.school.data,\
            discipline=form.discipline.data,\
            specialty=form.specialty.data,\
            grade=form.grade.data,\
            faculty=form.faculty.data,\
            grad_time=form.grad_time.data,\
            teacher_assigned=form.teacher_assigned.data,\
            id_type=form.id_type.data,\
            id_number=form.id_number.data,\
            address=form.address.data,\
            zip_code=form.zip_code.data)
            
            db.session.add(member)
            db.session.commit()

            flash('队员报名成功！')
        else:
            flash('信息有错误!!!')        
    return render_template('dashboard/team_info.html', visible=visible, template_name=template_name, form=form, members=members)




# Upload Solutions
@main.route('/dashboard/upload', methods=['GET', 'POST'])
@login_required
def upload():
    template_name='上传论文'
    form = UploadForm()
    if request.method == 'POST':
        if not form.validate_filename(form):
            flash('文件名不正确')
            redirect(url_for('main.upload'))
        if form.validate_on_submit() and form.validate_filename(form) :
            filename = secure_filename(form.file.data.filename)           
            form.file.data.save('uploads/' + filename)
            flash('上传完成')
    return render_template('dashboard/upload.html', form=form, template_name=template_name)





# Download Questions
@main.route('/dashboard/download', methods=['GET', 'POST'])
@login_required
def download_questions():
    template_name='下载试题'
    admin_settings = GetFile('admin_settings.json').Read()    
    site_data = {
        "doc_password": admin_settings['doc_password'],
        "zip_password_time":admin_settings['zip_password_time']        
    }
    return render_template('dashboard/download.html', site_data=site_data,template_name=template_name)





# MD5 code submission
@main.route('/dashboard/md5', methods=['GET', 'POST'])
@login_required
def md5():
    template_name='提交识别码'
    form = MD5Form()
    md5_status = {
        "actual": current_user.md5_code,
        "code_submission_time": current_user.md5_code_date
    }
    if md5_status['actual'] != None:
        form.submit.label.text = '重新提交识别码'

    if request.method == "POST":
        if form.validate_on_submit():
            current_user.md5_code = form.md5_code.data
            current_user.md5_code_date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            db.session.add(current_user)
            flash('识别码提交成功！')
            form.reset()
            redirect(url_for('main.md5'))
    # form.submit.label.text = 'asd'
    return render_template('dashboard/md5.html', form=form, md5_status=md5_status,template_name=template_name)






# A download endpoint, to download the file
@main.route('/download/<path:object_name>')
@login_required
def download(object_name):
    my_object = storage.get(object_name)
    if my_object:
        download_url = my_object.download_url()
        return redirect(download_url)
    else:   
        abort(404, "File doesn't exist")