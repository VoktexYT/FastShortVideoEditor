from flask import Flask, render_template, request, url_for, flash, redirect
import os


def confVideo():

    TEMPLATE_DIR = os.path.abspath('template')
    STATIC_DIR = os.path.abspath('static')
    app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

    @app.route('/config-project/', methods=['GET', 'POST'])
    def conf():
        #print(request.form['projectName'])
        return render_template("config.html")

    app.run(debug=True)

confVideo()
