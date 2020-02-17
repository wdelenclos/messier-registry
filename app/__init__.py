"""This is init module."""
from flask import Flask

# Place where app is defined
app = Flask(__name__)
from app import root
from app import objects
from app import articles
from app import images