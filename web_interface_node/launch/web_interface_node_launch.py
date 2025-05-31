# web_interface_node/launch/web_interface.launch.py
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
            executable='web_server',
            output='screen'
        ),
        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            output='screen'
        )
    ])
