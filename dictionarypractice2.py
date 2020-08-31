D = {'red': 'apple',
'green':'lime',
'blue':'blueberry',
'orange':'orange',
'yellow':'lemon',
'pink':'dragonfruit'}

#asking for a color
choice = raw_input("What of color of fruit would you like?:")
if choice in D.keys():
    print choice

fruit = D.get(choice,0)

print fruit

choice2 = raw_input("What kind of fruit would you like?:")
#here the user will pick a fruit from the ones printed earlier 
#and only that fruit will be returned from the dictionary.
#so "if apple is in values, print apple"
#print choice2
#dictionary keys can only have one value
if choice2 in D.values():
    print choice2
