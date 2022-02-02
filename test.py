import os

path, dirs, files = next(os.walk("Screenshots"))
print(len(files))