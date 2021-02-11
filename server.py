from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play/")
def mainroute(n=3):
    return render_template("index.html", x=n)

@app.route("/play/<int:n>/")
def multiplySquares(n):
    return render_template("index.html", x = n)

@app.route("/play/<int:n>/<string:color>/")
def colorpicker(color="aquamarine", n=3):
    return render_template("index.html", x = n, bg_color=color)

if __name__=="__main__":
    app.run(debug=True)