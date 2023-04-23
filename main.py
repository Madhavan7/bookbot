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
        if letter.isalpha():
          if letter.lower() in letters:
            letters[letter.lower()] += 1
          else:
            letters[letter.lower()] = 1
    return letters

def get_report():
  num = num_words()
  letters = num_letters()
  letters_array = [(letter, letters[letter]) for letter in letters]
  letters_array.sort(reverse=True, key = lambda x:x[1])
  print("--- Begin report of books/frankenstein.txt ---")
  print(str(num) + " words found in the document\n")
  for i in range(len(letters_array)):
    print("The \'" + letters_array[i][0] + "\' character was found " + str(letters_array[i][1]) + " times")
  
def get_book_text(path):
    with open(path) as f:
        return f.read()

get_report()
