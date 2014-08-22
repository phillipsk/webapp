#This is a comment
#This is a test function
#Here is the power of a function
#We also call this function

#To run this function, save the file as test_function.py
#Open the python interpeter and type python test_function.py

List_of_Gospels = ['Matthew', 'Mark', 'Luke', 'John'] #there are only three names here (in programming langauge 0 always has a value)
"""
The above is a list, read the book Lists are in Chapter 10
Functions are in Chapter 3
Google tutorials point for python tutorials regarding anything python
Stackoverflow is also your friend
As well as the offical python.org/doc
(Look no #comment syntax is needed here, as the three quotations represent the same value as #comment)
"""

Question_1 = "\nHello Sir/Madam, may I ask do you know of the Gospels?\n"  #\n signifies new line
Answer_1 = raw_input(Question_1)

if Answer_1 in ['Yes','yes','Y','y']: #here is another list, this list declares all our available responses
	Question_2 = "\nWho is an author of the Gospels?\n"
	Gospels = raw_input(Question_2).title() #.title() is a method, delete this method off of this statement and enter "mark" lowercase, see what happens

	def Gospel_Test(Gospels): #defining the function 'Gospels_Test' - the arguement is () - the parameter being passed within the arguemnt is the parameter of the string defined previously in the line above
		if Gospels in List_of_Gospels[0:3]: #here we are testing to see if the arguement entered in inside our list defined above
			print "\nCorrect, that is one of the Gospels.\n"
		else: 
			print "\nIncorrect Sir/Maddam, please try again.\n"


		 
	Gospel_Test(Gospels) #calling the function, again with an arguement, remember all the arguement is, is () while the parameter is the string Gospels

else:
	print "\nOkay, thank you for your response.\n"
	
#and there are if statements in here as well as if-else statements


