
# Main controller module
from flask import render_template
from flask.views import MethodView

from webapp import config

class Index(MethodView):

    def get(self):
        # TODO: this needs to find the templates dir
        return render_template('index.html')

