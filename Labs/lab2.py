#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        #message = input("Enter your noun: ")
        #print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        #
        message=input("enter a string:")
        print("Entered:"+message)

        # print only first and last of the sentence:
        for i in range(len(message)):
            if i == 0:
                print(message[i], end="")
            if i ==len(message) -1:
                print(message[i], end="")
            if message[i]==" ":
                print(message[i-1],
                      message[i+1], end="")

        # use slice notation:
        print("\n" + message[:2])


        # escaping a character:
        print("This is called \"escaping\" a character")


        # find all a's in the input word and count how many there are:
        fnd="a"
        fnd2="A"
        count = message.count(fnd)
        count2 = message.count(fnd2)

        print("The count is:", count+count2)

        # replace all occurences of the character a with the - sign
        message = message.replace(' ', '-')
        print(message)

    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        my_list = (list(message.split(" ")))
        print(my_list)

        # append a new element to the list and print:
        my_list.append('Appended')
        print('updated with append', my_list)

        # remove from the list in 3 ways:
        #my_list.remove('hello')
        #print('updated with remove', my_list)


        # check if the word cake is in your input list:
        chk = "cake"

        for chk in my_list:
            if chk in my_list:
                print("cake is here")
                break
            else:
                print("cake is not here")
        # reverse the items in the list and print:


        # reverse the list with the slicing trick:
        print(my_list[::-1])

        # print the list 3 times by using multiplication:



tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()
