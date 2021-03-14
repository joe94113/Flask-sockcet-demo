from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
app.debug = True

sockets = Sockets(app)  # 包上sockets


@sockets.route('/echo')
def echo_socket(ws):
    while True:
        # 收到前端發送socket open
        message = ws.receive()
        if (message == "socket open"):
            ws.send("歡迎使用客服機器人")
        else:
            ws.send(message)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/echo_test', methods=['GET'])
def echo_test():
    return render_template('index.html')


# https://github.com/heroku-python/flask-sockets 套件官方說明
if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('', 8000), app, handler_class=WebSocketHandler)
    server.serve_forever()

