from colors import Colors
target = "walls"
guess = "lsals" 
newString = ""
skiplist = []
firstnames = ["john", "paul"]
lastnames = ["lennon", "mccartney"]
#identify correct characters and store their index
for i in range(len(target)):
        if guess[i] == target[i]:
            skiplist.append(i)
            #found a matching character replaces with '-' so it isnt used twice 
            target = target[:i] + '-' + target[i+1:]

for idx, letter in enumerate(guess):
    #if previously identified as correct color the character green puts it in newstring and move to next  character
    if idx in skiplist:
        newString += f"{Colors.GREEN}{letter}{Colors.RESET}"
        continue
    #at this point any remaining characters are incorrect or wrong location
    if letter in target:
        target = target.replace(letter, "-", 1)
        newString += f"{Colors.YELLOW}{letter}{Colors.RESET}"
    else:
        newString += f"{letter}"
    print(target)
print(newString)