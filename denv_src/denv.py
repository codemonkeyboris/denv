# #!/usr/bin/python3
# import sys
# import os
# import subprocess


# DOCKER_IMAGE = "denv"

# def main():
#     if len(sys.argv) < 2:
#         print("Usage: denv.py <command> [arguments...]")
#         sys.exit(1)

#     command = sys.argv[1]
#     docker_command = ["sudo", "docker", "run", "-it", "--rm", "-v", f"{os.getcwd()}:/app", DOCKER_IMAGE] + sys.argv[1:]

#     try:
#         subprocess.run(docker_command, check=True, stderr=subprocess.DEVNULL)
#     except subprocess.CalledProcessError as e:
#         if e.returncode == 127:
#             print(f"Error: Command '{command}' not found in the Docker container.")
#         sys.exit(1)

# if __name__ == "__main__":
#     main()


#!/usr/bin/python3
import sys
import os
import subprocess


DOCKER_IMAGE = "denv"

def main():
    if len(sys.argv) < 2:
        print("Usage: denv.py <command> [arguments...]")
        sys.exit(1)

    command = sys.argv[1]
    docker_command = ["sudo", "docker", "run", "-it", "--rm", "--privileged", "--device=/dev:/dev", "-v", f"{os.getcwd()}:/app", DOCKER_IMAGE] + sys.argv[1:]

    try:
        subprocess.run(docker_command, check=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        if e.returncode == 127:
            print(f"Error: Command '{command}' not found in the Docker container.")
        sys.exit(1)

if __name__ == "__main__":
    main()




# #!/usr/bin/python3
# import sys
# import os
# import subprocess
# import argparse

# DOCKER_IMAGE = "denv"

# def main():
#     parser = argparse.ArgumentParser(description="Run a command in a Docker container.")
#     parser.add_argument("command", nargs=argparse.REMAINDER, help="The command to run in the Docker container.")
#     parser.add_argument("--device", help="The device to pass to the Docker container (e.g., /dev/ttyUSB0).")

#     args = parser.parse_args()

#     if not args.command:
#         parser.print_help()
#         sys.exit(1)

#     device_arg = [f"--device={args.device}"] if args.device else []
    
#     # Docker run command with device argument
#     docker_command = [
#         "sudo", "docker", "run", "-it", "--rm", 
#         *device_arg,  # Pass the specified device to the container if provided
#         "-v", f"{os.getcwd()}:/app", DOCKER_IMAGE,
#         "bash", "-c",
#         f"ls {args.device} && {' '.join(args.command)}"
#     ]

#     try:
#         subprocess.run(docker_command, check=True, stderr=subprocess.DEVNULL)
#     except subprocess.CalledProcessError as e:
#         if e.returncode == 127:
#             print(f"Error: Command '{args.command[0]}' not found in the Docker container.")
#         sys.exit(1)

# if __name__ == "__main__":
#     main()

