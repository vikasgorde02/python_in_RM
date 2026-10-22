import os
def get_time(vikasDSA ):
    return os.path.getatime(vikasDSA)
files=os.listdir('.')
files.sort(key=get_time)
for file in files:
    print(file)