import urllib
import urlparse
import httplib
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    url=request.form['handler']
    host = urlparse.urlparse(url).hostname
    #FLAG 3
    if '10.0.0.38' in url or 'secrety.corp' in url:
        return 'Restricted Area!'
    #FLAG 4
    if host == 'hidey.corp':
        return 'Restricted Area!'
    else:
        return urllib.urlopen(url).read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
