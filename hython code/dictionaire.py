# introducion au dictionaire avec python
import json

with open("database.json","r+") as jsfile:
   
 for index,food in enumerate(jsfile,start=1):
    print(f"{index}.{food}\n")
    