#!/usr/bin/env python 
"""
Entry point for the application for the rest api
"""
from flask import Flask, jsonify

app = Flask(__name__)

if __name__ == '__main__':
	app.run()