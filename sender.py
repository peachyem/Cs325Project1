file = open('prompts.txt', 'r')
read = file.readlines()
modified = []

#need to remove the /n from the end of the prompts
for line in read:
    modified.append(line.strip())

print(modified)