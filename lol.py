import os

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(".VOB"):
            print("{}, {}".format(root, file))
