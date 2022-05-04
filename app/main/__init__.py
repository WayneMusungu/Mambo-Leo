# from distutils.command.config import config
# from ensurepip import bootstrap
from flask import Blueprint, Flask
main = Blueprint('main',__name__)
from . import views,error
