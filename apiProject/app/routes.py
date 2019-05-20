from app import app
from fetchdef import *

@app.route('/')
@app.route('/index')

def index():
  
    result = snmpFetch("sysName")
    resultFull = api_fetch() + "\n" + result
    return resultFull

@app.route('/api_fetch')
def api_fetch():
    result = snmpFetch("sysUpTime")
    return result

#@app.route('/api_tcpInError')
#def api_tcpInError():
#   result = snmpFetch("ifNumbe")
#    return result

