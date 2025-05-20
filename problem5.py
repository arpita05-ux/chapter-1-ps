import os

# Select the directory you want 
directory = "/12 jee"

# use the os module to list the directory content
contents = os.listdir(directory)

# Print the contents
print("Contents of directory:", directory)
for item in contents:
    print(item)