def main():

	user_prompt=input("What is the Answer to the  Great Question of Life, the Universe and Everything? ")

	case_accepted=["forty-two","forty two" ,"42"]

	if user_prompt in case_accepted:
			print("Yes")
	else:
			print("No")	

main()		
