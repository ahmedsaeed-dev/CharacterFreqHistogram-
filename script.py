# Programmer:   Ahmed L Saeed
# Course:       CIS 298 - Intro to Python
# Instructor:   Robert Mann
# Program:      Project 04 - Files
# Due Date:     04/18/2019

import matplotlib.pyplot as plt


def plotter(dct):

    chars = list(dct.keys())
    count = list(dct.values())

    plt.bar(range(len(dct)), count, tick_label=chars)
    plt.title("Character Frequency - Project 04", weight='bold')
    plt.xlabel('Characters', weight='bold')
    plt.ylabel('Count', weight='bold')
    plt.savefig('bar.png')
    plt.show()


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

    for char in file.read():
        char = char.upper()
        if valid_char(char):
            dct[char] = dct.get(char, 0) + 1

    # display_output(dct)
    plotter(dct)


if __name__ == "__main__":
    main()
