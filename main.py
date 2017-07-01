#Importing spy, Spy, ChatMessage, friends From spy_details
from spy_details import spy, Spy, ChatMessage, friends
#Importing Steganography Features
from steganography.steganography import Steganography
#Importing DateTime Features
from datetime import datetime
#STATUS_MESSAGES List (Containing Status Messages)
STATUS_MESSAGES = ["Can't think of a status" , "Just Another  status", 'Not so creative status']

#Just a print meassage
print "Hello! Let\'s get started"

#Whether to continue with default values
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question).upper()

#A Funcion to Add status message
def add_status():

#Initializing updated_status_message Variable
    updated_status_message = None

	#If current stat meassage is not None
	#Or we can say that if there IS any Status meassage.
    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:#If there is no Status Message
        print 'You don\'t have any status message currently \n'
	
	#To Choose whether to continue with the old status meassage or not.
    ques = raw_input("Do you want to continue with the old status.? y/n :")

    if ques.upper() == "N":  #Here Upper() is used to accept both N (Capital)  and n (Lower case) as a response
        new_status = raw_input("Enter your new status:")


        if len(new_status) > 0: #If the New Status Message is not Empty
            STATUS_MESSAGES.append(new_status)#Append the new status message to the STATUS_MESSAGES list
            updated_status_message = new_status#Updating the value of updated_status_message According to the Users Choice

    elif ques.upper() == 'Y': #Here Upper() is used to accept both Y (Capital)  and y (Lower case) as a response

        item_position = 1

        for message in STATUS_MESSAGES: #Recurcively Getting every status message
            print '%d. %s' % (item_position, message) #Displaying Status Messages with Item Positions
            item_position = item_position + 1  #Incremeting the variable item_position

        message_selection = int(raw_input("\nChoose from the above messages ")) #Getting Users Choice


        if len(STATUS_MESSAGES) >= message_selection: #If User Input is Not Out Of Range
            updated_status_message = STATUS_MESSAGES[message_selection - 1] #Updating the desired status message

    else:#If User Enter Somthing Else than Y/N (or y/n)
        print 'The option you chose is not valid! Press either y or n.' #

    if updated_status_message:#If updated_status_message is not None
        print 'Your updated status message is: %s' % (updated_status_message)
    else:#If updated_status_message is None
        print 'You current don\'t have a status update'
     #Returning The value of updated_status_message
    return updated_status_message

#A Funcion to add a friend 
def add_friend():
#Initializing The Variable new_friend
    new_friend = Spy('','',0,0.0)
#Getting Name Of the Friend
    new_friend.name = raw_input("Please add your friend's name: ")
	#Getting Salutation Of the Friend
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
	#Concatinating Salutation And Name
    new_friend.name = new_friend.salutation + " " + new_friend.name
	#Getting Age
    new_friend.age = raw_input("Age?")
	#Converting Age To Integer
    new_friend.age = int(new_friend.age)
	#Getting Rating
    new_friend.rating = raw_input("Spy rating?")
	#Converting Rating To FloatingPoint
    new_friend.rating = float(new_friend.rating)
	#If Friend's Name is Not Empty ,Age is above 12 and friend's rating is above or equals to spy's rating 
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.age < 50: #new_friend.rating >= spy.rating:
        friends.append(new_friend)#Add Friend to The Friends List
        print 'Friend Added!'
    else:#If The Required Conditions are not Met
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends) #Return The Length of the friends list 

#A Funcion To Select a friend 
def select_a_friend():
    item_number = 0
#Recurcively accessing every friend from the list friends
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1
#Return The Value of friend_choice_position
    return friend_choice_position

#A Function To Send Message to the friend
def send_message():
#Choose a friend to send a message to
    friend_choice = select_a_friend()
#Name Of the Image Used For Stegnography
    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"#OutPut Image Path and Name 
    text = raw_input("What do you want to say? ")#Message to be hidden in the image
    Steganography.encode(original_image, output_path, text)#Steganography Funcion Call to get output image
#Assigning the variable new_chat
    new_chat = ChatMessage(text,True)
#Append the Value of new_chat to the chosen friend's chat List
    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


#A Function to read the message
def read_message():
#Whose Message do we wants to read
    sender = select_a_friend()
#Get Name of the file
    output_path = raw_input("What is the name of the file?")
#Run Steganography function to decode the file and get the hidden message
    secret_text = Steganography.decode(output_path)
#Getting the secret_text and assignig it to new_chat
    new_chat = ChatMessage(secret_text,False)
#Append The Value of new_chat to the friends list
    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"

#Funtion to Read Chat Historey 
def read_chat_history():
#Select  a friend to read historey
    read_for = select_a_friend()

    print '\n6'
#Recurcively fetching all values from the list chat of the chosen friend
    for chat in friends[read_for].chats:
        if chat.sent_by_me:  #If chat is with you
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else: #If chat is with some one else
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

#Function  to Start The Chat 
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

#If spy is of appropriate age
    if spy.age > 12 and spy.age < 50:

#Showing final authentication message
        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"
#Show Menu or Not
        show_menu = True
#Loop To Show Menu
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)#Converting menu_choice to integer 

                if menu_choice == 1:#Status Message
                    spy.current_status_message = add_status()
                elif menu_choice == 2:#Add A Friend
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:#Send Message to a friend
                    send_message()
                elif menu_choice == 4:#To Read Message sent by a friend
                    read_message()
                elif menu_choice == 5:#To Read Chat Historey
                    read_chat_history()
                else:
                    show_menu = False
    else:#If spy is not of correct age
        print 'Sorry you are not of the correct age to be a spy'

if existing == "Y": #If Value of existing is Y
    start_chat(spy)  #Start The start_chat function 
elif existing== "N": #Getting Spy Details if 

    spy = Spy('','',0,0.0)

# Welcome Message
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0 and spy.name!=" ":#If spy's name is not empty
	#Get spy Salutation
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")
	#Get spy Age
        spy.age = raw_input("What is your age?")
	#Converting Spy's age to int
        spy.age = int(spy.age)
	#Getting spy rating
        spy.rating = raw_input("What is your spy rating?")
	#Converting Spy rating to float
        spy.rating = float(spy.rating)
	#Start Chat 
        start_chat(spy)
    else:
        #Invalid Name
        print "Please add a valid spy name"


else:
    print "Invalid Choice..!"