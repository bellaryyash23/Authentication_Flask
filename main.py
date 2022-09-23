import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email_entered = request.form.get("email")
        if User.query.filter_by(email=email_entered).first():
            flash("User already registered. Please try to Login.")
            return render_template("register.html")
        else:
            password = request.form.get("password")
            hash_password = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)
            new_user = User(
                email=request.form.get("email"),
                password=hash_password,
                name=request.form.get("name")
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets"))
    else:
        return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email_entered = request.form.get("email")
        password_entered = request.form.get("password")
        user = User.query.filter_by(email=email_entered).first()
        if user:
            if check_password_hash(pwhash=user.password, password=password_entered):
                login_user(user)
                return redirect(url_for("secrets"))
            else:
                flash("Check Login Credentials.")
                return render_template("login.html")
        else:
            flash("Enter Valid E-Mail ID")
            return render_template("login.html")
    else:
        return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", user=current_user, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory("static", filename="files/cheat_sheet.pdf")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    app.run(debug=True)
