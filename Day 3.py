
# indexing is basically theb position of the characters(starts with 0)
# lenth of string is total number of char with spaces and special char included.
notion = "Welcome to the ultimate productivity tool"
print(notion[9])
print(len(notion)) #length of a string is also the last index of the string. 
# total+1 is how length is calculated (41)




# slicing of a string (it's basically accessing the parts of a string)
# slicing has negative values too(-7,-8 etc) that go backward 
# synatx - [starting index: ending index] ; where ending index is not included 


print(notion[4:9])
print(notion[ :9]) #starts with first index which is 0.
print(notion[0: ]) #length os string





# string functions

str_3 = "i'm a game developer."

#returns true if the substring has the same value
print(str_3.endswith("er."))

# #capitalizies 1st char only once until another string is created and stores the value of this string in it.
print(str_3.capitalize())

#  #replaces one value with another according to how you input info.
print(str_3.replace("game", "software"))

#  #find a substring's 1st index from the main string.
print(str_3.find("developer"))

#  #counts the no. of times a specific inputed substring occurs.
print(str_3.count("am"))

