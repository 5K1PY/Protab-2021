from os import listdir
from os.path import isfile, join
import tarfile

i = 0
while True:
    if i % 100 == 0:
        print(i)
    my_tar = tarfile.open(f"./{i%2}/heslo.tar.gz")

    mypath = f"./{(i+1)%2}"
    my_tar.extractall(mypath)  # specify which folder to extract to
    my_tar.close()

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for f in onlyfiles:
        if f != "heslo.tar.gz":
            print(f)
            quit()

    i += 1
