import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Float32, Int16MultiArray
import serial

class ESP32SerialBridge(Node):
    def __init__(self):
        super().__init__('esp32_serial_bridge')
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        self.sharp_pub = self.create_publisher(Int16MultiArray, 'sharp', 10)
        # (...outros publishers...)

        self.create_timer(0.5, self.read_serial)

    def read_serial(self):
        if self.ser.in_waiting:
            line = self.ser.readline().decode('utf-8').strip()
            # (...parse da linha e publicação...)

def main(args=None):
    rclpy.init(args=args)
    node = ESP32SerialBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

