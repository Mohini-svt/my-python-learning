
# list and tuple
# list is a built in data type that is somewhat similar to a an array 
# but it can store diff types of datatypes.It is mutable too.

cities = ["banglore", "delhi", "pune","kerala","gujarat","delhi"]
print(cities)
print(cities[0])
cities[3] = "Vskp" #lists are mutuable unlike strings 
print(cities)

print(cities[0:4]) #slicing same as in strings.

print(len(cities))



# list functions:
# Wouldn't return upated values like strings untill you print the list specificallly only.


# an element would be added at the end.
cities.append("Jsr") 
print(cities)

# arranges in ascending order.
cities.sort()
print(cities)

# descending order
print(cities.sort(reverse=True))

# reverses the list.
print(cities.reverse())

# adds an any element at the user inputed index
cities.insert(2,"Kashi")
print(cities)

# removes the first occurence of the element.
cities.remove("delhi")
print(cities)

# removes the element completely.
cities.pop(6)
print(cities)




# tuple (built-in data type taht lets us create immutateable squences of values)
menu = ("Fried rice","Paneer do pyaaza","Buter naan","Gulab jamun","Manchurian","Samosa chaat")
fruits = ("banna","apple","pear","plum","orange")
animals = ("tigeer","lion","monkey","dog","cat")

foodstuff_pg = menu + fruits + animals
print(foodstuff_pg)
foodstuff_It = list(foodstuff_pg)
print(foodstuff_It)
print(foodstuff_It[0:4])
print(foodstuff_It[0:2]) #first three items
print(foodstuff_It[2:4]) #last three items







