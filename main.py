def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def num_words():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    return len(words)

def num_letters():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    letters = {}
    for word in words:
      for letter in word:
          if letter.lower() in letters:
            letters[letter.lower()] += 1
          else:
            letters[letter.lower()] = 1
    print(letters)
    return letters
  
def get_book_text(path):
    with open(path) as f:
        return f.read()

num_letters()
