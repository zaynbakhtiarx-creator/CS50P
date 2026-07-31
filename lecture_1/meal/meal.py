def main():
    time = input('What time is it?: ')
    eating_time = convert(time)
    if 7 <= eating_time <= 8:
        print('breakfast time')
    elif 12 <= eating_time <= 13:
        print('lunch time')
    elif 18 <= eating_time <= 19:
        print('dinner time')


def convert(t):
    hours, minutes = t.split(':')
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 60
    return hours + minutes
    


if __name__ == "__main__":
    main()