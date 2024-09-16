import datetime

# while true:
# NO IF STATEMENTS
# 'continue' to go back if there's an error
while True:
    try:
        integer = int(input("Enter a integer that represent a month: "))
        break
    except ValueError:
        print("Please enter a character that can be converted to an integer")
    except:
        print("Please try again and enter a value inside the range of 1-12")

numOfMonth = str(integer)
conversion = datetime.datetime.strptime(numOfMonth, "%m")
numOfMonth = conversion.strftime("%B")
print(numOfMonth)
