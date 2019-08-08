#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from datetime import timedelta
from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify

__appname__ = 'JMG'
__rootdir__ = os.path.abspath(os.getcwd())

staticfolder = __rootdir__ + '/app/static'
templatefolder = __rootdir__ + '/app/templates'

app = Flask(__appname__, static_folder=staticfolder, template_folder=templatefolder, root_path=__rootdir__)
load_dotenv(verbose=True, dotenv_path=__rootdir__ + '/.env')


# Home route
@app.route('/', methods = ['GET'])
def home():

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
