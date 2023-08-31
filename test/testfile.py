import os

def app():
    path = 'D:\\2 code\\Automation\data\\230816'

    files = os.listdir(path)
    s = []
    for file in files:
        if not os.path.isdir(file):
            s.append(file)
    # return s/

    print(s)
app()