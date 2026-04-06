
#  Ask user to input temperature
temp = float(input("Please input temperature in Celsius: "))

# Analyze the temperature and Display 
if temp < 0:
      print("FREEZING")
elif 0 <= temp <= 20:
      print("COLD")
else:
      print("NORMAL")