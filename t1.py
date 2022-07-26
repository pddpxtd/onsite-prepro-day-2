"""Atbash Cipher"""
def main():
    """Atbash Cipher"""
    txt = input()
    for i in txt:
        if i.isupper():
            print(chr(65-ord(i)+90), end="")
        elif i.islower():
            print(chr(97-ord(i)+122), end="")
        else:
            print(i, end="")
main()
