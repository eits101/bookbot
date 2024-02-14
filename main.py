def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = num_words(text)
    dict_letters = num_letters(text)
    sorted = sort(dict_letters)


    print(f"--- Begin report of {book_path} ---")
    print(f"{num_of_words} words found in the document")
    print()
    for i in sorted:
        print(f"The '{i["letter"]}' character was found {i["num"]} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def num_words(text):
    words = text.split()
    return len(words)


def sort_on(dic):
    return dic["num"]




def sort(dic):
    sorted = []
    for letter in dic:
        if letter.isalpha():
            sorted.append({"letter": letter, "num": dic[letter]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted


def num_letters(text):
    words = text.split()
    letters = {}
    for word in words:
        for letter in word:
            lower_letters = letter.lower()
            if lower_letters not in letters:
                letters[lower_letters] = 0
            letters[lower_letters] += 1
    return letters


main()
