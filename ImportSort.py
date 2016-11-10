import os
import os.path

key = '#import'

def traversal_pwd():
    fileName = []
    pwd = os.path.abspath('.')
    for root, dirs, files in os.walk(pwd):
        for name in files:
            nPos = name.find('.h')
            if nPos == -1:
               nPos = name.find('.m')
            if nPos >= 0:
               fileName.append(root + '/' + name)
    return fileName

def read_file(path):
    with open(path, 'r') as f:
         lines = f.readlines()
         f.close()
         return lines

def filter_key(lines):
    classmates = []
    index = 0
    for line in lines:
           nPos = line.find(key)
           if nPos == 0:
              classmates.append(line)
              index = index + 1
           elif (nPos == -1):
                if len(classmates) > 0:
                   break
    classmates = sorted(classmates,key=len)
    return classmates

def write_lines_sorted(path,lines,classmates):
    if len(classmates) == 0:
        return
    with open(path, 'w') as f:
         index = 0
         for line in lines:
             pos = line.find(key)
             if pos == 0:
                 if index != 0xfff:
                    f.write(classmates[index])
                    index = index + 1
                 else:
                     f.write(line)
             else:
                 if index!= 0:
                     index = 0xfff
                 f.write(line)
         f.close()

fileName = traversal_pwd()

for path in fileName:
    line = read_file(path)
    classmates = filter_key(line)
    write_lines_sorted(path,line,classmates)


