import hashlib
from flask import Flask,request
from db_manager import add_url,get_url

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
        add_url(url,shorten_link)
        return {"status":"success","url":shorten_link}
    
    return {"status":"falied","url":''}

@app.route('/unshorten', methods=['POST','GET'])
def unshorten():
    shorten_url = request.args.get('url')
    orginal_url = get_url(shorten_url)
    if orginal_url:
        return {"status":"success","url":orginal_url}
    
    return {"status":"failed","url":''}


if __name__ =="__main__":
    app.run(host = '0.0.0.0', port = 3000, debug=True)
