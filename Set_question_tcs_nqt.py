
"""

Given a list A of integer numbers that have values coming from SET=(0, 1, 2). 
The task is to put then the output should be 1 1 0 0 2 2
all ones first, then all Os, then 2s at last.

For example, List A[] = {0, 2, 1, 0, 1, 2}
Output : 1 1 0 0 2 2

Maximum size of list should be less than or equal to 100

Input : 1st value will be size of array n , next n line contain value from above set . 

Output : Output will contain all 1 first then 0 and then 2s.

Sample Input 1 : 
6
0
0
1
2
2
0
Sample Output 1 : 1 0 0 0 2 2



"""
n=int(input())
num=[int(input()) for i in range(n)]
if(len(num)<=100):
    C0=num.count(1)
    l0=[1]*C0
    
    num.sort()
    for i in num:
        if(i!=1):
            l0.append(i)
        
    l0=list(map(str,l0))
    print(" ".join(l0))
else:
    print("array size exceeded")
        
