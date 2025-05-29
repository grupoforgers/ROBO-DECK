from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='web_interface_node',
            executable='web_interface_node_node',
            name='web_interface_node_node',
            output='screen'
        )
    ])
