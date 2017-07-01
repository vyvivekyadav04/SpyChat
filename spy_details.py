#Importing DateTime Features
from datetime import datetime

#Spy implimentation using Dictionary
#spy={
#    'name':'bond',
#    'salutation':'Mr.',
#    'age':24,
#    'rating':4.7,
#    'is_online':True
#}



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

#Default spy values
spy = Spy('bond', 'Mr.', 24, 4.7)

#Values for friends list
friend_one = Spy('SpyOne', 'Mr.', 27, 4.9)
friend_two = Spy('SpyTwo', 'Mr.', 21, 4.39)
friend_three = Spy('SpyThree', 'Dr.', 37, 4.95)

#List of friends 
friends = [friend_one, friend_two, friend_three]



