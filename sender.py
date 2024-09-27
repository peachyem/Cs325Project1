#this file takes input from a file, communicates with phi3 through ollama and then puts the responses in a seperate file

import ollama

#open and read from prompt file
promptfile = open('prompts.txt', 'r')
read = promptfile.readlines()
#holds the modified lines
modified = []
#keeps track of modified send to the ai
count = 0

#open the response file
responsefile = open('responses.txt', 'w')

#need to remove the /n from the end of the prompts
for line in read:
    modified.append(line.strip())

#respond to all
for prompt in modified:
    responseO = ollama.generate(model="phi3:mini", prompt=modified[count])
    #specifically only get the response and put each one on a newline
    responseClean = responseO["response"] + '\n'
    #print(responseClean)
    #write to response file
    responsefile.write(responseClean)
    count +=1
#close the file
responsefile.close()
