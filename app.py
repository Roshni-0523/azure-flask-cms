from flask import Flask, render_template, request, redirect, session
import pyodbc
import os

app = Flask(__name__)
app.secret_key = "secret"

server = os.environ.get("DB_SERVER")
database = os.environ.get("DB_NAME")
username = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")

conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
)

@app.route('/')
def home():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return render_template("dashboard.html", posts=posts)

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form['username']
        pwd = request.form['password']

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user,pwd))
        result = cursor.fetchone()

        if result:
            session['user'] = user
            return redirect("/")
    
    return render_template("login.html")

@app.route('/create', methods=["GET","POST"])
def create():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        body = request.form['body']

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO posts (title,author,body) VALUES (?,?,?)",
            (title,author,body)
        )
        conn.commit()

        return redirect("/")

    return render_template("create_post.html")

if __name__ == "__main__":
    app.run()