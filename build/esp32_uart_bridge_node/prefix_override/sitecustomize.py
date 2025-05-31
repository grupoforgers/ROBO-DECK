import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/forgers/ros2_ws/src/ROBO-DECK/install/esp32_uart_bridge_node'
