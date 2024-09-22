import ollama

file = open('prompts.txt', 'r')
read = file.readlines()
modified = []
count = 0

#need to remove the /n from the end of the prompts
for line in read:
    modified.append(line.strip())

#respond to all
for prompt in modified:
   words = modified
   response = ollama.generate(model="phi3", prompt=modified[count])
   print(response)
   count +=1

