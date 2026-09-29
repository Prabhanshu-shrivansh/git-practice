def my_decorator(func):
    def wrapper(filename):
        with open(filename, "r") as file:
            data = file.read()
        if data.strip():          # file contains data
            return func(filename)
        else:
            print("File is empty")
            return None
    return wrapper

@my_decorator
def read_file(filename):

    with open(filename, "r") as file:
        return file.read()

data = read_file("data.txt")

if data:
    print(data)