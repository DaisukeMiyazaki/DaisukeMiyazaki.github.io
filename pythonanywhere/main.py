#!/usr/bin/env python
from flask import Flask, redirect, request, render_template, url_for
import logging, io, base64, os, datetime, time
from datetime import datetime
app = Flask(__name__)
@app.route("/signup", methods=['POST', 'GET'])
def signup_page():
    if request.method == 'POST':
        email_param = request.form['email_address']
        signup_page_param = request.form['signup_page']
        url = "https://mdaisuke.net/" + signup_page_param
        if email_param is not None and signup_page_param is not None:
            st = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            # save to file and send thank you note
            with open("email_repo.txt","a") as myfile:
                myfile.write('Timestamp: ' + st + ' email:' + email_param + ' source:' + signup_page_param + '\n')
        if "/en/" in signup_page_param:
            return redirect(url_for('static', filename='thanks_en.html', to_url=url))
    return redirect(url_for('static', filename='thanks.html', to_url=url))
