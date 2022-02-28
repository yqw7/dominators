
repeat = (input(" How many AP classes do you want to take?"))
repeat = int(repeat)

def find_class(a1, a2):
    classes = ["Comp Sci Principles", "Chinese", "Psychology", "Human Geography", "Environmental Science", "Computer Science A", "US Comparative Government", "Microeconomics", "Macroeconomics", "US Gov & Politics", "Statistics", "Seminar", "Spanish Language", "English Language", "Art History", "Calculus AB", "Calculus BC", "Music Theory", "US History", "World History", "Biology", "European History", "Physics 2", "Physics 1", "Chemistry", "Physics C - Mechanics", "English Literature", "Physics C - E/M"]
    if a1 == ("science"):
        if a2 > 3:
            print("You should take" + " " + classes[22] + ",", classes[25] + ",", classes[27] + ",", classes[24])
        else:
            print("You should take" + " " + classes[4] + ",", classes[20] + ",", classes[23])
    if a1 == ("math"):
        if a2 > 3:
            print("You should take" + " " + classes[5] + ",", classes[8] + ",", classes[15] + ",", classes[16])
        else:
            print("You should take" + " " + classes[0] + ",", classes[10] + ",", classes[9])
    if a1 == ("english"):
        if a2 > 3:
            print("You should take" + " " + classes[26] + ",", classes[13])
        else:
            print("You should take" + " " + classes[11] + ",", classes[2])
    if a1 == ("foreign language"):
        if a2 > 3:
            print("You should take" + " " + classes[12] + ",", classes[17])
        else:
            print("You should take" + " " + classes[1] + ",", classes[2])
    if a1 == ("social studies"):
        if a2 > 3:
            print("You should take" + " " + classes[18] + ",", classes[21] + ",", classes[19])
        else:
            print("You should take" + " " + classes[3] + ",", classes[6] + ",", classes[9])
    if a1 == ("art"):
        if a2 > 3:
            print("You should take" + " " + classes[14] + ",", classes[21])
        else:
            print("You should take" + " " + classes[2] + ",", classes[3])

def classes_test():
    find_class("science", 4)
    find_class("math", 4)
    find_class("social studies", 2)

if __name__ == "__main__":
    classes_test()
    while (repeat > 0):
        find_class(input("What subject are you intrested in?"), int(input("On a scale of 1-5, how hard of an AP Class can you handle?")))
        repeat = repeat - 1
        if (repeat == 0):
            break
