from app import app
from fetchdef import *

@app.route('/')
@app.route('/index')
def index():
    result = snmpFetch()
    return result
