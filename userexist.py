def checkUserExist(userList , username , password) :
               present = False;
               for index in range(len(userList)) : 
                      if userList[index]["username"] == username and userList[index]["password"] == password : 
                             present = True;
               return present;      
