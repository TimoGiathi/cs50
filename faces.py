
def convert(mood):
	moods = {
		":)" : "🙂",
		"(:" : "🙁",
		"other" : "😐",
	}

	# hello ken :)
	arr = mood.split(" ")
	emoticon = arr[len(arr)-1] 
	if( emoticon in moods) :
		return moods[emoticon]
	else :
		return moods["other"]


def main():
	res = input("enter your mood? ")

	mood_with_emoji = convert(res)

	print(mood_with_emoji)


main();