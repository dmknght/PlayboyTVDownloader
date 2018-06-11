import sys

try:
	import utils, actions
except ImportError as error:
	print(error)
	sys.exit("Missing module!")
	

try:
	import re, json, mechanize
except ImportError as error:
	print(error)
	_, missing_moudle, _ = str(error).split("'")
	sys.exit("Usage: \"pip install %s\" or \"apt install python-%s\""
		%(missing_moudle, missing_moudle)
	)

	
try:
	getcookie = open('cookie.dat', 'r')
	cookie = getcookie.read()
	getcookie.close()
except:
	utils.printf("Error while reading cookie", "bad")
	sys.exit("Reading cookie.dat error")
	
if len(sys.argv) == 1:
	utils.print_help()
else:
	option = sys.argv[1]
	if option == "help" or option == "-h" or option == "--help":
		utils.print_full_help()
	else:
		actions.get_data(option, cookie)

