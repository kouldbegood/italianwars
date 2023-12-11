a_modifier = 0
b_modifier = 0
a_tot = 0
b_tot = 0
a_mod = []
b_mod = []
a_res = []
b_res = []
a_atk = 0
b_atk = 0
a_dmg = 0
b_dmg = 0
a_battle = []
b_battle = []
day = 1
end = 0
def battle():
    global day
    global end
    global a
    global b
    global a_tot
    global b_tot
    for n in range(len(a)):
        a_tot += a[n]
    print("player A, before battle:%s %s" %(a_tot,a))
    a_tot = 0
    for n in range(b_dmg):
        if a[len(a)-1] > 0:
            a[len(a)-1] -= 1
        else:
            if a[0] == 0:
                break
            a.pop()
            a[len(a)-1] -= 1

    for n in range(len(a)):
        a_tot += a[n]
    print("Player A, after battle:%s %s" %(a_tot,a))
    if a[len(a)-1] == 0:
        if a[0] == 0:
            print("Player B fully annihilated Player A.")
            end += 1
        else:
            a.pop()
            print("Player A, after regroup:%s %s" %(a_tot,a))
    elif log(a[len(a)-1],2) == round(log(a[len(a)-1],2)):
        print("Player A, after regroup:%s %s" %(a_tot,a))
    else:
        while a[len(a)-1] > 0:
            a_res.append(2 ** (int(log(a[len(a)-1],2))))
            a[len(a)-1] -= 2 ** (int(log(a[len(a)-1],2)))
        a.pop()
        a += a_res
        print("Player A, after regroup:%s %s" %(a_tot,a))
    a_tot = 0

    for n in range(len(b)):
        b_tot += b[n]
    print("player B, before battle:%s %s" %(b_tot,b))
    b_tot = 0
    for n in range(a_dmg):
        if b[len(b)-1] > 0:
            b[len(b)-1] -= 1
        else:
            if b[0] == 0:
                break
            b.pop()
            b[len(b)-1] -= 1
    for n in range(len(b)):
        b_tot += b[n]
    print("player B, after battle:%s %s" %(b_tot,b))
    if b[len(b)-1] == 0:
        if b[0] == 0:
            print("Player A fully annihilated Player B.")
            end += 1
        else:
            b.pop()
            print("player B, after regroup:%s %s" %(b_tot,b))
    elif log(b[len(b)-1],2) == round(log(b[len(b)-1],2)):
        print("player B, after regroup:%s %s" %(b_tot,b))
    else:
        while b[len(b)-1] > 0:
            b_res.append(2 ** (int(log(b[len(b)-1],2))))
            b[len(b)-1] -= 2 ** (int(log(b[len(b)-1],2)))
        b.pop()
        b += b_res
        print("player B, after regroup:%s %s" %(b_tot,b))
    b_tot = 0
    day += 1

def win_condition_A():
    global end
    if a[0] >= 4 * b[0]:
        end += 1
        print("Player A wins without a fight, Player B's troops run away like dogs.")
    elif a[0] * 4 <= b[0]:
        end += 1
        print("Player A is no match for Player B, Player B dominated Player A.")
    elif a[0] == b[0] == 0:
        end += 1
        print("It is a tie.")
def army_modifier(i):
    return log(i,2)
def army_strenth():
    for n in range(len(a_battle)):
        global a_modifier
        a_atk = randint(1,6)
        a_mod.append("The %sth army of Player A with a number of %s rolled %s" %(n+1,a[n],a_atk))
        a_modifier += a_atk * a_battle[n]
    for n in range(len(b_battle)):
        global b_modifier
        b_atk = randint(1,6)
        b_mod.append("The %sth army of Player B with a number of %s rolled %s" %(n+1,b[n],b_atk))
        b_modifier += b_atk * b_battle[n]
    for n in range(len(a_mod)):
        print(a_mod[n])
    print(" ")
    for n in range(len(b_mod)):
        print(b_mod[n])
    print("Player A has %s battle points." %(a_modifier))
    print("Player B has %s battle points." %(b_modifier))
    global a_dmg
    global b_dmg
    if a_modifier > b_modifier:
        a_dmg = 2 + a_battle[0]
        b_dmg = b_battle[0]
        print("On the %sth day of the battle, Player A got advantage. Player B - %s, Player A - %s." %(day,a_dmg,b_dmg))
    elif a_modifier < b_modifier:
        b_dmg = 2 + b_battle[0]
        a_dmg = a_battle[0]
        print("On the %sth day of the battle, Player B got advantage. Player A - %s, Player B - %s." %(day,b_dmg,a_dmg))
    else:
        a_dmg = a_battle[0]
        b_dmg = b_battle[0]
        print("On the %sth day of the battle, Player A - %s, Player B - %s." %(day,b_dmg,a_dmg))

from math import log
from random import randint

#Input A and B then transform their logrithm values.
print("This is a tester for Italian Wars, Please Enter numbers that is 1, 2, 4, 8, or 16 and seperate them with space.")
print("Enter the army of player A:")
A = input()
a = list(map(int,A.split(" ")))
a.sort(reverse=True)
a_battle = list(map(int,list(map(army_modifier,a))))       
print("Enter the army of player B:")
B = input()
b = list(map(int,B.split(" ")))
b.sort(reverse=True)
b_battle = list(map(int,list(map(army_modifier,b))))



while end < 1:
    army_strenth()
    battle()
    a_battle = list(map(int,list(map(army_modifier,a))))
    b_battle = list(map(int,list(map(army_modifier,b))))
    win_condition_A()
    a_modifier = 0
    b_modifier = 0
    a_res = []
    b_res = []
    a_mod = []
    b_mod = []
    print("Press any key to continue.")
    f = input()

if end == 1:
    print("The battle is over.")
    f = input()
    










































