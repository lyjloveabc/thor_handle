import os


def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile

for row in dirlist("/Users/luoyanjie/classes-dex2jar", []):
    with open(row, 'rb') as f:
        for line in f.readlines():
            if 'Authorization' in str(line):
                print(row)
