from app import app
from fetchdef import *

@app.route('/')
@app.route('/index')

def index():
    #listsnmp = ["sysUpTime","sysName", "sysObjectID"]
    #for i in range(3):
    result = snmpFetch("sysName")
    api_fetch()
    return result

@app.route('/api_fetch')
def api_fetch():
    result = snmpFetch("sysUpTime")
    return result

