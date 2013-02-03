
from webapp.controllers import main

# Flask routes
def dispatch():
    return [
        ('/', main.Index)
    ]
