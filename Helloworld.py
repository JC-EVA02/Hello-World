from datetime import date

today = date.today()
todaysDate = today.strftime("%m/%d/%y")
username = "Jose"

print("Hello " + username + "!" + " Today's Date is: ", todaysDate)


