from flask import Flask, render_template, request, redirect, url_for, session
import time
import dataset

app = Flask(__name__)



@app.route('/')
def home():
	return render_template ("home.html")
	