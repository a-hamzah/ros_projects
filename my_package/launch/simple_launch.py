from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_package',
            executable='my_node',
            name='node1'
        ),
        Node(
            package='my_package',
            executable='test',
            name='node2',
        ),
        
    ])