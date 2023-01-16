
import os
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution

def generate_launch_description():

    package_name = "ROS_Robot"

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare(package_name), "launch", "rsp.launch.py"
            ])
        ]),
        launch_arguments={"use_sim_time": "true"}.items()
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare("gazebo_ros"), "launch", "gazebo.launch.py"
            ])
        ])
    )

    spawn_entity = Node(package="gazebo_ros", 
    executable="spawn_entity.py",
    arguments=["-topic", "robot_description", "-entity", "my_bot"],
    output="screen")

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity
    ])