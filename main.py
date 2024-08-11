def countSpaces(inputString):

   spaces_count = 0
   for index in range(0, len(inputString)):
   
      if inputString[index] == " ":

         spaces_count += 1

   return spaces_count

inputString = "My favourite tourist place is Paris"


print("Count of no of spaces in an input string:", countSpaces(inputString))