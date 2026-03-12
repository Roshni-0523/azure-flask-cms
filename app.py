from flask import Flask, render_template, request, redirect, session
import pyodbc
import os
import logging

app = Flask(__name__)
app.secret_key = "secret"

# Enable logging
logging.basicConfig(level=logging.INFO)

# Azure SQL connection info from environment variables
server = os.environ.get("DB_SERVER")
database = os.environ.get("DB_NAME")
username = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")

conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template("home.html")


# ---------------- LOGIN ----------------
@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":

        user = request.form['username']
        pwd = request.form['password']

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (user, pwd)
        )

        result = cursor.fetchone()

        if result:
            logging.info(f"{user} logged in successfully")
            session['user'] = user
            return redirect("/dashboard")

        else:
            logging.warning("Invalid login attempt")

    return render_template("login.html")


# ---------------- CREATE POST ----------------
@app.route('/create', methods=["GET", "POST"])
def create():

    if 'user' not in session:
        return redirect("/login")

    if request.method == "POST":

        title = request.form['title']
        author = request.form['author']
        body = request.form['content']

        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO posts (title, author, body) VALUES (?, ?, ?)",
            (title, author, body)
        )

        conn.commit()

        return redirect("/dashboard")

    return render_template("create_post.html")


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect("/login")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts")

    posts = cursor.fetchall()

    return render_template("dashboard.html", posts=posts)


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect("/login")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run()