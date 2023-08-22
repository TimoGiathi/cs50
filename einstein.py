
def convert(mass):
	# Constants
	speed_of_light = 300000000 
	# Calculate energy using E = mc^2
	return int(mass * speed_of_light ** 2)


def main():

	# Get mass from the user
	res = int(input("Enter mass in kilograms: "))

	energy = convert(res)
	
	# Print the equivalent energy in Joules
	print(energy)


main()