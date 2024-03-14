import hashlib
from flask import Flask,request

def encoder(url):
    return str(int(hashlib.sha1(url.encode("utf-8")).hexdigest(), 16) % (10 ** 8))


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def main():
    return 'Hello'

@app.route('/shorten', methods=['POST','GET'])
def shorten():
    if request.method == "GET":
        url = request.args.get('url')
        shorten_link = encoder(url)
        return {"status":"success","url":shorten_link}
    
    return {"status":"falied","url":''}

@app.route('/unshorten', methods=['POST','GET'])
def unshorten():
    return 'Hello'


if __name__ =="__main__":
    app.run(debug=True)
