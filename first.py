# from datetime import date 
# name = input("What is your name?")
# year = input("what year were you born?")
# print ("hello " + name + " nice to meet you")
# print ("hello world")
# firstName = int(input("what is your firstname?"))
# lastName = int(input("what is your lastname?"))
# print ("hello " + firstName + lastName)
# year_str = int(input("what year were  you born?")) 

# current_year = int(input("what is currentyear?"))

# age = current_year - year_str

# age = int(date.today().year) - year_str
# print ("Hello " + (str(firstName))  + (str(lastName))  + "You are " + (str(age)) + " years old")
# import random
# b = random.randradef interest(principal, rate, time):
    
#     rest = principal * rate * time 
    
#     return rest / 100 

# print(interest(4,5,2))nge(1, 10)
# attempts = 5
# while attempts > 0:
#     guess = int(input("Make a guess: "))
#     if guess < b:
#       print("Too Low")
#     elif guess > b:
#       print("Too High")
#     else:
#       print("hurray you guess right")
#       break
#     attempts -= 1
#     if attempts > 1:
#         print(f" you have {attempts} {'attempts' if attempts > 1 else 'attempt'} left")
#     else:
#             print(f"sorry, you've used all your attempts. The number was {b}")
# import random
# b = random.randrange(1, 10)
# guess = int(input("Make a guess: "))
# while
# def test():
#     food =["eba", "amala", "indomie", "eggs"]
#     for i in food[0:4:2]:
#         print(i)
# test()
# def test():
#     global food
#     food =["eba", "amala", "indomie", "eggs"]
#     for i in range(len(food)):
#         print(i,food[0:4:2])
# test()
# print(food)
# def area(length, breadth):
#     return length * breadth
# print(area(4,5))
# def interest(principal, rate, time):
    
#     rest = principal * rate * time 
    
#     return rest / 100 

# print(interest(4,5,2))
# def interest(principal:int, rate:int, time:int, b = 100):

#     if rate >= 100:
#         print("your rate must be interger:")
#     rest = (principal * rate * time) / b
#     return rest
# print(interest(2,3,5))
# movies =[
# {
# "title":"bob", "genres":"comedy",
# "title":"rich", "genres":"Drama",
# "title":"alternate", "genres":"Action",
# "title":""
# }
# ]
# def count_movies_by_genres():

#     for genres in movies:
# class Animal:
#     def_init_(self, name, specie):
#     self.name = name
#     self.specie = specie
#     def speak(self):
#     pass
# class Dog(Animal):
#     def_init_(self, name, breed):
#     super()._init_(name,)
# class Dog: 
#      __number = 0
#      def __init__(self, name):
#          self.name = name
#          Dog.__number += 1
#          self.dognumber = Dog.__number
        

#      def bark(self):
#          print(f"{self.name} says woof!")

# jack = Dog ("jack")
# print(f"{jack.dognumber}")
class Dog: 
     number = 0
     def __init__(self, name):
         self.name = name
         Dog.__number += 1
         self.__dognumber = Dog.number
         
     @property
     def dognumber(self):
          return self.__dognumber
        

     def bark(self):
         print(f"{self.name} says woof!")

jack = Dog ("jack")
print(f"{jack.dognumber}")



