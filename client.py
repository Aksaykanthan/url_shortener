from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def main():
    return 'Hello'

@app.route('/shorten', methods=['POST','GET'])
def shorten():
    return 'hello'

@app.route('/unshorten', methods=['POST','GET'])
def unshorten():
    return 'Hello'


if __name__ =="__main__":
    app.run(debug=True)
