import os
import subprocess
import sys


def usage():
    msg = "Usage:\n\tpython migrate_packages OLD_PYTHON_PATH NEW_PYTHON_PATH"
    print(msg)


def get_all_packages(old_python_path):
    old_python_path = old_python_path.strip().replace("'", "").replace("\"", "")
    old_python_path = os.path.join(old_python_path, "python.exe")
    cmd = [old_python_path, "-m", "pip", "list"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    pip_list = proc.stdout.read().decode("utf-8").split("\r\n")
    all_packages = []
    for package in pip_list[2:-1]:
        package = "==".join("{} {}".format(package.split(" ")[
                            0], package.split(" ")[-1]).split())
        all_packages.append(package)
    return all_packages


def install_packages(new_python_path, list_of_packages):
    new_python_path = new_python_path.strip().replace("'", "").replace("\"", "")
    new_python_path = os.path.join(new_python_path, "python.exe")
    failed_installations = []
    for package in list_of_packages:
        cmd = [new_python_path, "-m", "pip", "install", package]
        success = subprocess.call(cmd)
        if not success:
            print("Failed to install {}".format(package))
            failed_installations.append(package)
    return failed_installations


def create_report(failed_installations):
    print("Number of failed installations:\n\t{}".format(
        len(failed_installations)))
    for package in failed_installations:
        print("\t{}".format(package))


def main():
    if len(sys.argv) < 3:
        usage()
        return
    list_of_packages = get_all_packages(sys.argv[1])
    failed_installations = install_packages(sys.argv[2], list_of_packages)
    create_report(failed_installations)


if __name__ == "__main__":
    main()
