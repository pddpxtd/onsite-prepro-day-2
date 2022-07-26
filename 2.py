'''ตัวเลขที่มีอยู่'''
def main():
    '''ตัวเลขทีี่มีอยู่'''
    long = input()
    value1 = 0
    while True:
        value = input()
        if value <= long:
            value2 = int(value)
            while value2 >= 0:
                value2 = int(input())
                if value2 >= 0:
                   value1 += value2
                   print("Sum of Found Number = %d"%value1)
        elif value > long:
            print("Not Found Number")
        elif value == 0:
            print("No Tape Measure")
        elif value == "No more!":
            break
main()

นอนกันเถอะ เย้