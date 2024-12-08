def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

if __name__ == "__main__":
    read_file("row1.txt")
