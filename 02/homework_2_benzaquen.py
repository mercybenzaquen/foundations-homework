#Mercy Benzaquen
# 2016-05-25
#Homework2

#1
print("QUESTION 1")
numbers = [ 22, 90, 0, -10, 3, 22, 48]
print(numbers)
#1
print("QUESTION 1")
print(len(numbers))

#2
print("QUESTION 2")
print(numbers[3])

#3
print("QUESTION 3")
print(numbers[1]+ numbers[3])

#4
print("QUESTION 4")
print(sorted(numbers))
print(sorted(numbers)[5])

#5
print("QUESTION 5")
print(numbers)
print(numbers[6])

#6 wujuuu :)
print("QUESTION 6")
for anyelement in numbers:
    variable = anyelement
    if anyelement < 10 and anyelement % 2 == 0:
        print(variable * 30 + 6)
    elif anyelement < 10:
        print(variable * 30)
    elif anyelement != -10 and anyelement > 50:
        print(variable - 11)
    elif anyelement != -10:
        print(variable - 1)
#7 Sum the result of each of the numbers divided by two.
print("QUESTION 7")
#variable to store the sum
newnumber = (sum(numbers) // 2)
print(newnumber)

#Dictionaries
print("DICTIONARIES")

print("QUESTION 8")
Movie = {'Title': 'Zootopia', 'Year': '2016','Director': 'Byron Howard','Budget': 150000000,'Revenue': 983938315}
print("My favorite movie is", (Movie['Title']), "which was released in", (Movie['Year']), "and was directed by", (Movie['Director']))

print("QUESTION 9")
print((Movie['Revenue']) - (Movie['Budget']))

print("QUESTION 10")
if (Movie['Budget']) > (Movie['Revenue']):
    print("It was a flop!")
elif (Movie['Revenue']) > (Movie['Budget']) * 5:
    print("That was a good investment!")

print("QUESTION 11")
Population = {'Manhattan': 1.6, 'Brooklyn': 2.6, 'Bronx': 1.4, 'Queens': 2.3, 'Staten Island': 0.4}

print("QUESTION 12")
print(Population['Brooklyn'])

print("QUESTION 13")
everybody = Population['Manhattan'], Population['Brooklyn'], Population['Bronx'], Population['Queens'], Population['Staten Island']
print(sum(everybody))

print("QUESTION 14")
print( (Population['Manhattan'] / sum(everybody)) * 100,"%") 
