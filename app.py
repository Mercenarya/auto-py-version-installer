import requests
import os


python_current_version = os.system("python --version")
directory = "C/SetupPyVersion/"
py_version = input("enter your version (example: 3.11.0 or 3.9.0): ")


def check_dir(dir):
    try:
        if os.path.exists(dir):
            for file in dir:
                print(os.listdir(file))
                
        else:
            return "Directory doesn't exists"
    except OSError as error:
        return error


def setup_folder(path):
    try:
        if os.path.exists(path):
            print(setup_py(py_version,directory))
            return "Exists Folder"
        else:
            os.makedirs(path)
            print(setup_py(py_version,directory))
    except OSError as error:
        return error

def setup_py(version,path):
    
    url = f"https://www.python.org/ftp/python/{version}/python-{version}-amd64.exe"
    response = requests.get(url=url,timeout=1)
    if response.status_code == 200:
        with open(f"{path}/setup-python-{version}.exe",'wb') as file:
            file.write(response.content)
        return f".exe path directed installation processing complete\nOpen C:/SetupPyVersion/\n Python version: "
    else:
        return f"{response.status_code}"
if __name__ == "__main__":
    try:
        check_dir(directory)
        print(f"current version: {python_current_version}")
        print(setup_folder(directory))
    except Exception as error:
        print(error)
    