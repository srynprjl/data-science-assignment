## Ask the user to input a word and count vowels and consonent using a function

def count_vowels(word):
    vowel = 0
    consonant = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        if i in vowels:
            vowel += 1
        else:
            consonant += 1

    print(f"Vowels: {vowel}")
    print(f"Consonant: {consonant}")


while True:
    a = input("Enter a word")
    a = a.lower()
    if(a.isalpha()):
        break
    else:
        print("Invalid input.")


count_vowels(a)
