from flask import Flask, render_template,request,redirect,url_for,session
import mysql.connector as mc
my_db = mc.connect(user = "root" , host = "localhost" , password = "22072003Rr" , database = "MiniProject ")
cur = my_db.cursor()
app = Flask(__name__)
app.secret_key = "abcd"


@app.route("/guest/browse")
def browse_guest():
    return render_template('browse.html', username = "Login")


@app.route("/")
def initial():
    session["status"] = False
    return render_template("index.html", username = "Login")


@app.route("/<username>/browse")
def browse_page(username):
    if session['status'] == False:
        return redirect(url_for("browse_guest"))
    return render_template('browse.html', username = username)


@app.route("/<username>")
def logged(username):
    if session["status"] == False:
        return redirect(url_for("index"))
    return render_template("index.html" , username = username)


@app.route("/login",methods = ["POST","GET"])
def index():
    if session['status'] == False:
        if request.method == "POST" and request.form['submit'] == 'Login':
            mail = request.form['email']
            passwd = request.form['password']
            cur.execute(f"SELECT Username FROM USERS WHERE Mail = '" + f"{mail}" + "' AND Password = '" f"{passwd}" + "'")
            Id_s = cur.fetchall()
            print(Id_s)
            if len(Id_s) == 0:
                return redirect(url_for("wrongpass"))
            else:
                session["status"] = True
                session["username"] = Id_s[0][0]
                return redirect(url_for("logged" , username = Id_s[0][0]))
        else:
            return render_template("login.html")
    else:
        return redirect(url_for("my_profile" , username = session["username"]))

@app.route("/signup")
def sign_up_page():
    if request.method == "POST" and request.form['submit'] == 'Login':
        name = request.form['name']
        mail = request.form['email']
        passwd = request.form['email']
        cur.execute("INSERT INTO USERS VALUES('" + name + "','" + mail + "','" + passwd + "'" + ")")
        session['status'] = True
        session['username'] = name
        return redirect(url_for("logged" , username = name))
    else:
        return render_template("signup.html")

@app.route("/home")
def home_button():
    if session["status"] == True:
        return redirect(url_for("logged", username = session['username']))
    return redirect(url_for("initial"))

@app.route("/wrongpass", methods = ["POST","GET"])
def wrongpass():
    if session['status'] == False:
        if request.method == "POST" and request.form['submit'] == 'Login':
            mail = request.form['email']
            passwd = request.form['password']
            cur.execute(f"SELECT Username FROM USERS WHERE Mail = '" + f"{mail}" + "' AND Password = '" f"{passwd}" + "'")
            Id_s = cur.fetchall()
            print(Id_s)
            if len(Id_s) == 0:
                return redirect(url_for("wrongpass"))
            else:
                session["status"] = True
                session["username"] = Id_s[0][0]
                return redirect(url_for("logged" , username = Id_s[0][0]))
        else:
            return render_template("wrongpass.html")

@app.route("/<username>/profile")
def my_profile(username):
    
@app.route("/terms")
def terms():
    return render_template("terms.html")
if(__name__ == "__main__"):
    app.run(debug = True)
