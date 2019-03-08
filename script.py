# Programmer:   Ahmed L Saeed
# Course:       CIS 298 - Intro to Python
# Instructor:   Robert Mann
# Program:      Project 04 - Files
# Due Date:     03/21/2019

def valid_char(i):
    if 'A' <= i <= 'Z':
        return True
    elif '0' <= i <= '9':
        return True
    else:
        return False

def display_output(dct):
    for k, v in sorted(dct.items()):
        print("{}: {}".format(k, v))

    # verify char req = 36
    # print(len(dct.keys()))

def main():
    file = open("myfile.txt", "r+")

    dct = {}

    for i in file.read():
        i = i.upper()
        if valid_char(i):
            dct[i] = dct.get(i, 0) + 1

    display_output(dct)



if __name__ == "__main__":
    main()
