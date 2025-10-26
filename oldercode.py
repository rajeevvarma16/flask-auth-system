# import flask
# import flask_login
# # from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import SQLAlchemy

# app = flask.Flask(__name__)
# app.secret_key = 'super secret string'



# login_manager = flask_login.LoginManager()
# login_manager.init_app(app)
# users = {'raj@gm.com': {'password': '213'}}
# login_manager.login_view = 'login'

# class User(flask_login.UserMixin):
#     pass


# @login_manager.user_loader
# def user_loader(email):
#     if email not in users:
#         return
    
#     user = User()
#     user.id = email
#     return user

# @app.route('/')
# def home():
#     return "Home page works!"

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if flask.request.method == 'POST':
#         email = flask.request.form.get('username')  # from login.html input
#         password = flask.request.form.get('password')
#         if email in users and users[email]['password'] == password:
#             user = User()
#             user.id = email
#             flask_login.login_user(user)
#             return flask.redirect('/protected')
#         return "Invalid credentials! <a href='/login'>Try again</a>"
#     return flask.render_template('login.html')


# @app.route('/register', methods=['GET', 'POST'])
# def register():

#     if flask.request.method == 'POST':
#         email = flask.request.form.get('email')
#         password = flask.request.form.get('password')
#         # store in dummy users dict
#         users[email] = {'password': password}
#         return "Registration successful! <a href='/login'>Login now</a>"
#     return flask.render_template('register.html')

# @app.route('/forgotpassword', methods=['GET', 'POST'])
# def forgot_password():
#     if flask.request.method == 'POST':
#         email = flask.request.form.get('email')
#         return f"Password reset instructions sent to {email}"
#     return flask.render_template('forgotpassword.html')
    

# @app.route('/protected')
# @flask_login.login_required
# def protected():
#     print(users)

#     return 'Logged in as: ' + flask_login.current_user.id + " <br><a href='/logout'>Logout</a>"

# @app.route('/logout')
# def logout():
#     flask_login.logout_user()
#     return 'Logged out. <a href="/login">Login again</a>'

# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return 'Unauthorized', 401

# if __name__ == "__main__":

    
#     app.run(debug=True, port=8000)