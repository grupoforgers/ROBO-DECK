from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rosbridge_server',
            executable='rosbridge_websocket',
            output='screen'
        ),
        Node(
            package='web_interface_node',
            executable='web_server.py',
            output='screen'
        )
    ])