import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, render_template, request
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
bootstrap = Bootstrap(app)




from app import routes