import re
import long_responses as long

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
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    
    response('See you Brother', ['done'], single_response=True)
    response('Okay you want Leave application',['leave','application'],single_response=True)

    # Longer responses
    response(long.R_ADVICE, ['give', 'your','functions'], required_words=['give','your','functions'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response



# Main AI LOGIC above ("DO NOT ALTER !!!!!!!!! except some responses") ----------------------------------------------------------------

def finish():
    exit() 


def init():
    print('Bot: Opening the file')
    file_name = 'Cl.txt'
    
    with open(file_name, 'w') as file:
        name = input('Bot: Enter your name: ')
        file.write(f'Hello {name}!\nHow are you?')    




# Selection of leave application option
# Its trigger Words (leave or application)

def application():
    print("Bot: You chose the option for writing leave application :- ")
    a=input("write the type of application you want ")
    file_name='leave.txt'

    with open(file_name,'w')as file:

        name = input("Enter your name - ")
        ID = int(input("Enter your ID - "))

        if(ID>0 and ID<=10):
            post = 'Senior'
        elif(ID>11 and ID<=20):
            post='Junior'
        else:
            post = 'New'      

        if(post =='New'):
            CL=2
        elif(post=='Junior'):
            CL= 4
        else:   
            CL=10          

        starting_date=int(input("Enter the date of leave starting - "))
        starting_month=str(input("Enter the month of leave starting - "))

        ending_date=int(input("Enter the date of leave ending - "))
        ending_month=str(input("Enter the month of leave ending - "))

        supervisor=str(input("Enter the name of your supervisor "))

        reason=str(input("Enter the reason:- "))

        file.write(f'{name}\n{ID}\n{post}\n{CL}\n{starting_date} {starting_month} to {ending_date} {ending_month} \n subject :- Leave application\n\n dear {supervisor} \n \n I hope this message finds you well. I am writing to formally request a leave of absence from work for {CL} days.\n The purpose of my leave is {reason}\n\n Thank you')  



# Testing the response system
while True:
    user_input = input('You: ')
    if user_input.lower() == 'open':
        init()
    elif user_input.lower() == 'by':
        print('Bot: See you Soon')
        finish()
    elif user_input.lower()==  'leave' or 'application' :
        application()

    else:
        print('Bot: ' + get_response(user_input))
