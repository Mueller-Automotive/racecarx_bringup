from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution

from ament_index_python.packages import get_package_share_directory

from launch_ros.actions import Node

def generate_launch_description():
    pkg_racecarx_sim = get_package_share_directory(
        'racecarx_sim')
    pkg_racecarx_control = get_package_share_directory(
        'racecarx_control')

    sim_launch = PathJoinSubstitution(
        [pkg_racecarx_sim, 'launch', 'launch_sim.launch.py'])
    control_launch = PathJoinSubstitution(
        [pkg_racecarx_control, 'launch', 'launch_control.launch.py'])

    sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([sim_launch]),
    )
    control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([control_launch]),
    )

    return LaunchDescription([
        sim,
        control
    ])