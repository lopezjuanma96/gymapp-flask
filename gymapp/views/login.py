from flask import Blueprint, render_template, redirect, url_for, flash
# from flask import request
from werkzeug.security import check_password_hash
from ..forms.login_form import LoginForm
from ..models.user import User  # Uncomment this when you have a User model

bp = Blueprint('login', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            if user.admin:
                return redirect(url_for('home.admin'))
            return redirect(url_for('home.index'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form)
