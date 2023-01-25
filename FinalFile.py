# Final file
# Iterate over the three .txt files (you can get those files on our Teams group)
# using the read function to get a final file with the content of those three files.

# Expected: You can not write manually the name of the three files.
# Get a .txt as a output of this program with the content of all the files.

file_names = ["file1.txt", "file2.txt", "file3.txt"]
with open("new_file.txt", "w") as new_file:
    for name in file_names:
        with open(name) as f:
            for line in f:
                new_file.write(line)
            new_file.write("\n") 