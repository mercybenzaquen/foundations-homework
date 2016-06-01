# Mercy Benzaquen
# 2016-05-30
# Homework 3
print("LISTS")

#print("QUESTION1")
Countries = ["Colombia", "Venezuela", "Brazil", "Ecuador", "Bolivia", "Chile", "Paraguay"]

print("QUESTION2")
for each_country in Countries:
    print(each_country)
print("QUESTION3")
Sorted_countries = sorted(Countries)
print(Sorted_countries)
print("QUESTION4")
print(Sorted_countries[0])
print("QUESTION5")
print(Sorted_countries[-2])
#Countries.pop("Brazil") Did not work, why?
print("QUESTION6")
Sorted_countries.remove('Brazil')
print(Sorted_countries)
print("QUESTION7")
for each_country in Sorted_countries:
    print(each_country)
print("DICTIONARIES")
#print("QUESTION1")
Tree = {'name':"Jaya Sri Maha Bodhi", 'species':"Sacred fig", 'age':"2300", 'location_name':"Anuradhapura, Sri Lanka", 'latitude':"8.3452", 'longitude':"80.3881"}
print("QUESTION2")
print((Tree['name']), "is a", (Tree['age']), "tree that is in", (Tree['location_name']))
print("QUESTION3")
if float(Tree['latitude']) < 40.7128:
    print("The", (Tree['name']), "in", (Tree['location_name']), "is south of NYC")
else:
    print("The", (Tree['name']), "in", (Tree['location_name']), "is north of NYC")
age = input("How old are you?")
age_difference = int(Tree['age']) - int(age)
if int(age) > int(Tree['age']):
    print("You are", (age_difference) * -1, "years older than", (Tree['name']))
#I multiplied the age difference so I can get a positive number when:
#If the person is 15,000 --> You are -12700 years older than Jaya Sri Maha Bodhi
elif int(age) < int(Tree['age']):
    print((Tree['name']), "was", age_difference, "years old when you were born.")
print("LIST OF DICTIONARIES")
print("QUESTION2 and QUESTION3")

list_of_dictionaries = [ {'name': "Moskow", 'latitud': "55.7558", 'longitude':"37.6173"} ,
 {'name': "Tehran", 'latitud': "35.6892", 'longitude':"51.3890"} ,
{'name': "Falkland Islands", 'latitud': "-51.7963", 'longitude':"-59.5236"} ,
{'name': 'Seoul','latitud': "37.5665", 'longitude':"126.9780"}]


for dictionaries in list_of_dictionaries:
    print((dictionaries['name']), ":")
    if float(dictionaries['latitud']) > 0:
        print((dictionaries['name']), "is above the Equator" )
        if float(dictionaries['latitud']) > 8.3452:
            print("Jaya Sri Maha Bodhi", "is north", (dictionaries['name']))
        elif float(dictionaries['latitud'])< 8.3452:
            print("Jaya Sri Maha Bodhi", "is south", (dictionaries['name']))
    if float(dictionaries['latitud']) < 0:
        print((dictionaries['name']), "is below the Equator" )
        if float(dictionaries['latitud'])< 8.3452:
            print("Jaya Sri Maha Bodhi", "is south", (dictionaries['name']))
    if float(dictionaries['latitud']) == -51.7963:
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

print("QUESTION3 just south or north tree")
for dictionaries in list_of_dictionaries:
    if float(dictionaries['latitud'])> 8.3452:
        print("Jaya Sri Maha Bodhi", "is north", (dictionaries['name']))

    elif float(dictionaries['latitud'])< 8.3452:
        print("Jaya Sri Maha Bodhi", "is south", (dictionaries['name']))
