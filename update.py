import os
import platform
import shlex
import subprocess
import sys

def update(path):
    for root, directory, files in os.walk(path):
        for name in files:
            name = os.path.join(root, name)
            # if "dropbot" in name:
            #     continue
            if "requirements.txt" in name:
                os.chdir(os.path.dirname(name))
                if platform.system() == "Windows":
                    cmd = "python -m pip install -r requirements.txt"
                else:
                    cmd = "pip install -r requirements.txt"
                print(os.path.dirname(name))
                try:
                    print(subprocess.check_output(shlex.split(cmd)).decode())
                except Exception as e:
                    print("Failed to install requirements for {}".format(root))
                finally:
                    continue

def main():
    update(sys.argv[1])

if __name__ == "__main__":
    main()
