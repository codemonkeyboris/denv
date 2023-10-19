#!/usr/bin/python3  
# must be top line

import sys
import os
import subprocess

DEBUG = False
DOCKER_IMAGE = "denv"


def debug_print(obj): 
    if DEBUG:
        print(obj)

def main():
    debug_print("HELLO DENV!")
    if len(sys.argv) < 2:
        print("Usage: denv.py <command> [arguments...]")
        sys.exit(1)

    command = sys.argv[1]
    docker_command = ["sudo", "docker", "run", "-it", "--rm", "--privileged", "--device=/dev:/dev", "-v", f"{os.getcwd()}:/app", DOCKER_IMAGE] + sys.argv[1:]

    debug_print(docker_command)
    try:
        subprocess.run(docker_command, check=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        if e.returncode == 127:
            print(f"Error: Command '{command}' not found in the Docker container.")
        sys.exit(1)

if __name__ == "__main__":
    main()
