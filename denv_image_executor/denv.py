#!/usr/bin/python3
import sys
import os
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: denv.py <command> [arguments...]")
        sys.exit(1)

    command = sys.argv[1]

    docker_image = "denv"  # Replace with your Docker image name

    # Combine the command and any additional arguments
    docker_command = ["sudo", "docker", "run", "-it", "--rm", "-v", f"{os.getcwd()}:/app", docker_image] + sys.argv[1:]

    try:
        subprocess.run(docker_command, check=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        if e.returncode == 127:
            print(f"Error: Command '{command}' not found in the Docker container.")
        sys.exit(1)

if __name__ == "__main__":
    main()
