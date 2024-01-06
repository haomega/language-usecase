# import module
import re
# import module's method
from re import compile
# import current path test.py file
import test


# conditions
if 1 > 0: 
  str = "a"
  match str:
    case "a"
      print("is a")
    case _:
      print("default")
elif:
  print("else if")
else:
  print("else")


arr = [1,2,3]
# loop simple
for it in arr: 
  print(it)
# loop with index
for index, it in arr: 
  print(index,it)

# simple function 
def sum(): 
  return 0
def sum() -> int: 
  return 0


# toJSON method
def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)

