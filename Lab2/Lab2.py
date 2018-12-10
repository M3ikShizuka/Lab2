import operator
#####################################################################################################################
##################################################### Funcs: ########################################################
#####################################################################################################################
def main():
    text = input("Text: ")
    work_text = text.split('.')[0]
    favorite_char = None
    favorite_value = 0
    count = {}
    best_letters = {}

    # Количество повторений символов.
    for char in work_text:
        if char.isalpha() == False:
            continue
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Наиболее часто повторяющиеся символ
    fav = max(count.items(), key=operator.itemgetter(1))
    favorite_char = fav[0]
    favorite_value = fav[1]

    # Наиболее часто повторяющиеся символы
    for key, value in count.items():
        if value == favorite_value:
            best_letters[key] = value

    # Первый символ по алфавиту
    for char in best_letters:
        if char < favorite_char:
            favorite_char = char

    # Поиск первого вхождения и размера
    for char in work_text:
        low = char.lower()
        if (low == favorite_char):
            favorite_char = char

    print("%s %i" % (favorite_char, favorite_value))
#####################################################################################################################
##################################################### Exec: #########################################################
#####################################################################################################################
main()