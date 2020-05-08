import subprocess

print("""*****************************
	    MULIPLE SITES RUNNER
         *****************************""")
url_list = open('urllist.txt').read()
urls = url_list.splitlines()
subprocess.run("mkdir Output", shell=True)

for url in urls:
	with open("Output/%s"%url,'w') as f:
		p1 = subprocess.run("wpscan --url %s"%url, stdout=f, text=True, shell=True)
	print(open("Output/%s"%url).read())

