''' an inspector calls quote searcher written by Casey Williams '''

def find_act(line_number, filename):
	with open(filename, 'r') as f:
		for(i, line) in enumerate(f):
			if (i <= line_number):
				if '{{act' in line.lower():
					act = line.lower().title().replace("{", "")
	return act

#filename = input("Please enter the name of the .txt (e.g. myfile.txt): ")
filename = "an_inspector_calls.txt"

try:
	open(filename)
except:
	print("File does not exist! Quitting...")
	exit()

while (True):
	quote = raw_input("Enter the quote you'd like to find, enter '%quit%': ").lower()
	if(quote == "%quit%"):
		print("Bye!")
		exit()
	padded_quote = str(" " + quote + " ")
	print("")
	with open(filename, 'r') as f:
		result = 0
		results = []
		for (i, line) in enumerate(f):
			if (padded_quote in line): 
				act = find_act(i, filename)
				person = line.split(":")[0].replace("\t", "")
				print("("+ str(result) +") The quote " + quote + " occurs on line " + str(i) + " spoken by " + person + " in " + act)
				result += 1
				results.append(line)
	
	while(True):
		print("")
		choice = raw_input("If you'd like to see the full line, enter the result number in the brackets, else just press enter: ")
		if(choice == ""):
			print("")
			break
		else:
			print("")
			print(results[int(choice)])
