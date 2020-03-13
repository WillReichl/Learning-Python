#
# Read and write files using the built-in Python file methods
#


def main():
    # Open a file for writing and create it if it doesn't exist
    filepath = "output/textfile.txt"
    # f = open(filepath, "w+")

    # Open the file for appending text to the end
    f = open(filepath, "a")

    # write some lines of data to the file
    for i in range(10):
        f.write("This is line " + str(i) + "\r\n")

    # close the file when done
    f.close()

    # Open the file back up and read the contents
    f = open(filepath, "r")
    if f.mode == 'r':
        # contents = f.read()
        # print(contents)
        fl = f.readlines()
        for x in fl:
            print(x)


if __name__ == "__main__":
    main()
