from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from forms import RegistrationForm, LoginForm
from models import app, db, User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app.config.from_object('config.Config')

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')

        # Set a cookie to mark that the user has registered
        response = make_response(redirect(url_for('login')))
        # Cookie valid for 30 days
        response.set_cookie('registered', 'true', max_age=30*24*60*60)
        return response
    return render_template('signup.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/chat")
@login_required
def chat():
    return render_template('chat.html', title='Chat')


if __name__ == '__main__':
    app.run(debug=True)
