D = {'projectmanager':[99000], 'softwareengineer':[88000], 'softwaredesigner':[95000]}
switch = 0;
end = 0; #this is here to make a loop to end the program
#in place of a boolean, but has the same function
choice = raw_input("What job would you like to have?")

#why does this not take the right input after a wrong one?
while switch != 1:
    if choice in D.keys():
        switch = switch + 1;
        salary = D.get(choice,0) #here, the .get and ,0 is added to make the default 0 if the key is not found.
        print "The salary for this job is %s" % salary
    else:
        choice = raw_input()
        switch=0;

