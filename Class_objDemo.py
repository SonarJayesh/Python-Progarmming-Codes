#Create a class Library with attributes like Acc-Number, Title, and Author. 
#Implement methods to compute fines and display book details.

class library:
    def __init__(self, acc_no, title, author,days):

        self.acc_no = acc_no
        self.title = title
        self.author = author
        self.days = days

    def fines(self):
        return self.days * 5 

    def display(self):
        print("Acc_No: ",self.acc_no)
        print("Title: ",self.title)
        print("author: ",self.author)
        print("Fines: ",self.fines())

acc = input("Enter the Account Number:")
title = input("Enter the title:")
author = input("Enter the Author Name: ")
days = int(input("Enter the late days: "))


b = library(acc, title, author, days)
b.display()
