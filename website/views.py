from flask import Blueprint

# define that this file is teh blueprint of our ptoject, split up files and folders nicely
views = Blueprint('views',__name__)

@views.route('/')
def home():
    return "<H1> Test </H1>"

