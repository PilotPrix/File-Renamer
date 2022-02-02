import os
files = ["Copy of copy of document", "Copy of copy of document"]

folderSelection = input() + "/"
# impliment error safe mechanism
path, dirs, files = next(os.walk(folderSelection))
numberOfFiles = len(files)
print("There are", numberOfFiles, "in this folder")

userInput = input("Make your file selection: ")


for i in userInput:
  if i == " ":
    userInput = userInput.replace(" ", "")

userInput = userInput.split(",")

numbers = []
ranges = []


for i in userInput:
  numDashes = 0
  for j in i:
    if j == "-":
      numDashes += 1

  if numDashes == 0:
    numbers.append(int(i))
  elif numDashes == 1:
    ranges.append(i)
  else:
    print("Error, you suck")

for i in range(len(numbers)):
  rename = files[i] + " " + str(numbers[i])
  
  os.rename(folderSelection + files[i], folderSelection + rename)


for i in ranges:
  i = i.split("-")

  startingNum = int(i[0])
  endingNum = int(i[1])

  for j in range(startingNum, endingNum + 1):
    rename = files[j] + " " + str(j)
    os.rename(folderSelection + files[j], folderSelection + rename)


# Fail safe: ensure no overlaps (eg. "3, 1-7" "1-4, 3-6")
# Add renaming customization input