from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField,\
                     SelectField, TextAreaField
from wtforms.validators import Required, Optional, Length, Email, Regexp, EqualTo, NumberRange
from wtforms import ValidationError
from ..models import User, Member
from werkzeug.datastructures import MultiDict



class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('下次自动登录')    
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('电子邮箱', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField('用户名', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('密码', validators=[
        Required(), EqualTo('password2', message='确认密码不正确，请重新输入！')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('帐号已被注册')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('原密码', validators=[Required()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='确认密码不正确，请重新输入')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('修改密码')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField('修改密码')


class PasswordResetForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='确认密码不正确，请重新输入')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('修改密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('邮箱不正确')


class ChangeEmailForm(FlaskForm):
    email = StringField('新邮箱', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('修改密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')

class ContactForm(FlaskForm):
    purpose = SelectField('留言类型', choices=[('赛事信息','赛事信息'),\
     ('赛事信息','参赛咨询'), ('队员信息填写','队员信息填写'),\
     ('审核与缴费','审核与缴费'), ('试题下载','试题下载'), ('论文提交','论文提交'),\
      ('证书及奖金领取','证书及奖金领取'), ('其它','其它')])
    message = TextAreaField('内容', validators=[Required()])
    submit = SubmitField('提交')

class PaymentForm(FlaskForm):
    amount = StringField('RMB', validators=[Required(), NumberRange()])
    submit = SubmitField('缴费')

class MemberRegistrationForm(FlaskForm):
    phone = StringField('联系电话', validators=[Required()])
    email = StringField('联系邮箱', validators=[Required(), Length(1, 64), Email()])
    name = StringField('真实姓名', validators=[Required()])
    student_number = StringField('学生号', validators=[Required()])
    sex = SelectField('性别', choices=[('男','男'), ('女', '女')])
    ethnic = StringField('民族', validators=[Required()])
    province = StringField('省份', validators=[Required()])
    school = StringField('学校', validators=[Required()])
    student_type = StringField('学生类型', validators=[Required()])
    discipline = StringField('专业', validators=[Required()])
    specialty = StringField('研究方向', validators=[Optional()])
    grade =StringField('年级', validators=[Required()])
    faculty = StringField('院系名称', validators=[Required()])
    grad_time = StringField('预期毕业时间', validators=[Required()])
    teacher_assigned = StringField('本队指导老师', validators=[Optional()])
    id_type = SelectField('证件', choices=[('身份证','身份证'), ('护照', '护照')])
    id_number = StringField('证件号', validators=[Required()])
    address = StringField('通讯地址', validators=[Required()])
    zip_code = StringField('邮编', validators=[Required()])
    submit = SubmitField('提交信息')
    
    def validate_email(self, field):
        if Member.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')
    def validate_phone(self, field):
        if Member.query.filter_by(email=field.data).first():
            raise ValidationError('电话号已被注册')
    def validate_id(self, field):
        if Member.query.filter_by(email=field.data).first():
            raise ValidationError('身份证号已被注册')




class MD5Form(FlaskForm):
    md5_code = StringField('识别码', validators=[Required()])
    submit = SubmitField('提交信息')
    
    def reset(self):
        data = MultiDict([ ('csrf', self.generate_csrf_token() ) ])
        self.process(data)





class UploadForm(FlaskForm):    
    file = FileField('上传论文', validators = [ \
        FileRequired(),\
        FileAllowed(['pdf'], '只允许PDF文件')
        ])
    question_number = SelectField('试题号', choices=[('A','A'), ('B', 'B'), ('C', 'C'),\
     ('D', 'D'), ('E', 'E')])    
    submit = SubmitField('上传')
    
    def validate_filename(self, field):
        if field.file.data.filename == str(field.question_number.data)+str(current_user.id)+'.pdf':
            return True      



