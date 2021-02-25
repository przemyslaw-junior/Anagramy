#  Anagramy z liter jednego słowa można utworzyć inne slowo
def anagram(slowo_1, slowo_2):
    # posortowanie i sprawdzenie ciągu znaków
    if(sorted(slowo_1)== sorted(slowo_2)):
        print('Te słowa to Anagramy')
    else:
        print('Te słowa to nie Anagramy')

print('pierwsze słowo')
slowo_1 =input().lower()
print ('drugie słowo')
slowo_2 =input().lower()
anagram(slowo_1, slowo_2)