#!/usr/bin/env python3
import sys
import os
import subprocess

def main():
    if len(sys.argv) < 3:
        print("Usage: denv.py <command> <script-path> [arguments...]")
        sys.exit(1)

    command = sys.argv[1]
    script_path = sys.argv[2]

    if not os.path.exists(script_path):
        print(f"Error: File '{script_path}' not found on the host.")
        sys.exit(1)

    docker_image = "denv"  # Replace with your Docker image name

    # Combine the command and script path, and append any additional arguments
    docker_command = ["sudo", "docker", "run", "-it", "--rm", "-v", f"{os.getcwd()}:/app", docker_image, command, script_path] + sys.argv[3:]

    try:
        subprocess.run(docker_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command in Docker container: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()




# #!/usr/bin/env python3
# import sys
# import os
# import subprocess

# def main():
#     if len(sys.argv) < 2:
#         print("Usage: denv.py <command>")
#         sys.exit(1)

#     command = sys.argv[1:]

#     docker_image = "denv"  # Replace with your Docker image name

#     docker_command = ["docker", "run", "-it", docker_image] + command

#     try:
#         subprocess.run(docker_command, check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error running command in Docker container: {e}")
#         sys.exit(1)

# if __name__ == "__main__":
#     main()



# #!/usr/bin/env python3
# import sys
# import os
# import subprocess

# def main():
#     if len(sys.argv) != 3:
#         print("Usage: denv.py <command> <script-path>")
#         sys.exit(1)

#     command = sys.argv[1]
#     script_path = sys.argv[2]

#     if not os.path.exists(script_path):
#         print(f"Error: File '{script_path}' not found on the host.")
#         sys.exit(1)

#     docker_image = "denv"  # Replace with your Docker image name

#     docker_command = ["sudo", "docker", "run", "-it", "--rm", "-v", "$(pwd):/app", docker_image, command, "${@:2}"]

#     try:
#         subprocess.run(docker_command, check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error running command in Docker container: {e}")
#         sys.exit(1)

# if __name__ == "__main__":
#     main()
