def write_file(file_name, file_content):
    pass
    with open(f"{file_name}.txt", "w") as t:
        t.write(file_content)

def append_file(file_name, append_content):
    pass
    with open(f"{file_name}.txt", "a") as t:
        t.write(append_content)

def read_file(file_name):
    pass
    with open(f"{file_name}.txt") as t:
        return t.read()


# use write_file function. 
write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )

read_file(file_name="logfile")
print(read_file(file_name="logfile"))

# use append_file function.
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")
print(read_file(file_name="logfile"))
