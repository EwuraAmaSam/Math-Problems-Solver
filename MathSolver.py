import random
def Rules():
    print("Welcome to another challenge with Ananse.")
    print("Here are the rules:")
    menu = eval(input("Type 0 to go back to the main menu: "))
    if menu == 0:
        main()
    else:
        pass

def ScoreBoard():
    pass

def levelOne():
    name = input("Now, enter your name to begin: ")
    earnable_points = 5
    points = []
    question = 0

    while question < 3:
        a = random.randint(0,9)
        b = random.randint(1,9)
        signlist = ['+','-','/','*']
        c = random.randint(0,3)
        if c == 0:
            ans = a + b
        elif c == 1:
            ans = a - b
        elif c == 2:
            ans = a//b
        else:
            ans = a*b
        print("What is ", a, signlist[c],b, "?")
        user_ans = eval(input("Answer here: "))
        count = 1
        while user_ans != ans and count != 3:
            count += 1
            earnable_points -= 1
            print("Please try again")
            print("What is ", a, signlist[c],b, "?")
            user_ans = eval(input("Answer here: "))
        if count == 0 or count < 3:
            points.append(earnable_points)
            print("Well done! You have earned,", earnable_points)
        else:
            points.append(1)
            print("The answer is ", ans)
        question +=1
    print("Congratulations! You have earned: ",sum(points), "points.")

              
# levelOne()        


def levelTwo():
    name = input("Now, enter your name to begin: ")
    earnable_points = 5
    points = []
    question = 0

    while question < 3:
        a = random.randint(0,99)
        b = random.randint(1,99)
        signlist = ['+','-','/','*']
        c = random.randint(0,3)
        if c == 0:
            ans = a + b
        elif c == 1:
            ans = a - b
        elif c == 2:
            ans = a//b
        else:
            ans = a*b
        print("What is ", a, signlist[c],b, "?")
        user_ans = eval(input("Answer here: "))
        count = 1
        while user_ans != ans and count != 3:
            count += 1
            earnable_points -= 1
            print("Please try again")
            print("What is ", a, signlist[c],b, "?")
            user_ans = eval(input("Answer here: "))
        if count == 0 or count < 3:
            points.append(earnable_points)
            print("Well done! You have earned,", earnable_points)
        else:
            points.append(1)
            print("The answer is ", ans)
        question +=1
    print("Congratulations! You have earned: ",sum(points), "points.")

    

# levelTwo()

def levelThree():
    name = input("Now, enter your name to begin: ")
    earnable_points = 5
    points = []
    question = 0

    while question < 3:
        a = random.randint(0,99)
        b = random.randint(1,99)
        d = random.randint(1,99)
        signlist = ['+','-']
        c = random.randint(0,1)
        e = random.randint(0,1)
        if c == 0 and e == 0:
            ans = a + b +d
        elif c ==  1 and e == 1:
            ans = a - b -d
        elif c == 0 and e == 1:
            ans = a+b-d
        else:
            ans = a-b+d
        print("What is ", a, signlist[c],b,signlist[e],d, "?")
        user_ans = eval(input("Answer here: "))
        count = 1
        while user_ans != ans and count != 3:
            count += 1
            earnable_points -= 1
            print("Please try again")
            print("What is ", a, signlist[c],b,signlist[e],d, "?")
            user_ans = eval(input("Answer here: "))
        if count == 0 or count < 3:
            points.append(earnable_points)
            print("Well done! You have earned,", earnable_points)
        else:
            points.append(1)
            print("The answer is ", ans)
        question +=1
    print("Congratulations! You have earned: ",sum(points), "points.")


# Function to begin the game
def Game():
    
    print("Please choose the level.")
    print("Type 1 for Beginner level")
    print("Type 2 for Intermediate level")
    print("Type 3 for Advanced level")
    level = eval(input("Level: "))
    if level == 1:
        levelOne()
    elif level == 2:
        levelTwo()
    elif level == 3:
        levelThree()
        
# Function to run the Home page
def Begin():
    print("Hey there. What do you want to do?")
    print("Type 1 to see the RULES.")
    print("Type 2 to see the SCORE BOARD.")
    print("Type 3 to BEGIN THE GAME.")
    ToDo = eval(input("Please type here: "))
    if ToDo == 1:
        Rules()
    elif ToDo == 2:
        ScoreBoard()
    elif ToDo == 3:
        Game()
    else:
        print("Please type correctly what you want to do")
        

    

def main():
    Begin()
main()
    