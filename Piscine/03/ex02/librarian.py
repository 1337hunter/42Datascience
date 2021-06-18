import os
import zipfile

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

def CheckEnv():
    path = os.sys.prefix.split('/')
    if not path or path[-1] != "gbright":
        print("Change our emvironment to gbright")
        exit()

def main():
    CheckEnv()
    os.system("python3 -m pip install beautifulsoup4 pytest > /dev/null")
    os.system("python -m pip list --format=freeze")
    os.system("python -m pip list --format=freeze > requirements.txt")
    try:
        zipf = zipfile.ZipFile('gbright.zip', 'w', zipfile.ZIP_DEFLATED)
        zipdir('./gbright', zipf)
    except:
        print("File handle error")
        exit()
    zipf.close()

if __name__ == '__main__':
    main()