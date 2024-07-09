import shutil
import subprocess


def main():
    completed = subprocess.call(["git", "init"])
    if not completed:
        print("Git repository not setup")
    shutil.copyfile(".env.dist", ".env")


if __name__ == "__main__":
    main()
