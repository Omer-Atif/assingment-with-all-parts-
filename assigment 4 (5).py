file1 = input("Enter the path to the file: ")

with open(file1, 'r') as file:
    lines = file.readlines()

print("Content of the file stored in a list:")
for line in lines:
    print(line.strip()) 
