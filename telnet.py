#pip install Flask
from flask import Flask, jsonify, render_template, request
import socket 
app = Flask(__name__)

# test telnet  to a destination (ip or name) by reaching APP:5000/telnet/DEST/PORT
# and returns if it's down or reachable

@app.route('/')
def index():
    return render_template('./json.html')


@app.route('/SomeFunction')
def SomeFunction():
    print('In SomeFunction')
    return "Nothing"
    
@app.route('/telnet/<ip>/<port>')
def tst(ip=None, port=None):
    print('In SomeFunction')
    print(ip)
    if (isOpen(ip, port)):
        print ("ip "+str(ip) + " port " +str(port) + " REACHABLE!" )
        return "ip "+str(ip) + " port " +str(port) + " REACHABLE!"  
    else:
        print ("ip "+str(ip) + " port " +str(port) + " DOWN")
        return "ip "+str(ip) + " port " +str(port) + " DOWN"

                       
def isOpen(ip,port):                  
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.settimeout(5.0)
      s.connect((ip, int(port)))
      s.settimeout(None)      
      s.shutdown(2)
      return True    
   except:
      return False
      
if __name__ == '__main__':
   app.run(host= '0.0.0.0')
