import argparse

import pybullet
import time
from robot_descriptions.loaders.pybullet import load_robot_description

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="name of the robot description")
    args = parser.parse_args()

    pybullet.connect(pybullet.GUI)

    try:
        robot = load_robot_description(args.name)
    except ModuleNotFoundError:
        robot = load_robot_description(f"{args.name}_description")

    print(f"Robot successfully loaded with an ID of {robot}")
    time.sleep(10)
    pybullet.disconnect()
