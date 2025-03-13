# open file and store file object in a variable 
file = open('page.txt', 'r')

# read the contents of file
print(file.read())

# close the file 
file.close()