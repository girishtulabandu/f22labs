from random import choice
from string import ascii_uppercase
n=''.join(choice(ascii_uppercase) for i in range(6))
f=list(n)
bull=0
count=0
while count<15:
    bull=0
    cock=0
    i=str(input('Enter a word in CAPS which contains only 6 characters'))
    l=list(i)
    while len(l)!=6:
        print("You have to enter only 6 characters word, Guess again")
        i=str(input())
        l=list(i)
    for h in range(6):
        for g in range(6):
            if(l[h]==f[g]):
                cock=cock+1
    for m in range(6):
        if(l[m]==f[m]):
            bull=bull+1
            cock=cock-1
    print("Number of characters that are correct,but in wrong place {}".format(cock))
    print("Number of characters that are correct and in correct place {}".format(bull))
    count+=1
    if(count<15):
        print("You have {} chances left".format(15-count))
    elif(count==15):
        print("you've crossed all the chances, the answer is {}".format(n))
    if(bull==6):
        print("yes you gussed it correct, the answer is {}".format(n))
        break
   
