from datetime import date

today = date.today()
todaysDate = today.strftime("%m/%d/%y")
username =  input("What is your name?")
  

  

print("Hello " + username + "!" + " Today's Date is: ", todaysDate)


