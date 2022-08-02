from flask import *
import json

app = Flask(__name__)

@app.route('/', methods=["GET"])
def main_func():
	return "<p>Go to a specific api</p>"

@app.route('/phrase_rec/', methods=["GET"])
def rec_returner():
	user_query = str(request.args.get('text_so_far')).lower()   #/?text_so_far=...

	with open("teenwords.txt") as teenwords:
		list_of_words = teenwords.readlines()
		word_list = []
		for word in list_of_words:
			new_word = word.strip().lower()
			if user_query in new_word:
				word_list.append(new_word)

	top_list = []
	second_list = []
	bottom_list = []
	for word in word_list:
		if user_query[0]==word[0] and user_query[1]==word[1]:
			top_list.append(word)
		elif user_query[0]==word[1] and user_query[1]==word[2]:
			second_list.append(word)
		else:
			bottom_list.append(word)

	list_main = top_list + second_list + bottom_list

	main_list = []
	for i in range(0, len(list_main)):
		if len(main_list)<5:
			main_list.append(list_main[i])
		else:
			break

	main_list_len = 5 - len(main_list)
	for i in range(0, main_list_len):
		main_list.append("")

	data_set = {'item_1': main_list[0], 'item_2': main_list[1], 'item_3': main_list[2], 'item_4': main_list[3], 'item_5': main_list[4]}
	json_dump = json.dumps(data_set)
	return json_dump
	
if __name__ == "__main__":
	app.run(port=80, host="0.0.0.0")
