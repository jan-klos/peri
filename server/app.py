from flask import Flask, render_template, request, redirect, send_file
import socket  # for IP address testing
import os

app = Flask(__name__)

@app.route("/")
def main(error=""):
    return render_template("main.html", error=error)


@app.route("/", methods=["POST"])
def main_post():
    error = "You must enter something"
    template_data = {"test": 12}
    if "led_submit" in request.form:
        if request.form["led"] != "":
            return render_template("led.html", **template_data)
    elif "stat_submit" in request.form:
        if not request.form["stat"] != "":
            return render_template("stat.html", **template_data)
    return main(error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
