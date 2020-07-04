import os
import sys

# Lists all files in directory like windows `dir /s /b > output.txt` command and outputs to text file
# Usage: listFiles.py [directory] [output_file.txt]

outputFile = open(str(sys.argv[2]), "w", newline='\n')

sourceDirectory = os.path.join(sys.argv[1])

for root, dirs, files in os.walk(sourceDirectory):
    for file in files:
        outputFile.write(os.path.join(root, file) + "\n")

outputFile.close()
