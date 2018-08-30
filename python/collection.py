fruits = ["Apple","Banana","Orange"]
print(fruits)
fruits[1]="WATERMELON"
print(fruits)

face = list(("eyes","nose","mouth"))
x = float(raw_input("Please enter a number If > 2 eyebrowes, else chick:  "))
if x > 2:
	face.append("EYEBROWES")
else:
	face.append("CHICK")
print(face)
z=str(len(face))
print("Returns the number of items in a list 'Face' : "+z)

