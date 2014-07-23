# -*- coding: utf-8 -*-
# views.py

from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('template.html')

