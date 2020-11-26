import os
import shutil


def isDir(name):
    return len(name.split('.')) == 1


dirs = os.listdir()
c = 0
for i in dirs:
    if isDir(i):
        nd = os.listdir(i)
        os.mkdir('../images/{}'.format(i))
        for j in nd:
            pth = "{}/{}".format(i,j)
            sp = pth.split('.')
            sp[-1] = sp[-1].upper()
            npth = '.'.join(sp)
            to = '{}/{}'.format('../images',npth)
            print(npth)
            print(to)
            os.rename(pth, npth)
            shutil.move(npth, to)