import os


def isDir(name):
    return len(name.split('.')) == 1


dirs = os.listdir()
c = 0
for i in dirs:
    if isDir(i):
        nd = os.listdir(i)
        for j in nd:
            pth = "{}/{}".format(i,j)
            sp = pth.split('.')
            sp[-1] = sp[-1].lower()
            npth = '.'.join(sp)
            print(npth)
            print(os.rename(pth, npth))