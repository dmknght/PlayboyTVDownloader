
def printf(mtext, mtype = 'warn'):
	############################################
	#	Print text w/ color
	#
	###########################################

	print(craft_msg(mtext, mtype))

def craft_msg(mtext, mtype = 'warn'):
	####################################################
	#	create text message with color
	#	bad: red
	#	warn: yellow
	#	good: light green
	#	This functions is using for Linux terminal only
	####################################################

	mtext = {
		'bad': '\033[91m{}\033[00m'.format(mtext),
		'warn': '\033[93m{}\033[00m'.format(mtext),
		'good': '\033[92m{}\033[00m'.format(mtext)
	}
	return (mtext[mtype])

def print_table(headers, *args, **kwargs):
	################################################
	#	print beautiful table in terminal style
	#	author @routersploit project
	#	ALL input data must be string
	################################################

	extra_fill = kwargs.get("extra_fill", 5)
	header_separator = kwargs.get("header_separator", "-")
	if not all(map(lambda x: len(x) == len(headers), args)):
		printf("Data does not fit table", 'bad')
		return
	def custom_len(x):
		try:
			return len(x)
		except TypeError:
			return 0
	fill = []
	headers_line = '  '
	headers_separator_line = '  '

	for idx, header in enumerate(headers):
		column = [custom_len(arg[idx]) for arg in args]
		column.append(len(header))
		current_line_fill = max(column) + extra_fill
		fill.append(current_line_fill)
		headers_line = "".join((headers_line, "{header:<{fill}}".format(header = header, fill = current_line_fill)))
		headers_separator_line = "".join((
			headers_separator_line,
			'{:<{}}'.format(header_separator * len(header), current_line_fill)
		))
	print(headers_line)
	print(headers_separator_line)
	for arg in args:
		content_line = '| '
		for idx, element in enumerate(arg):
			content_line = "".join((
				content_line,
				'{:{}}'.format(element, fill[idx])
			))
		print(content_line)
		
def print_banner():
	print("""
	PLAYBOY TV DOWNLOADER
	
>>>> Get Video link and download it for you <<<<
>>>> Playboy TV: http://ma.playboy.tv <<<<<
>>>> @Author: https://github.com/dmknght/PlayboyTVDownloader <<<<
""")
	
def print_full_help():
	print_banner()
	print("""
1. Setup environment
	sudo apt install python python-mechanize
2. Create cookie
	a) Open http://ma.playboy.tv/ and create free an account
	b) Login to your account, press F12, click "Console" tab
	    and type "document.cookie[Enter]"
	c) Copy whole output data and save it to cookie.dat
3. Getting downloadable video URL
	a) Choose your video URL, (example):
	  http://ma.playboy.tv/show/video/29311/real-p-o-v-season-02-ep-03/
	b) Open Terminal, cd to project folder, run:
	  python main.py <video URL>
	c) Press y[Enter] if the code find downloadable URL and wait
	   Or copy download link and download by your application
	""")
	
def print_help():
	print_banner()
	print("""
Usage:
	python main.py <playboy_tv_url>
	
Display help:
	python main.py help
 """)