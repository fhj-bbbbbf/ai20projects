def error():
    print('Please input number 1~9!')


print('''
Let's play a game with me!
Score the following statements with number 1~9.
Remember!
The bigger the number is, the more you agree on the statement.
And if you are not sure, please input "5".
''')

print("Are you ready?")
answer0=input()
while answer0!='yes':
    print('Prepare yourself and say yes when you are ready!')
    answer0=input()

print('''
1. Our country desperately needs a mighty leader who will do what has to be done
to destroy the radicalnew ways and sinfulness that are ruining us.
''')

answer1=input()
def jiancha():
    global answer1
    while answer1!=str(1) and answer1!=str(2) and  answer1!=str(3) and answer1!=str(4) and answer1!=str(5) and answer1!=str(6) and answer1!=str(7) and answer1!=str(8) and answer1!=str(9):
        error()
        answer1=input()
jiancha()
    
count=0
def scorezheng():
    global count
    if int(answer1)==1:
        count+=-4
    if int(answer1)==2:
        count+=-3
    if int(answer1)==3:
        count+=-2
    if int(answer1)==4:
        count+=-1
    if int(answer1)==6:
        count+=1
    if int(answer1)==7:
        count+=2
    if int(answer1)==8:
        count+=3
    if int(answer1)==9:
        count+=4
scorezheng()

print('''
2. Gays and lesbians are just as healthy and moral as anybody else.
''')

answer1=input()

jiancha()

def scorefan():
    global count
    if int(answer1)==1:
        count+=4
    if int(answer1)==2:
        count+=3
    if int(answer1)==3:
        count+=2
    if int(answer1)==4:
        count+=1
    if int(answer1)==6:
        count+=-1
    if int(answer1)==7:
        count+=-2
    if int(answer1)==8:
        count+=-3
    if int(answer1)==9:
        count+=-4

scorefan()

print('''
3. It is always better to trust the judgment of the proper authorities
in government than to listen to the noisy rabble-rousers in our society
who are trying to create doubt in people’s minds.
''')
answer1=input()

jiancha()

scorezheng()

print('''
4.The only way our country can get through the crisis ahead is to get back to
our traditional values, put some tough leaders in power, and silence the
troublemakers spreading bad ideas.
''')
answer1=input()

jiancha()

scorezheng()

print('''
5. Our country needs free thinkers who have the courage to defy traditional ways,
even if this upsets many people.
''')
answer1=input()

jiancha()

scorefan()

print('''
6. Our country will be destroyed someday if we do not smash the perversions
eating away at our moral fiber and traditional beliefs.
''')
answer1=input()

jiancha()

scorezheng()

print('''
7. Everyone should have their own lifestyle, religious beliefs, and sexual
preferences, even if it makes them different from everyone else.
''')
answer1=input()

jiancha()

scorefan()

print('''
8. The “old-fashioned ways” and the “old-fashioned values” still show
the best way to live.
''')
answer1=input()

jiancha()

scorezheng()

print('''
9. You have to admire those who challenged the law and the majority’s view
by protesting for human right and equality.
''')
answer1=input()

jiancha()

scorefan()

print('''
10. What our country really needs is a strong, determined leader who will crush
evil, and take us back to our true path.
''')
answer1=input()

jiancha()

scorezheng()

print('''
11. Some of the best people in our country are those who are challenging our
government and ignoring the “normal way things are supposed to be done.
''')
answer1=input()

jiancha()

scorefan()

print('''
12. There are many radical, immoral people in ourcountry today, who are trying
to ruin it for their own reactionary purposes,whom the authorities should put
out of action.
''')
answer1=input()

jiancha()

scorezheng()

print('''
13. A “woman’s place” should be wherever she wants to be. The days when women
are submissive totheir husbands and social conventions belong strictly in the
past.
''')
answer1=input()

jiancha()

scorefan()

print('''
14. Our country will be great if we honor the ways of our forefathers, do what
the authorities tell us to do, and get rid of the “rotten apples” who are
ruining everything.
''')
answer1=input()

jiancha()

scorezheng()

print('''
15. There is no “ONE right way” to live life; everybody has to create their
own way.
''')
answer1=input()

jiancha()

scorefan()

print('''
16. Homosexuals and feminists should be praised for being brave enough to defy
traditional family values.
''')
answer1=input()

jiancha()

scorefan()

print('''
17. This country would work a lot better if certain groups of troublemakers would
just shut up and accept their group’s traditional place in society.
''')
answer1=input()

jiancha()

scorezheng()

print('''
Thanks for your participation!
Your score for authoritarian personality is %d.
''' %count)

if 34<count<69:
    print('''
You show a strong authoritarian personality, who are easily to agree
with traditional values and obey the authority.
    ''')

if 0<count<35:
    print('''
You show a moderate authoritarian personality, who have the tend to agree
with traditional values and obey the authority.
    ''')

if count==0:
    print('''
You are either totally neutral or indifferent to politics!
    ''')

if -34<count<0:
    print('''
You do not show authoritarian personality, who are more tolerant of social
diversity.
    ''')

if -69<count<-33:
    print('''
You are strogly against authoritarian personality, who emphasize values
different from the mojority.
    ''')




