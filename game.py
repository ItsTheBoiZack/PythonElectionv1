
def main():
    print("Welcome to Zackary's gov algo")
    print("--------------------")
    name = input ("What is your name: ")
    print ("Thats wonderful! It's great to meet you" + name)

    #Gathered Basic Name

    print("How old are you?")
    age = int(input("Age: "))
   

    #Ask for age

    if age < 18:
        print("You are too young to vote")
        Subtract = 18 - age
        print (Subtract)
        print("Until you can vote")
    else:
        print("Great! You are able to vote")

    #Age done


main()