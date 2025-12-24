def word_count(book_text):
        all_words=book_text.split()
        num_words=len(all_words)
        return(num_words)

def char_count(book_text):
	book_text=book_text.lower()
	chars={}
	for letter in book_text:
		if letter not in chars:
			chars[letter]=0
		chars[letter]+=1
	return(chars)

def sort_on(item):
	return item['num']

def sort_char(dictionary):
	dict_list=[]
	for char,num in dictionary.items():
		dict_list.append({'char':char,'num':num})
	dict_list.sort(reverse=True, key=sort_on)

	return dict_list
