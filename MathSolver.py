import random
# import time

leaderboard_1={}
leaderboard_2={}
leaderboard_3={} 



def saveleaderboard1():
    with open('leaderboard1_Ananse.txt','w') as file:
            file.writelines('------leaderboard_1------------- \n')
            file.writelines('   Name      | Score  \n')
            for j in leaderboard_1:
                spaces_count=15-len(j)
                spaces=' '*spaces_count
                file.writelines('{}{}|    {}\n'.format(j,spaces,leaderboard_1[j]))
          

def saveleaderboard2():
    with open('leaderboard2_Ananse.txt','w') as file:
            file.writelines('------leaderboard_2------------- \n')
            file.writelines('   Name      | Score  \n')
            for j in leaderboard_2:
                spaces_count=15-len(j)
                spaces=' '*spaces_count
                file.writelines('{}{}|    {}\n'.format(j,spaces,leaderboard_2[j]))
        

def saveleaderboard3():
    with open('leaderboard3_Ananse.txt','w') as file:
            file.writelines('------leaderboard_3------------- \n')
            file.writelines('   Name      | Score  \n')
            for j in leaderboard_3:
                spaces_count=15-len(j)
                spaces=' '*spaces_count
                file.writelines('{}{}|    {}\n'.format(j,spaces,leaderboard_3[j]))
         
            print('Leaderboards Ready!')

try:
    f=open('leaderboard1_Ananse.txt')
    print('Y')
    f.close()
except IOError:
    saveleaderboard1()

    saveleaderboard2()

    saveleaderboard3()


def Rules():
    # a = "Welcome to another game with Ananse"
    print(f"{'Welcome to another game with Ananse 😁':>70}")
    print(f"{'Are you ready? 😎':>70}")
    print(f"{'Let us check out the rules rules 📃':>70}")
    print(" ")
    print(f"{'BEGINNER LEVEL RULES':>30}")
    print(" ")
    print(f"{'👩‍🏫At this stage, you will be working with just one math operator.':>50}")
    print(" ")
    print(f"{'👩‍🏫It could be addition, subtraction, division, or multiplication.':>50}")
    print(" ")
    print(f"{'👩‍🏫Do you know the good part to this level?? There is no time limit😉':>50}")
    print(" ")

    print(f"{'INTERMEDIATE LEVEL RULES':>30}")
    print(" ")
    print(f"{'👩‍🏫At this level, we are going to try bigger numbers with only one operator':>50}")
    print(" ")
    print(f"{'👩‍🏫You also have 3 minutes to solve each problem.':>50}")
    print(" ")
   

    print(f"{'ADVANCED LEVEL RULES':>30}")
    print(" ")
    print(f"{'👩‍🏫This is the part where it gets challenging but interesting.':>50}")
    print(" ")
    print(f"{'👩‍🏫At this level, you get to work with two math operators (+,-) and higher numbers.':>50}")
    print(" ")
    print(f"{'👩‍🏫You have 5 minutes to answer each question':>50}")
    print(" ")


    print(f"{'RULES FOR THE SCORES':>60}")
    print(" ")
    print(f"{'If you get it correct on the first attempt, you earn 5 points ✔🎊':>50}")
    print(" ")
    print(f"{'If you get it correct on the second attempt, you earn 4 points ✔🥂':>50}")
    print(" ")
    print(f"{'If you get it correct on the third attempt, you earn 5 points ✔👏':>50}")
    print(" ")
    print(f"{'If you do not get it after the three attempts, you get 1 point 😉':>50}")
    print(" ")

    menu = eval(input(f"{'TYPE 0 TO GO BACK TO THE MAIN MENU: ' :>70}"))
    if menu == 0:
        main()
    else:
        pass

def Savetoleaderboard(filename,name,points):
    with open(filename,'a') as file:
        spaces_count=15-len(name)
        spaces=' '*spaces_count
        file.writelines('{}{}|    {}\n'.format(name,spaces,sum(points)))

def ScoreBoard():
    pass


def levelOne():
    name = input(f"{'Welcome 🥳! Enter your name to begin:':^50}")
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
        user_ans = eval(input(f"{'Answer here: ':^50}"))
        count = 1
        while user_ans != ans and count != 3:
            count += 1
            earnable_points -= 1
            print("Please try again 😊")
            print("What is ", a, signlist[c],b, "?")
            user_ans = eval(input(f"{'Answer here: ':^50}"))
        if count == 0 or count < 3:
            points.append(earnable_points)
            print("Well done! You have earned", earnable_points, "points 😎")
        else:
            points.append(1)
            print("The answer is ", ans, "and you earn 1 point for trying 👏.")
        question +=1
    print("Congratulations! You have earned: ",sum(points), "points.")
    leaderboard_1[name]=sum(points)
    Savetoleaderboard('leaderboard1_Ananse.txt',name,points)
    # writeleaderboard()


              
# levelOne()        


def levelTwo():
    name = input(f"{'Welcome 🥳! Enter your name to begin:':^50}")
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
        user_ans = eval(input(f"{'Answer here: ':^50}"))
        count = 1
        t = 10
        while user_ans != ans and count !=3:
            count += 1
            earnable_points -= 1
            print("Please try again 😊")
            print("What is ", a, signlist[c],b, "?")
            user_ans = eval(input(f"{'Answer here: ':^50}"))
        if count == 0 or count < 3:
            points.append(earnable_points)
            print("Well done! You have earned", earnable_points, "points 🥂")
        else:
            points.append(1)
            print("The answer is ", ans)
            print("Better luck next time 👌.")
            print(" ")
           
        question +=1
    print("Congratulations! You have earned: ",sum(points), "points ❤.")
    leaderboard_2[name]=sum(points)
    Savetoleaderboard('leaderboard2_Ananse.txt',name,points)
    # writeleaderboard()
  

    

# levelTwo()

def levelThree():
    name = input(f"{'Welcome 🥳! Enter your name to begin:':^50}")
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
        user_ans = eval(input(f"{'Answer here: ':^50}"))
        count = 1
        while user_ans != ans and count != 3:
            count += 1
            earnable_points -= 1
            print("Please try again")
            print("What is ", a, signlist[c],b,signlist[e],d, "?")
            user_ans = eval(input(f"{'Answer here: ':^50}"))
        if count == 0 or count < 3:
            points.append(earnable_points)
            print("Well done! You have earned ", earnable_points, "points 🎊.")
        else:
            points.append(1)
            print("The answer is ", ans, " you have one point for trying 👌.")
        question +=1
    print("Congratulations! You have earned: ",sum(points), "points.")
    leaderboard_3[name]=sum(points)
    Savetoleaderboard('leaderboard3_Ananse.txt',name,points)
    # writeleaderboard()
   



def writeleaderboard():
    with open('leaderboard1_Ananse.txt','r') as file:
        content=file.readlines()
        for i in content:
            i.split('|')
        for i in content :
            print(i)
    with open('leaderboard2_Ananse.txt','r') as file:
        content=file.readlines()
        for i in content:
            i.split('|')
        for i in content :
            print(i)
    with open('leaderboard3_Ananse.txt','r') as file:
        content=file.readlines()
        for i in content:
            i.split('|')
        for i in content :
            print(i)
    print(" ")
    print(f"{'You and your friends are doing amazing! Math is fun right?':^50}")
    print(f"{'Now, what do you want to do next?':^50}")
    print(f"{'Type 0 to go back to the main menu.':^50}")
    print(f"{'Type 1 to play a game.':^50}")
    print(f"{'Type any other key to exit.':^50}")
    doNext = eval(input("Type here: "))
    if doNext == 0:
        Begin()
    elif doNext == 1:
        Game()
    else:
        print("Goodbye")



           



# Function to begin the game
def Game():
    
    print(f"{'Please choose the level.':^90}")
    print(" ")
    print(f"{'Type 1 for BEGINNER level 👶.':^90}")
    print(f"{'Type 2 for INTERMEDIATE level 🏃‍♂️.':^90}")
    print(f"{'Type 3 for ADVANCED level. 🏃‍♀️💨':^90}")
    print(" ")
   
    level = eval(input(f"{'Level: ':^50}"))
    if level == 1:
        levelOne()
    elif level == 2:
        levelTwo()
    elif level == 3:
        levelThree()
    else:
        print("Please type properly what you want to do")
        Game()
        
# Function to run the Home page
def Begin():
    print(f"{'Hey there. What do you want to do?':^90}")
    print(f"{'Type 1 to see the RULES.':^90}")
    print(f"{'Type 2 to see the SCORE BOARD.':^90}")
    print(f"{'Type 3 to BEGIN THE GAME.':^90}")

    ToDo = eval(input("Please type here: "))
    if ToDo == 1:
        Rules()
    elif ToDo == 2:
        # saveleaderboard()l
        writeleaderboard()
    elif ToDo == 3:
        Game()
    else:
        print("Please type correctly what you want to do")
        Begin()
        

def main():
    Begin()

main()
    