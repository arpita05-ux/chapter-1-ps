import os

# Specify the directory you want to list (you can change this)
directory = "/12 jee"

# List all files and folders in the specified directory
contents = os.listdir(directory)

# Print the contents
print("Contents of directory:", directory)
for item in contents:
    print(item)
