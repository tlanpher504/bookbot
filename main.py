from stats import word_count,char_count,sort_char
import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
        	book_text=f.read()
        	return(book_text)

def print_report(book, num, sorted_char):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book}...")
	print("----------- Word Count ----------")
	print(f"Found {num} total words")
	print("--------- Character Count -------")
	for item in sorted_char:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")

	print("============= END ===============")

def main():
	book=sys.argv[1]
	get_book_text(book)
	full_string=get_book_text(book)
	num=word_count(full_string)
	dict1=char_count(full_string)
	sorted_char=sort_char(dict1)
	print_report(book,num,sorted_char)

if len(sys.argv)!=2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
main()



"""
path_to_file = "books/frankenstein.txt"
"""


'''
main('books/frankenstein.txt')
print(book_text)
'''
