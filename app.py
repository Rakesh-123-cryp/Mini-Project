from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

@app.route("/")
def initial():
    return render_template(r"User/rakesh/Desktop/Kivy_app/Mini-Project/index1.html")

@app.route("/login")
def index():
    if request.method == "GET":
        var1 = request.args.get('email')
        return "<h1>var1</h1>"#redirect(url_for("redicrected_page" , var = var1))
@app.route("/redirected")
def redicrected_page(var):
    return var

if(__name__ == "__main__"):
    app.run(debug = True)
