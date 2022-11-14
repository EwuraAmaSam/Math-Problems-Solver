import random
def Rules():
    print("Welcome to another challenge with Ananse.")
    print("Here are the rules:")

def ScoreBoard():
    pass

def levelOne():
    name = input("Now, enter your name to begin: ")
    earnable_points = 5
    points = []
    a = random.randint(0,9)
    b = random.randint(0,9)
    signlist = ['+','-','/','*']
    c = random.randint(0,3)
    if c == 0:
        ans = a + b
    elif c == 1:
        ans = a - b
    elif c == 2:
        ans = a/b
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
    else:
        points.append(1)
        print("The answer is ", ans)
    # print(points)
  



    # print("What is ", a, "+ ",b, "?")
    # user_ans1 = eval(input("Answer here: "))
    # if user_ans1 == ans:
    #     print("Correct for 5 points")
    #     points.append(5)
    # elif user_ans1 != ans:
    #     print("Please try again")
    #     print("What is ", a, "+ ",b, "?")
    #     user_ans2 = eval(input("Answer here: "))
        
    #     if user_ans2 == ans:
    #         print("Good! You have earned 3 points")
    #         points.append(3)
    #     elif user_ans2 != ans:
    #         print("Please try again")
    #         print("What is ", a, "+ ",b, "?")
    #         user_ans3 = eval(input("Answer here: "))
    #         if user_ans3 == ans:
    #             print("You did it. You have earned 2 points")
    #             points.append(2)
    #         elif user_ans3 != ans:
    #             print("Oops. That is wrong but you earn 1 point for trying")
            
            
              
levelOne()        


def levelTwo():
    pass

def levelThree():
    pass

# Function to begin the game
def Game():
    
    print("Please choose the level.")
    print("Type 1 for Beginner level")
    print("Type 2 for Intermediate level")
    print("Type 2 for Advanced level")
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
        

    

# def main():
#     Begin()
# main()
    