def consonant_counter(word):
    consonant="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count= sum(1 for any in word if any in consonant)
    return count

word=input("Enter a word: ")
print("Number of consonants:", consonant_counter(word))
