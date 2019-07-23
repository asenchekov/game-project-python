# file = open("filename.extension", "editingType")
# w mode writes and overwrites file
out = open("firstOutput.txt", "w")

out.write("Test")

out.close()

# a mode appending to file
out = open("firstOutput.txt", "a")

out.write("Test")

#always close the files after finishing to write
out.close()

# opens and closes the file automaticaly code inside it writes to file
with open("firstOutput.txt", "a") as out:
  out.write("\n")
  out.write("end of file")

inputFile = open("firstOutput.txt", "r")

fileContent = inputFile.read()

print(fileContent)
