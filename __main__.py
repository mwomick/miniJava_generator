from generator import makeProgram


def main():
    for i in range(0, 9):
        text_file = open("Test"+"{:03d}".format(i)+".mjava", "w")
        n = text_file.write(makeProgram())
        text_file.close()


if __name__ == "__main__":
    main()
