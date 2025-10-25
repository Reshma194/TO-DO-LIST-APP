from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app import db

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'username': 'admin',
    'password': '123'
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # ✅ Correct way to access dictionary values
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            flash('Login Successful!', 'success')
            return redirect(url_for('tasks.view_tasks'))  # Redirect to the task page
        else:
            flash('Invalid Credentials!', 'danger')

    # GET method just shows login page
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out!', 'info')
    return redirect(url_for('auth.login'))
