import pandas as pd
import sys

def exit():
    sys.exit()

def start_up(name, age):
    bsIdea = str(input("Enter your buissness idea (brief) : \n" ))
        
    amount = int(input("Enter your investment amount : USD " ))
    
    if amount >= 10_000 :
        
        df = pd.read_csv("startup.csv")
        
        uID = len(df.index) + 1
        
        newdf = pd.DataFrame([{"UniqueID": uID,
                               "Name": name,
                               "Age": age,
                               "Bussness Idea":bsIdea,
                               "Investment Amount":amount}],
                             index=[uID - 1])
        
        df = pd.concat([df,newdf], axis=0)
        
        df.to_csv("startup.csv", index=False)
        
        print("\n \n\033[1;38;2;0;0;0;11;48;2;225;190;11m NOTE \033[1;38;2;0;0;0;11;48;2;255;0;110m Your Unique ID is " , uID,"\033[0m")
        
    else :
        print("You are NOT eligible for Startup")
        
    main_menu()
        
def student(name, age):
    df = pd.read_csv("student.csv")
        
    uID = len(df.index) + 1
    
    print(" \n \n\033[1;38;2;0;0;0;11;48;2;58;134;255m ╔════════════════════════╗ \n ║      Class 10 - 1      ║ \n ║      Class 12 - 2      ║ \n ║      Graduate - 3      ║ \n ╚════════════════════════╝ \033[0m")

    qualification = int(input("Enter your Qualification    : "))

    if qualification == 1 :
        m10 = int(input("Enter your 10th Marks       : "))
                
        if m10>=80 and m10<=100:
            print("\n You are eligible! \n Your data has been stored")
        
            newdf = pd.DataFrame([{"UniqueID": uID, "Name": name , "Age": age,"Marks 10":m10 }], index=[uID - 1])
                    
        elif m10>100:
            print("Check your input")
        
        else :
            print("\n You are NOT eligible!")
            
            main_menu()

    elif qualification == 2 :
        m10 = int(input("Enter your 10th Marks       : "))
        m12 = int(input("Enter your 12th Marks       : "))
    
        avg = (m10 + m12) / 2
        
        if avg >= 75 and avg<=100:
            print("\\n You are eligible! \n Your data has been stored")
            
            newdf = pd.DataFrame([{"UniqueID": uID, "Name": name , "Age": age,"Marks 10":m10, "Marks 12":m12}], index=[uID - 1])
        
        elif avg>100:
            print("\n Check your input") 
        
        else :
            print("\n You are NOT eligible!")
            main_menu()

    elif qualification == 3:  
        m10 = int(input("Enter your 10th Marks       : "))
        m12 = int(input("Enter your 12th Marks       : "))
        mg  = int(input("Enter your Bachelors Marks  : "))
        
        avg = (m10 + m12 + mg) / 3
            
        if avg >= 70 and avg<=100:
            print("\n You are eligible! \n Your data has been stored")
            
            newdf = pd.DataFrame([{"UniqueID": uID, "Name": name , "Age": age,"Marks 10":m10, "Marks 12":m12, "Marks Bachelors":mg}], index=[uID - 1])
            
        elif avg>100:
            print("Check your input") 
        
        else :
            print("\n You are NOT eligible!")
            main_menu()

    else:
        print("Wrong Input")
        
        student(name, age)
        
    
    df = pd.concat([df,newdf], axis=0)
    
    df.to_csv("student.csv", index=False)
    
    print("\n \n\033[1;38;2;0;0;0;11;48;2;225;190;11m NOTE \033[1;38;2;0;0;0;11;48;2;255;0;110m Your Unique ID is " , uID,"\033[0m")
    
    
    main_menu()

def reg():
    
    name = str(input("Enter your name : "))

    age = int(input("Enter your age : "))
    
    print("\033[1;38;2;0;0;0;11;48;2;225;190;11m ╔════════════════════════╗ \n ║     Start-up   - 1     ║ \n ║     Student    - 2     ║ \n ║     Return     - 3     ║ \n ╚════════════════════════╝ \033[0m")
    
    opt = int(input("Enter your option : "))
    
    if opt == 1:
        start_up(name, age)
        
    elif opt == 2:
        student(name, age)
        
    elif opt == 3:
        main_menu()
        
    else:
        print("\n Wrong input try again!")
        reg()
        
    main_menu()

def analyse():   
    print("\033[1;38;2;255;255;255;11;48;2;131;56;236m ╔════════════════════════╗ \n ║   Past Records of Stu  ║ \n ╚════════════════════════╝ \033[0m \n")
    
    df = pd.read_csv("pastrecords.csv")
        
    print("Number of different Countries applied are ", str(df.CountryOfApplication.nunique()), "\n")
    print("The countries applied are")
    for i in df.CountryOfApplication.unique():
        print(i, end="\n")
    print("\nAverage marks of applicants are ",round(df['AvgMarks'].mean(),2))
    
    print("\nAverage age of applicants are ",round(df['Age'].mean()),"\n")
    
    main_menu()

def main_menu():
    print("\033[1;38;2;0;0;0;11;48;2;251;86;7m ╔════════════════════════╗ \n ║     Register   - 1     ║ \n ║     Analyse    - 2     ║ \n ║     Exit       - 3     ║ \n ╚════════════════════════╝ \033[0m")
    option = int(input("Enter Your Option : "))
    
    if option == 1:
        reg()
        
    elif option == 2:
        analyse()
    
    elif option == 3:
        exit()
        
    else:
        print("\n Wrong input try again!")
        main_menu()
        
    
main_menu()

# \033[1;38;2;0;0;0;11;48;2;58;134;255m
# \033[1;38;2;0;0;0;11;48;2;251;86;7m
# \033[1;38;2;255;255;255;11;48;2;131;56;236m
# \033[1;38;2;255;255;255;11;48;2;58;134;255m
# \033[1;38;2;0;0;0;11;48;2;58;134;255m

# https://dsingh.vercel.app/ -Dilpreet Singh