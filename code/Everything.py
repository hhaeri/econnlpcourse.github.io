"""
A program to demonstrate all concepts covered in the Python fundamentals crash course

Problem 1 in Chapter 10 of Py4E - https://www.py4e.com/html3/10-tuples
"Exercise 1: Revise a previous program as follows: Read and parse the “From” lines
and pull out the addresses from the line. Count the number of messages
from each person using a dictionary. After all the data has been read,
print the person with the most commits by creating a list of (count, email)
tuples from the dictionary. Then sort the list in reverse order
and print out the person who has the most commits."

context: you can use mbox-short.txt as input.

Approach: This file has lines starting with: "From" followed by a space, an email id and so on.
These are the lines we want and rest of the lines are not needed for this program
"""

from_counts = {} #an empty dictionary object to store  <email id, number of times they sent emails> pairs.
""" a dictionary because I want to store an email id (key) and the number of times 
it appeared  in the From: field in the text"""

# Let us start by reading the file line by line:
fh = open("files/mbox-short.txt") #open a file handler

for line in fh: #read the file line by line
    # We have to now see if the line is starting with "From"
    if line.startswith("From"): #use the
        # All lines that start with a From are not necessarily in the format we want.
        try: #what if there is no space at all in this line? the line below will throw an error
            temp = line.split(" ") #.split() method splits a string into pieces and returns a list.

            #You can print the variable temp here if you want to see what it looks like.

            if temp[0] == "From" and "@" in temp[1]: #conditional and boolean expressions.
                """
                At the beginning, I initiated an empty dictionary object to store the email id and the 
                number of times it was in the "From" field. Here, we start populating that dictionary,
                each time we see a line starting with From and has an @ symbol -which I use as a proxy
                to identify the email. The following line looks for temp[1] i.e., an email id
                in from_counts dictionary. If it finds it, it adds one to the number of times it appeared
                so far in the text. Else, it assigns that email as a new key, and starts the counter at 1. 
                """
                from_counts[temp[1]] = from_counts.get(temp[1],0)+1
        except:
            print("This line starts with a From, but does not have the format we want")

fh.close() #close the file handler.

print(from_counts) #See what is in the dictionary.

#convert the dictionary into a list of tuples
from_counts_new = []
for key in from_counts.keys():
    from_counts_new.append((from_counts[key],key))

"""the above three lines can be condensed to a single line below. 
This is called "List comprehension" in Python. """
#from_counts_new = [(v,k) for k,v in from_counts.items()]

#from_counts_new contains a list of (count, email) tuples.
from_counts_new.sort(reverse=True)

#from_counts_new now contains (count, email) tuples, sorted in descending order of count.
#Remember: .sort() changes the list contents itself, and does not create a new list.
#print(from_counts_new)  #See the sorted list

print(from_counts_new[1]) #see the one with most sent emails

"""
Note: I wrote the code this way to make use of all data structures we discussed and put in conditionals, loops
exception handling, files- everything in place. There are optimal ways of writing the code. You can try yourselves!

The only things I did not use here are functions and main function. Try to add those too into this program!
"""