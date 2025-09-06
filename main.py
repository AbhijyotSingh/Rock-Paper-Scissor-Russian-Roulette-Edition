import random,sys,time
import mysql.connector as sql

def slow_type(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.0125)
    print("\n")
        
def register():
    cur.execute("SELECT name_user from data_rps")
    names=[i[0] for i in cur.fetchall()]
    name=input("Enter your name:")
    if name not in names:
        cur.execute("INSERT INTO data_rps(name_user,points,health,no_wins,no_losses) VALUES(%s,%s,%s,%s,%s)",(name,points,health,no_wins,no_loss))
        db.commit()
        m1="You are successfully registered. Enjoy the game!"
        slow_type(m1)
    else:
        m2="You are already registered. Try logging in."
        slow_type(m2)
        print("\n")
        login()
        
def login():
    m1="Welcome back! Please login."
    slow_type(m1)
    cur.execute("SELECT name_user from data_rps")
    names=[i[0] for i in cur.fetchall()]
    name=input("Enter your username:")
    if name in names:
        m2=f"Welcome back, {name}!"
        slow_type(m2)
    else:
        m3="User not found. Try registering."
        slow_type(m3)
        register()

def show_rules():
    message1="This game is exactly like normal rock, paper and scissor. The only twist comes where you lose. You are given 100 health points. Each time you win against the computer, you recieve 10 points and gain 5 health points. Each time you lose against it, you lose 5 points and your health decreases by 10. You can either play to your heart's content or stop at any given moment, you will be asked if you want to continue or not. Hope you enjoy this fun little game I made."
    slow_type(message1)

def rps_rr():
    data=view()
    m1="This is your saved file."
    slow_type(m1)
    id1=data[0]
    name=data[1]
    points=data[2]
    health=data[3]
    no_wins=data[4]
    no_loss=data[5]
    ans=input("Do you want to play the game (yes/no):")
    if health>0:
        while ans=="yes":
            choices=["rock","paper","scissor"]
            user_choice=input("Enter your choice (rock/paper/scissor):")
            comp_choice=random.choice(choices)
            print(f"The computer chose {comp_choice}.")
            if user_choice in choices:
                if user_choice=="rock" and comp_choice=="scissor":
                    m2="You gained 10 points!"
                    slow_type(m2)
                    no_wins+=1
                    points+=10
                    health+=5
                elif user_choice=="rock" and comp_choice=="paper":
                    m3="You lost 5 points."
                    slow_type(m3)
                    no_loss+=1
                    health-=10
                elif user_choice=="paper" and comp_choice=="rock":
                    m2="You gained 10 points!"
                    slow_type(m2)
                    no_wins+=1
                    points+=10
                    health+=5
                elif user_choice=="paper" and comp_choice=="scissor":
                    m3="You lost 5 points."
                    slow_type(m3)
                    no_loss+=1
                    health-=10
                elif user_choice=="scissor" and comp_choice=="paper":
                    m2="You gained 10 points!"
                    slow_type(m2)
                    no_wins+=1
                    points+=10
                    health+=5
                elif user_choice=="scissor" and comp_choice=="rock":
                    m3="You lost 5 points."
                    slow_type(m3)
                    no_loss+=1
                    health-=10
                else:
                    m4=f"You both chose {user_choice}. Tie"
                    slow_type(m4)
            else:
                m4="You didn't choose any of the following."
                slow_type(m4)
                cur.execute("UPDATE data_rps SET points=%s, health=%s, no_wins=%s, no_losses=%s WHERE name_user=%s",
                (points, health, no_wins, no_loss, name))
                db.commit()
                m6="Successfully added."
                slow_type(m6)
                break
            ans=input("Do you want to play the game (yes/no):")
        else:
            m5="Thank you for playing the game. Your scores will get added in the database."
            slow_type(m5)
            cur.execute("UPDATE data_rps SET points=%s, health=%s, no_wins=%s, no_losses=%s WHERE id=%s",
            (points, health, no_wins, no_loss,id1))
            db.commit()
            m6="Successfully added."
            slow_type(m6)
    else:
        m7="Your health is 0 now. Let's set it back to 100"
        slow_type(m7)
        health=100
        cur.execute("UPDATE data_rps SET points=%s, health=%s, no_wins=%s, no_losses=%s WHERE id=%s",(points, health, no_wins, no_loss,id1))
        db.commit()
        m6="Successfully added."
        slow_type(m6)        

def view_all():
    m1="(ID, Username,Points, Health, Wins, Losses)"
    slow_type(m1)
    cur.execute("SELECT * FROM data_rps")
    for i in cur:
        print(i)

def view():
    name=input("Enter your username:")
    cur.execute("SELECT name_user from data_rps")
    names=[i[0] for i in cur.fetchall()]
    if name in names:
        cur.execute("SELECT * FROM data_rps where name_user=%s",(name,))
        m1="(ID, Username,Points, Health, Wins, Losses)"
        slow_type(m1)
        for i in cur:
            print(i)
        return i
    else:
        m1="User not found. Try registering and playing the game."
        slow_type(m1)
        exit()
    
def game():
    m3="Press 1 to play the game."
    slow_type(m3)
    m4="Press 2 to view all stats."
    slow_type(m4)
    m5="Press 3 to view your stats."
    slow_type(m5)
    try:
        choice=int(input("Enter your choice:"))
    except ValueError:
        m5="Only integral values are allowed."
        slow_type(m5)
    else:
        if choice==1:
            rps_rr()
        elif choice==2:
            view_all()
        elif choice==3:
            view()
        else:
            m6="Only these options are available."
            slow_type(m6)
            return 

def main():
    m1="-----Welcome to Rock Paper Scissor-Russian Roulette Edition-----"
    slow_type(m1)
    m2="-----A game for children taken to the extreme.-----"
    slow_type(m2)
    
    ques=input("Do you want to see the rules of the games (yes/no):")
    if ques.lower()=="yes":
        show_rules()
    elif ques.lower()=="no":
        m3="Let's get back to the game. But first of all, try registering if you're a new user or try logging in if you're already a player."
        slow_type(m3)
    else:
        print("No other options available.")
        return
    
    ques1=input("Are you new here (yes/no):")
    if ques1.lower()=="yes":
        register()
    elif ques1.lower()=="no":
        login()
    else:
        print("No options are available.")
        return
    game()
    
if __name__=="__main__":
    pass1=input("Enter the password of your SQL database:")
    db=sql.connect(
        host="localhost",
        user="root",
        password=pass1
    )
    cur=db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS RPS_RR")
    cur.execute("USE RPS_RR")
    cur.execute("CREATE TABLE IF NOT EXISTS data_rps(id INT AUTO_INCREMENT PRIMARY KEY, name_user varchar(255),points int,health int, no_wins int, no_losses int)")
    print("Database and table have been successfully created.")
    print("\n")
    health=100
    points=0
    no_wins=0
    no_loss=0

    main()
