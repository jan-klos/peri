from flask import Flask, render_template, request, redirect, send_file, g
import os
import sqlite3
import chart

app = Flask(__name__)

db = sqlite3.connect('/home/komp/peri_db/database.db', check_same_thread=False)
cursor = db.cursor()


@app.route("/")
def main(error="", success=""):
    return render_template("main.html", error=error, success=success)


@app.route("/", methods=["POST"])
def main_post():
    error = "You must enter something"
    template_data = {"test": 12}
    if "led_submit" in request.form:
        if "led_rb" in request.form:
            if request.form["led_rb"] == "led_on":
                return main(success="LED on")
            elif request.form["led_rb"] == "led_off":
                return main(success="LED off")
    elif "stat_submit" in request.form:
        if request.form["stat"] != "":
            cursor.execute('''SELECT time, value FROM luminosity''')
            chart.make_chart(cursor.fetchall())
            return render_template("stat.html", **template_data)
    return main(error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
