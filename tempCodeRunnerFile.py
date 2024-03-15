import hashlib
from flask import Flask,request

def encoder(url):
    return str(int(hashlib.sha1(url.encode("utf-8")).hexdigest(), 16) % (10 ** 8))


s = "hello"
print(encoder(s))