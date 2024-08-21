from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[
        DataRequired(message="Email is required"),
        Email(message="Your email is not valid")
    ])
    password = PasswordField(label='Password', validators=[
        DataRequired(message="Your password is not valid"),
        Length(min=8, message="Please enter 8 characters")
    ])
    submit = SubmitField(label='Submit')


app = Flask(__name__)
app.secret_key = "sauravbista"
bootstrap = Bootstrap5(app)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")



        # Form is valid and has been submitted
        # Process the form data here
        return redirect(url_for('home'))
    # Render form with errors if not valid
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
