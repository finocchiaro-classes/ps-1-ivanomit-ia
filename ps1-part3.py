
def heart_rate(age,goal):
    max_hr= 220- age
    print ("Your maximum heart rate is :", max_hr)

    if goal== 'S':
        print('Your target Heart rate range is', max_hr*0.8, 'and', max_hr*1)
    if goal == 'E':
        print('Your target Heart rate range is', max_hr*0.6, 'and', max_hr*0.6)
    



user_age= int( input('what is your age?'))

user_goal= input(" is your goal speed(S) or endurance(E)?")              


heart_rate(user_age, user_goal)
