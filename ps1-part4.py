
prior_arrest= int(input("Prior arrest: "))

prior_arrest_for_local_ordinance= input("Prior arrests for local ordinance (Y/N):")

Age = int(input(" Age at release:"))

score= 0

if prior_arrest>=2:
    score+=1
    
if prior_arrest>=5:
    score+=1
    
if prior_arrest_for_local_ordinance == "Y":
    score+=1
else:
        score+=0

if Age>=40:
    score-=1

if 18<= Age<=24:
    score+=1
print("The recidivism risk score is" , score)
