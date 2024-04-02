gamelib = { 
    "Donkey_Kong" : { "copies" : 3 , "cost" : 2},
    "Super_Mario_Bros" :{ "copies" : 5 , "cost" : 3},
    "Tetris" : { "copies" : 2 , "cost" : 1}
}

userlist = {}

adminuser = "admin"
adminpassword = "adminpass"
log_in = False
adminlog_in = False
usercurrent = ''


def userreg():
 while True:   
    try:

     newusername = input("Enter new username: ")  
     if not newusername :
       return 
    
     newpassword = input("Enter new password: ")
     if not newpassword :
        return
    
     if newusername in userlist:
        print("Username already exists")
        return
     
     userlist[newusername] = {"password": newpassword, "balance": 0, "points": 0}
    
    except ValueError as e:
     print(e)
    break

def login():
  while True:
    try: 
      
      username = input("Enter your username: ")
      if not username:
        return

      password = input("Enter your password ")
      if not password:
        return
      
      if username not in userlist:
        print("Username does not exist") 
        return
      
      if password == userlist[username]["password"]:
        global log_in
        global usercurrent
        usercurrent = username
        log_in = True

        print("login successful")

    except ValueError as e:
     print(e)
    break
  
def adminlogin():
    while True:
      try:

       a_username = input("Enter your username: ")
       if not a_username:
        return

       a_password = input("Enter your password ")
       if not a_password:
        return
      

       if a_username == adminuser and a_password == adminpassword:
         global adminlog_in
         adminlog_in = True

         print ("Admin Login Successful")

      except ValueError as e:
       print(e)
      break

def availablegames():
  for games,details in gamelib.items():
    print(f"{games}: {details}")


def gamerent():
  while True:
      try:
        availablegames()
        for games,details in gamelib.items():
        
         choice = input("Enter your choice: ")
         if choice == '1': 
          pass
          
def main():
  print("Welcome to the Game Rental System: ")
  print("")
  print("")
  print("")
  print("")
  print("")




  
      
  


    



      




    
