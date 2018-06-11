1. Setup environment
	`sudo apt install python python-mechanize`
2. Create cookie
-	a) Open http://ma.playboy.tv/ and create free an account
-	b) Login to your account, press F12, click "Console" tab
-	    and type `document.cookie[Enter]`
-	c) Copy whole output data and save it to cookie.dat
3. Getting downloadable video URL
-	a) Choose your video URL, (example):
-	  http://ma.playboy.tv/show/video/29311/real-p-o-v-season-02-ep-03/
-	b) Open Terminal, cd to project folder, run:
-	  `python main.py <video URL>`
-	c) Press `y[Enter]` if the code find downloadable URL and wait
-	   Or copy download link and download by your application