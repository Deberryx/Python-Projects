"""
Mad Libs Generator
------------------------------
"""
#Loop back at this point once code finishes
loop = 1
while (loop < 10):
#All the questions that the program aska the user
   noun = input ("choose a noun: ")
   p_noun = input("choose a plural noun: ")
   noun2 = input("Choose a noun")
   place = input("Name a place: ")
   adjective = input("Choose an adjective(Describing word): ")
   noun3 = input("Choose a noun: ")
#Display the story based on the users input
   print ("--------------------------------------------")
   print ("Be kind to your",noun,"- footed", p_noun)
   print ("For a duck may be somebody's", noun2,",")
   print ("Be kind to your",p_noun,"in",place)
   print ("where the weather is always",adjective,",")
   print ()
   print ("You may think that is this the",noun3,",")
   print ("well it is.")
   print ("--------------------------------------------")
#loop back to "loop = 1"
   loop = loop + 1
