from flask import Flask,request,render_template,redirect
import requests

app = Flask(__name__)

URL = "http://127.0.0.1:3000"


@app.route('/shorten', methods=['POST','GET'])
def shorten():
    short = ''
    if  request.method == 'GET':
        url = request.args.get('url')
        x = requests.get(f"{URL}/shorten?url={url}").json()
        short = x['url']

    return render_template("home.html", short_url=f'http://127.0.0.1:4000/{short}')


@app.route('/<token>', methods=['POST','GET'])
def unshorten(token):
    url = token
    if  request.method == 'GET':
        x = requests.get(f"{URL}/unshorten?url={url}").json()
        short = x['url']
        return redirect(short)
    
    return render_template("home.html", short_url=f'{short}')


if __name__ =="__main__":
    app.run(host= '0.0.0.0',port = 4000,debug=True)
