# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
dt = input()
month, day, year = (int(x) for x in dt.split(' '))    
answer = datetime.date(year, month, day).weekday()
if(answer == 0):
    print('MONDAY')
elif(answer == 1):
    print('TUESDAY')
elif(answer == 2):
    print('WEDNESDAY')
elif(answer == 3):
    print('THURSDAY')
elif(answer == 4):
    print('FRIDAY')
elif(answer == 5):
    print('SATURDAY')
elif(answer == 6):
    print('SUNDAY')
else:
  print('Invalid Input')
