import os
import subprocess
import sys

def update(path):
    for root, directory, files in os.walk(path):
        for name in files:
            name = os.path.join(root, name)
            if "dropbot" in name:
                continue
            if "requirements.txt" in name:
                os.chdir(os.path.dirname(name))
                cmd = "pip install -r requirements.txt"
                print(os.path.dirname(name))
                print(subprocess.check_output(["pip", "install", "-r", "requirements.txt"]).decode())

def main():
    update(sys.argv[1])

if __name__ == "__main__":
    main()
