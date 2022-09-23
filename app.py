from flask import Flask, render_template,request,redirect,url_for,session
import csv
app = Flask(__name__)
app.secret_key = "abcd"
@app.route("/")
def initial():
    session["login_status"] = False
    if session["login_status"] == True:
        return render_template("index.html", status = session["login_status"])
    return render_template("index.html", status = session["login_status"])

@app.route("/login",methods = ["POST","GET"])
def index():
    if request.method == "POST" and request.form['submit'] == 'Login':
        mail = request.form['email']
        passwd = request.form['password']
        with open ("files/customers.csv","r") as file:
            r = csv.reader(file)
            for i in r:
                check = 0
                if i[0] == mail and i[1] == password:
                    check = 1
                    break
            if check == 0:
                return redirect(url_for("/login" , auth = False))
            session["login_status"] = True
            return redirect(url_for("initial" , status = session['login_status']))
    else:
        return render_template("login.html")
@app.route("/signup")
def redicrected_page(var):
    if request.method == "POST" and request.form['submit'] == 'Login':
        details = []

        with open ("files/customers.csv","w+") as file:
            w = csv.writer(file)
            details.append(request.form['email'])
            details.append(request.form['password'])
            details.append(request.form['confirm_password'])
            w.writerow(details)

if(__name__ == "__main__"):
    app.run(debug = True)
