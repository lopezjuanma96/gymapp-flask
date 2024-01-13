from flask import Blueprint, render_template, redirect, url_for, flash
# from flask import request
from werkzeug.security import generate_password_hash
from ..forms.register_form import RegisterForm
from ..models.user import User

bp = Blueprint('register', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(
            username=form.username.data
            ).first()
        if existing_user is None:
            hashed_password = generate_password_hash(
                form.password.data,
                )
            new_user = User(
                username=form.username.data,
                password=hashed_password
                )
            new_user.add()
            flash('Thanks for registering!')
            return redirect(url_for('login.login'))
        flash('A user already exists with that username.')
    return render_template('register.html', form=form)
