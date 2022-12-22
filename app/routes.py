from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
@app.route('/dashboard')
def dashboard():
    liquid = LiquidViewData()
    try:
        ip = app.config['NODE_IP']
        port = app.config['NODE_PORT']
        user = app.config['RPC_USERNAME']
        password = app.config['RPC_PASSWORD']
        rpc_connection = AuthServiceProxy(f'http://{user}:{password}@{ip}:{port}')
        connection_count = rpc_connection.getconnectioncount()
        liquid.running = True
        if connection_count > 0:
            liquid.online = True
        liquid.block_height = rpc_connection.getblockcount()
        network_info = rpc_connection.getnetworkinfo()
        liquid.peer_count = network_info["connections"]
        liquid.version = network_info["subversion"]
        liquid.version = liquid.version.replace("/", "")
        liquid.version = liquid.version.replace("Elements Core:", "")
    except Exception as e:
        liquid.message = "An error occured. Mouseover to see."
        liquid.message_details = str(e)
    return render_template('dashboard.html', liquid=liquid)


class LiquidViewData:
    def __init__(self):
        self.running = False
        self.online = False
        self.peer_count = 0
        self.block_height = 0
        self.version = ""
        self.message = ""
        self.message_details = ""
