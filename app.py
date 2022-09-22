from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def initial():
    session["login_status"] = False
    return render_template(r"index.html", status = session["login_status"])

@app.route("/login")
def index():
    if request.method == "POST":
        mail = request.forms['email']
        passwd = request.forms['password']
        
        return redirect("/redicrected" , var = var1)
@app.route("/redirected")
def redicrected_page(var):
    return var

if(__name__ == "__main__"):
    app.run(debug = True)
