from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sensor_node',
            executable='sensor_node_node',
            name='sensor_node_node',
            output='screen'
        )
    ])
