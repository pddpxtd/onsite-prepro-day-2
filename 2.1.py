"""ตัวเลขที่มีอยู่"""
def main():
    """ตัวเลขทีี่มีอยู่"""
    length = int(input())
    you = 0
    if length <= 0:
        return print("No Tape Measure")
    while True:
        text = input()
        if text == "No more!":
            break
        if int(text) <= length:
            you += int(text)
    if you == 0:
        print("Not Found Number")
    else:
        print("Sum of Found Number = "+str(you))
main()
