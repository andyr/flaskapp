
import logging, os, sys
from flask import Flask


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src = os.path.join(project_root, 'src')
templates = os.path.join(project_root, 'templates')
static = os.path.join(project_root, 'static')


@app.route('/')
def hello_world():
    return 'hello world'



if __name__ == '__main__':
    if src not in sys.path:
        sys.path.insert(sys.path.insert(0, src))

    from webapp import router
    # TODO: hook the router to the application

    app = Flask(__name__,
        static_folder=static,
        template_folder=templates
    )
    app.debug = True
    app.run(host='0.0.0.0')
