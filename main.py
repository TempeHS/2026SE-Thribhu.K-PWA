from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)


@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    data = dbHandler.listExtension()
    return render_template("/index.html", content=data)


@app.route("/about.html", methods=["GET"])
def about():
    return render_template("/about.html")


@app.route("/add.html", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        try:
            dbHandler.insertContact(email, name)
            return render_template("/add.html", is_done=True)
        except Exception as e:
            return render_template(
                "/add.html", err=True, errmsg=f"Email not unique: {e}"
            )
    else:
        return render_template("/add.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
