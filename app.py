# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 21:41:13 2025

@author: ADMIN
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('map.html', api_key="")

if __name__ == '__main__':
    app.run(debug=True)
