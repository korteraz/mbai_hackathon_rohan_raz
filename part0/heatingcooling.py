#Raz Kurteran and Rohan Kumar
def average_temp():
    heat_days = 0
    cool_days = 0
    temp_input = int(input("Enter the average daily temperature: "))
    while temp_input > -459:
        if temp_input > 80:
            heat_days += 1
        if temp_input < 60:
            cool_days += 1
        temp_input = int(input("Enter the average daily temperature: "))
    return heat_days, cool_days

if __name__ == '__main__':
    heat_days, cool_days = average_temp()
    print(f"Heating Days: {heat_days}")
    print(f"Cool Days: {cool_days}")



