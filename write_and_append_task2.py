#take user input and write to file

text=input("Enter text to write to the file :")

with open('output.txt','wt') as file:
    file.write(text + '\n')

print("data successfully written to output.txt. \n")

#additonal input append to same file

append_text=input("Enter additional text to append :")

with open('output.txt','at') as file:
    file.write(append_text +'\n')

print("data successfully written to output.txt. \n")

#read and display final output

print("final content of output.txt:\n")

with open('output.txt','rt') as file:
    print(file.read())

