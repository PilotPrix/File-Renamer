files = ["Copy of copy of document", "Copy of copy of document"]

userInput = input()

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
  files[i]


for i in ranges:
  i = i.split("-")

  startingNum = i[0]
  endingNum = i[1]

  for j in range(startingNum, endingNum):
    files[j]