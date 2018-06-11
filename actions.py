import utils, sys, re, json

def parse_data(resp):
	parse = "paths\W\W(.*)\W\W,"
	try:
		link_info = re.findall(parse, resp, re.MULTILINE)[0]
		return link_info
	except:
		utils.printf("Can not get video URL", "bad")
		sys.exit(0)

def best_video_quality(link_dict):
	quality = link_dict.keys()
	max_value, best_quality = 0, ''
	for value in quality:
		int_value, _ = value.split('p')
		if int(int_value) > max_value:
			max_value, best_quality = int(int_value), value
	utils.printf("\nBest video quality: %s" %(max_value), "good")		
	return max_value, best_quality


def get_data(url, cookie):
	import mechanize
	try:
		process = mechanize.Browser()
		process.addheaders = [('Cookie', cookie)]
		process.set_handle_robots(False)
		process.open(url)
		if process.geturl() == "http://ma.playboy.tv/access/login":
			utils.printf("Got login page! Check your cookie", "bad")
			sys.exit(1)
			
		else:
			resp = process.response().read()
			link_info = json.loads(parse_data(resp))
			utils.print_table(("Quality", "Video URL"), *link_info.items())
			quality, best_format = best_video_quality(link_info)
			dload_link = link_info[best_format]
			utils.printf(dload_link, "good")

			utils.printf("Do you want to save this video? [Y]")
			option = raw_input()
			if option == "Y" or option == "y":
				if url[-1] == "/":
					dload_name = "%s_%s.%s" %(
						url.split('/')[-2],
						quality,
						re.findall(
							"%s.(.*)\?" %(best_format),
							dload_link,
							re.MULTILINE
						)[0]
					)
				else:
					dload_name = "%s_%s.%s" %(
						url.split('/')[-1],
						quality,
						re.findall(
							"%s.(.*)\?" %(best_format),
							dload_link,
							re.MULTILINE
						)[0]
					)
				utils.printf("Saving to %s" %(dload_name), 'good')
				utils.printf("Downloading, please wait....")
				process.retrieve(dload_link, dload_name)
				utils.printf("Download completed!", "good")

			else:
				utils.printf("You can download your video manually")
	
	except KeyboardInterrupt:
		utils.printf("Terminated by user!", "bad")
		sys.exit(1)

	except:
		utils.printf("Error while getting data", "bad")
		sys.exit(0)

	finally:
		process.close()
		