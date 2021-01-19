import os
import sys

# Lists all files in directory like windows command `dir /s /b > output.txt` to a file.
# Usage: listFiles.py [directory] [output_file.txt]

if len(sys.argv) == 3:
    with open(str(sys.argv[2]), "w", encoding="utf-8", newline="\n") as outputFile:
        for root, folders, files in os.walk(os.path.join(sys.argv[1])):
            for file in files:
                outputFile.write(os.path.join(root, file) + "\n")
else:
    print("Incorrect number of parameters. ")
