from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='esp32_bridge',
            executable='esp32_bridge_node',
            name='esp32_bridge_node',
            output='screen'
        )
    ])
