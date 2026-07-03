def CheckVowel(ch):
    if ch in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonant")

def main():
    ch = input("Enter a character: ")

    if len(ch) == 1 and ch.isalpha():
        CheckVowel(ch)
    else:
        print("Please enter a single alphabet.")

if __name__ == "__main__":
    main()