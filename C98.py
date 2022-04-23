from fileinput import filename


def countwords():
    filename = input("enter file name:")
    count = 0
    fp = open(filename,'r')
    for line in fp:
        words = line.split()
        count = count+len(words)
    print("number of words")
    print(count)

countwords()