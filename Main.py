import re
from datetime import datetime
import long_responses as long
import mysql.connector


# Data base connection

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345678",
    database = "mine"
)

cursor=mydb.cursor()


''' application should call this get_data() function and 
    should take the value from data base and put it in other function for the resut 
'''
           

# Selection of leave application option
# Its trigger Words (leave application)

def application():
    NAME,cl,pl,POST

    print("Bot: You chose the option for writing leave application :- ")
    get_Data()
    a=str(input("Enter the type of leave :- "))
    get_type(a,Emp_id)
    file_name = 'leave.txt'

    with open(file_name, 'w') as file:

        starting_date = int(input("Enter the date of leave starting :- "))
        starting_month = int(input("Enter the month of leave starting :- "))
        starting_Year = int(input("Enter the year of leave starting :- "))

        year1 = starting_Year

        if not valid_date(starting_date, starting_month, starting_Year):
            starting_Year = int(input("Enter the year of leave starting :- "))
            year1 = starting_Year

        ending_date = int(input("Enter the date of leave ending :- "))
        ending_month = int(input("Enter the month of leave ending :- "))
        ending_Year = int(input("Enter the year of leave ending :- "))
        year2 = ending_Year

        if not valid_date(starting_date, starting_month, ending_Year):
            ending_Year = int(input("Enter the year of leave ending :- "))
            year2 = ending_Year

        supervisor = input("Enter the name of your supervisor :- ")
        
        # Initialize the variable 'days' before using it

        dates(starting_date,starting_month,starting_Year,ending_date,ending_month,ending_Year)

        reason = input("Enter the reason:- ")

        file.write(f'Name :- {NAME}\nEmployee Id :- {Emp_id}\nPost :- {POST}\nRemaining Leave :- {cl}\nLeave From :-  {starting_date} / {starting_month} / {starting_Year} to {ending_date} / {ending_month} / {ending_Year}\n subject :- Leave application\n\n dear {supervisor} \n \n I hope this message finds you well. I am writing to formally request a leave of absence from work for {days} days.\n The purpose of my leave is {reason}\n\n Thank you')


   
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts the words present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # required worf or single
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0
    

def check_all_messages(message):
    highest_prob_list = {}

    # Simplification
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'to', 'code'], required_words=['love','code'])
    
    response('See you Brother', ['done'], single_response=True)
    response('Okay you want Leave application',['leave','application'],single_response=True)
    
    response('Chose option for raising ticket \n',['raise','ticket'],single_response=True)

    # Longer responses
    response(long.R_ADVICE, ['give', 'your','functions'], required_words=['give','your','functions'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Main AI LOGIC above ("DO NOT ALTER !!!!!!!!! except some responses") ----------------------------------------------------------------

Emp_id=0
cl=0
pl=0
NAME=None
Cl=0
Pl=0
POST=None
    
def get_Data():
    id=int(input("Enter the Emp_ID :- "))

    formula = f"SELECT * FROM OFFICE WHERE ID = {id}"
    cursor.execute(formula)

    ans=cursor.fetchall()
    global NAME,cl,pl,POST,Emp_id,Cl,Pl
    for name,CL,PL,emp,post ,in ans:
        NAME=name
        Cl=CL
        Pl=PL
        POST=post
        Emp_id=id

def get_data(Emp_id):


    formula = f"SELECT * FROM OFFICE WHERE ID = {Emp_id}"
    cursor.execute(formula)

    ans=cursor.fetchall()
    global NAME,cl,pl,POST,Cl,Pl
    for name,CL,PL,emp,post ,in ans:
        NAME=name
        Cl=CL
        Pl=PL
        POST=post


def get_type(a,Emp_id):
    get_data(Emp_id)
    global cl

    if(a.lower()=="cl"):
       cl=Cl
    else:
        cl=Pl
       
days=0 

def dates(starting_date, starting_month, starting_year, ending_date, ending_month, ending_year):
    # Convert input parameters to datetime objects
    global days
    start_date = datetime(starting_year, starting_month, starting_date)
    end_date = datetime(ending_year, ending_month, ending_date)

    # Calculate the difference in days
    days = (end_date - start_date).days + 1
 

def finish():
    exit() 


def init():
    print('Bot: Opening the file')
    file_name = 'Cl.txt'
    
    with open(file_name, 'w') as file:
        name = input('Bot: Enter your name: ')
        file.write(f'Hello {name}!\nHow are you?')   


# To add function for voice module 

# date checking is valid or not

def valid_date(date,month,year):
    
    date_data={1:31,2:29 if(year%4==0 and year%100!=0) or (year %400==0) else 28,
          3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    
    for key,value in date_data.items():
        if date<=value:
            return True
        else:
            print('Invalid date entered enter the valid date')
            return False
        

# Ticket generation

def Ticket():
    reason=input("Enter the reason of the ticket :- ")

    ticket=f"{reason} if the reason of the ticket"

    file_name='ticket.txt'
    with open(file_name,'w')as file:
        file.write(ticket)



# Testing the response system
while True:
    
    user_input = input('You: ')

    if user_input.lower() == 'open':
        init()
    elif (user_input.lower() == 'by') or (user_input.lower() == 'bye') or(user_input.lower() == 'done'):
        print('Bot: See you Soon')
        finish()
    elif (user_input.lower()=='leave application'):
        print('You chose option for application ' )
        application()    
    elif(user_input.lower()=='raise ticket'):
        Ticket()    
    else:
        print('Bot: ' + get_response(user_input))

