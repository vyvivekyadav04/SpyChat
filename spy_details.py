#Importing DateTime Features
from datetime import datetime

#Class Spy
class Spy:
#Method __init__ for class Spy
    def __init__(self, name, salutation, age, rating):
		#Spy Details :-
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#Class ChatMessage
class ChatMessage:
#Method __init__ for class ChatMessage
    def __init__(self,message,sent_by_me):
		#Message Values:-
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('bond', 'Mr.', 24, 4.7) #Assigning  spy spy with default spy values  

#Values for friends list
friend_one = Spy('Raja', 'Mr.', 4.9, 27)
friend_two = Spy('Mata Hari', 'Ms.', 4.39, 21)
friend_three = Spy('No', 'Dr.', 4.95, 37)

#List of friends 
friends = [friend_one, friend_two, friend_three]



