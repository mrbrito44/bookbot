def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = counter(text)
    chars_dict = chars_count(text)
    print(chars_dict)



def chars_count(text):
    char_list = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_list:
            char_list[lowered] += 1
        else:
            char_list[lowered] = 1
    return char_list




def counter(text):
    words = text.split()
    print(len(words))
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()



    

        

main()
