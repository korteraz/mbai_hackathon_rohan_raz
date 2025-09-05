#Raz Kurteran and Rohan Kumar
def calculate_ticket(driving_speed, speed_limit):
    if driving_speed - speed_limit <= -10:
        return 50
    if 6 <= driving_speed - speed_limit <= 20:
        return 75
    if 21 <= driving_speed - speed_limit <= 40:
        return 150
    if driving_speed - speed_limit > 40:
        return 300

    return 0


if __name__ == '__main__':
    speed_limit = int(input("Enter the speed limit: "))
    driving_speed = int(input("Enter your driving speed: "))

    print(calculate_ticket(driving_speed, speed_limit))