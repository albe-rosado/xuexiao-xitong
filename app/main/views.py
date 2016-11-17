from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import main
from ..auth.forms import LoginForm, ChangePasswordForm, ChangeEmailForm
from ..models import User
from ..email import send_email

@main.route('/' , methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('index.html', form=form)

@main.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    template_name='选手首页'
    return render_template('dashboard/home.html', template_name=template_name)

@main.route('/dashboard/pay', methods=['GET', 'POST'])
def pay():
    template_name='网上缴费'
    flash("还没有缴费平台")
    return render_template('dashboard/pay.html', template_name=template_name)
