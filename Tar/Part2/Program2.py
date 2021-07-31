from os import listdir
from os.path import isfile, join, isdir
import tarfile


def searchPassword(path):
    if (isdir(path)):
        contents = listdir(path)
        for item in contents:
            mypath = join(path, item)
            if item[-7:] == ".tar.gz":
                my_tar = tarfile.open(mypath)
                my_tar.extractall(mypath[:-7]) # specify which folder to extract to
                my_tar.close()
                searchPassword(mypath[:-7])
            else:
                searchPassword(mypath)
    else:
        with open(path, encoding="utf-8") as soubor:
            text = soubor.read()
            print(text, end="")
            if text != 'Tady heslo nenajdeš!\n':
                quit()


searchPassword(".\\heslo")
