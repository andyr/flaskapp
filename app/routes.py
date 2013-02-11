#
#from webapp.controllers import main
#
## Flask routes
#def dispatch():
#    return [
#        ('/', main.Index)
#    ]

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
