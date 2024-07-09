import shutil
import subprocess


def main():
    failed = subprocess.call(["git", "init"])
    if not failed:
        subprocess.call(["git", "add", "*"])
        subprocess.call(["git", "commit", "-m", "Initial commit"])
    else:
        print("Git repository not setup")
    shutil.copyfile(".env.dist", ".env")


if __name__ == "__main__":
    main()
