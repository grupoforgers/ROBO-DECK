import rclpy
from rclpy.node import Node
from flask import Flask, send_from_directory
import threading
import os

class WebInterfaceNode(Node):
    def __init__(self):
        super().__init__('web_interface_node')
        self.get_logger().info('Servidor web iniciado.')

app = Flask(__name__, static_folder='../web')

@app.route('/')
def index():
    return send_from_directory('../web', 'index.html')

def main():
    rclpy.init()
    node = WebInterfaceNode()

    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000)).start()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()