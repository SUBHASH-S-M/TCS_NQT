
"""

A game development company wants to design a brain game application for kids. 
There are different types of tasks to be designed for the game. 
Among all the tasks, there is one task in which each digit 
of an exisiting number has to be replaced with another digit. 
Consider the following table:

Existing Numbers: 0 1 2 3 4 5 6 7 8 9

Replace By: 9 8 7 6 5 4 3 2 1 0

Sample Input 1 : 105671

Sample Output 1 : 894328



"""
num=input()
if(int(num)>=0 and int(num) <=1000000):
    num=list(map(int,num))
    num=[9-i for i in num]
    num=list(map(str,num))
    print("".join(num))
else:
    print("Wrong Input")