from app import app, db
from flask import flash, redirect, render_template, url_for, session
from .forms import LoginForm, SigninForm, ReceiptForm
from .models import User, Receipt
from flask_login import login_user, login_required, current_user, logout_user
from create_e_receipt import create_receipt
from werkzeug.security import check_password_hash, generate_password_hash

@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash("Please check you login credentials and try again.")
        else:
            login_user(user)
            return redirect(url_for("dashboard"))

    return render_template("login.html", form=form)


@app.route("/signin", methods=["POST", "GET"])
def signin():
    form = SigninForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email address already exists.")
            return redirect(url_for("register"))
        else:
            new_user = User(email, username, password=generate_password_hash(password))

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("login"))

    return render_template("signin.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("login")

@app.route("/create-receipt", methods=["POST", "GET"])
@login_required
def receipt():
    form = ReceiptForm()

    if form.validate_on_submit():
        _from = form.ffrom.data
        _for = form.ffor.data
        amount = form.amount.data
        payment_type = form.payment_type.data
        date = form.date.data

        new_receipt = Receipt(_from=_from, _for=_for, amount=amount, payment_type=payment_type, date=date)
        db.session.add(new_receipt)
        db.session.commit()

        receipt_no = str(new_receipt.id)

        create_receipt(_from, _for, amount, payment_type, date, receipt_no=receipt_no)

        return redirect(location=url_for("static", filename="e-receipts/" + receipt_no + ".jpg"), code=302)

    return render_template("receipt.html", form=form)

@app.route("/dashboard")
@login_required
def dashboard():
    e_receipts = Receipt.query.all()
    return render_template("dashboard.html", current_user=current_user, e_receipts=e_receipts)

@app.route("/protected")
@login_required
def protected():
    return 'Protected Page. Welcome, ' + current_user.id
