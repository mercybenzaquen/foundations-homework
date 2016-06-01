#Mercy Benzaquen
#05/23/16
#Homework 1

name = input("What's your name?")
print ("Hola, " + name)
yearofbirth = input ("What year were you born in?")
if int(yearofbirth) >= 2016:
    print ("Oops looks like you made a mistake, try again")
yearofbirth = input ("Try again, year of birth?")
#I don't know how to keep it from showing all the extra info if they put a
#date in the future
age = 2016 - int(yearofbirth)
print ("You are roughly", age, "years old")
heartbeat = age * 42048000
print ("Your heart has beaten", heartbeat, "times in your lifetime")
bluewhale = age * 3153600
print ("A blue whale's heart has beaten", bluewhale, "times in your lifetime")
rabbit = age * 68328000
print ("A rabbit's heart has beaten", rabbit, "times in your lifetime")
formula = rabbit // 1000000000000
if rabbit >= 1000000000000:
    print (formula, "billion")
#HELPPP
venus = age // 0.62
print("If you lived in Venus you would be", venus, "years old")
neptune = age * 164.79
print("If you lived in Neptune you would be", neptune, "years old")
if age > 22:
    difference = age - 22
    print ("You are", difference, "years older than me!")
elif age < 22:
    difference2 = 22 - age
    print("You are", difference2, "years younger than me!")
elif age == 22:
    print("We are the same age")
mod = int(yearofbirth) % 2
if mod > 0:
    print ("Your were born in an odd year")
else:
    print ("Your were born in an even year")

if int(yearofbirth) >= 2009:
    print ("The Pittburghs Steelers have won 1 superbowls in your lifetime")
if int(yearofbirth) >= 2006 and int(yearofbirth) <= 2009:
    print ("The Pittburghs Steelers have won 2 superbowls in your lifetime")
if int(yearofbirth) >= 1980 and int(yearofbirth) <= 2006:
    print ("The Pittburghs Steelers have won 3 superbowls in your lifetime")
if int(yearofbirth) >= 1979 and int(yearofbirth) <= 1980:
    print ("The Pittburghs Steelers have won 4 superbowls in your lifetime")
if int(yearofbirth) >= 1976 and int(yearofbirth) <= 1979:
    print ("The Pittburghs Steelers have won 5 superbowls in your lifetime")
if int(yearofbirth) >= 1974 and int(yearofbirth) <= 1976:
    print ("The Pittburghs Steelers have won 6 superbowls in your lifetime")

if int(yearofbirth) >= 1933 and int(yearofbirth) <= 1945:
    print ("FDR was in office when you were born")
if int(yearofbirth) >= 1945 and int(yearofbirth) <= 1953:
    print ("Harry S. Truman was in office when you were born")
if int(yearofbirth) >= 1953 and int(yearofbirth) <= 1961:
    print ("Dwight D. Eisenhower was in office when you were born")
if int(yearofbirth) >= 1961 and int(yearofbirth) <= 1963:
    print ("John F. Kennedy was in office when you were born")
if int(yearofbirth) >= 1963 and int(yearofbirth) <= 1969:
    print ("Lyndon B. Johnson was in office when you were born")
if int(yearofbirth) >= 1969 and int(yearofbirth) <= 1974:
    print ("Richard Nixon was in office when you were born")
if int(yearofbirth) >= 1974 and int(yearofbirth) <= 1977:
    print ("Gerald Ford was in office when you were born")
if int(yearofbirth) >= 1977 and int(yearofbirth) <= 1981:
    print ("Jimmy Carter was in office when you were born")
if int(yearofbirth) >= 1981 and int(yearofbirth) <= 1989:
    print ("Ronald Reagan was in office when you were born")
if int(yearofbirth) >= 1989 and int(yearofbirth) <= 1993:
    print ("George W. Bush was in office when you were born")
if int(yearofbirth) >= 1993 and int(yearofbirth) <= 2001:
    print ("Bill Clinton was in office when you were born")
if int(yearofbirth) >= 2001 and int(yearofbirth) <= 2009:
    print ("George W. Bush was in office when you were born")
if int(yearofbirth) >= 2009 and int(yearofbirth) <= 2016:
    print ("Barack Obama was in office when you were born")
