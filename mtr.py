import requests
import sys
import subprocess

url_list = open("urlist.txt").read()
urls = url_list.splitlines()

for url in urls:
	url_to_check = f"https://{url}"

	try:
	    requests.get(url_to_check)

	except requests.ConnectionError:
	    print("Website is Not Working",url_to_check)

	else:
	    print("Website is working",url_to_check)
	    subprocess.call(["wpscan","--url","%s"%url_to_check])
