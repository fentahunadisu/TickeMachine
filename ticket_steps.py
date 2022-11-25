from store import drug_stor
from massege import massage

def first_step():
  massage1 = massage("your number is")
  massage2 = massage("please wait and someone will assist you shortly")
  list = """"
         1 cosmetics
         2 medicine
         3 perfume"""
  id_list = [1234, 4321]
  count = 0
  count_limit = 3
  while count_limit > count:
    id = int(input("please enter your id"))
    if id in id_list:
      print(list)
      order = input("please choose your product area from drug store")
      while order != "":
        print(massage1)
        drug_stor()
        print(massage2)
        permission = input("do you want continue y/n")
        if permission == "y":
            order = input("please choose your product area: ")
        else:
          print("try again please")
        break
      else:
        order = input("please choose your product area from drug the list")
    else:
      print("please try again")
    count += 1