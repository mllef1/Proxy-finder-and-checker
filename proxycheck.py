import requests
import threading
import time
import os


#clear your screen so it looks all neat
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

try:
	os.system("pip install requests[socks]") # needed to use socks proxies
	os.system("pip install time") # time
	os.system("pip install threading") # threading
	clear()
except ImportError as e:
    print("Find a way to run this command: pip install 'requests[socks]'") # if the thing fucks up




thread_amm = int(input("Ammount of threads you want [pick based on how fast your internet connection is and how good your computer is]: "))


#big ass list of links, add your links to the list
socks5 = [
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
	"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
	"https://api.openproxylist.xyz/socks5.txt",
	"https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5",
	"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",
	"https://proxyspace.pro/socks5.txt",
	"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
	"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
	"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
	"https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt",
	"https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks5.txt",
	"https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",
	"https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
	"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
	"https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt",
	"https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt",
	"https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",
	"https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/socks5/global/socks5_checked.txt",
	"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
	"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
	"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
	"https://api.openproxylist.xyz/socks5.txt",
	"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
	"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
	"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
	"https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/socks.txt",
	"https://proxyspace.pro/socks5.txt",
	"https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5",
	"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
	"http://worm.rip/socks5.txt",
]

print("Gathering SOCKS5 proxies, this will only take a few seconds")

proxy_list = open("socks5.txt" , "a")

#for every line in the list of links, try to open a link and if it works put the content in a file
counter = []
counter_item = 0

for i in socks5:
	counter.append("-")

def get_list(line):
	try:
		getproxy = requests.get(line)
		proxy_list.write(getproxy.text)
	except:
		pass

for line in socks5:
	time.sleep(0.35)
	counter[counter_item] = "+"
	threading.Thread(target=get_list, args=(line,))
	counter_item += 1
	print(f"Completed: [{''.join(counter)}]", end='\r')
proxy_list.close()

print("\nlet it rest for 5 sec, so it can write down more proxies")
time.sleep(5)

print("\nDone\nRemoving duplicates\n")


#add them to list then check if it is in list to remove duplicates
prx = []
finallist = []
proxy_list = open("socks5.txt" , "r")
for ip in proxy_list:
	split_ip = ip.split(':')
	if split_ip[0] in prx:
		pass
	else:
		prx.append(split_ip[0])
		finallist.append(ip)
proxy_list.close()

proxy_list = open("socks5.txt", "w")
proxy_list.write("")
proxy_list.close()

proxy_list = open("socks5.txt", "a")
for i in finallist:
	proxy_list.write(str(i.replace(" ", "")))
proxy_list.close()

proxy_list = open("checked.txt", "w")
proxy_list.write("")
proxy_list.close()

clear()
print("Done fetching proxies. \nNow checking...")
proxy_list = open("socks5.txt" , "r")
lines = len(proxy_list.readlines())
proxy_list = open("socks5.txt" , "r")

#             ^
# shit i wrote some time ago i forgot what it does and i dont bother to read
#probably to fix the list

line_num = 0



checked_proxies = []

proxy_threads = []


def proxy_check(unchecked_proxy):

	try:



		unc_proxy = {
			"http": "socks5://" + unchecked_proxy,
			"https": "socks5://" + unchecked_proxy
		}


		response = requests.get(
		    'https://google.com', # you can set this to anything you want
		    proxies=unc_proxy,
		    timeout=20,

		)





		getloc_proxy = unchecked_proxy.split(":")


		getloc = requests.get(
			'http://demo.ip-api.com/json/' + getloc_proxy[0] + '?fields=66842623&lang=en', #this is to find the location of the proxy ip
			proxies=unc_proxy,
	    	timeout=20,

		)


		ipjson = getloc.json()
		location = ipjson['country']

		elapsed_time = response.elapsed




		spaces = 40 - len(unchecked_proxy)
		spaces = " " * spaces
		checked_file = open("checked.txt", "a")
		checked_proxies.append(unchecked_proxy)





		print(unchecked_proxy + spaces + "[ " + location + ", Request time: "+ str(elapsed_time.total_seconds()) +"  seconds ]")
		checked_file.write(unchecked_proxy + "\n")
		checked_file.close()









	except requests.exceptions.Timeout:
		pass
	except:
		pass

amm_checked = 0 #ammount checked.  amount or ammount????
for unchecked_proxy in proxy_list:
	time.sleep(0.01) #so your computer doesnt crash
	while threading.active_count() >= thread_amm: #limit how many threads run
		time.sleep(1) # if too many give it a second so some finish
	unchecked_proxy = unchecked_proxy.strip()
	proxy_thread = threading.Thread(target=proxy_check, args=(unchecked_proxy,)) #run proxy_check in a thread
	proxy_thread.start()
	proxy_threads.append(proxy_thread)
	amm_checked += 1

	print(f"Progress: {str(amm_checked)}/{str(lines)}",  end='\r') #shows how much proxies were checked
for proxy_thread in proxy_threads:
	proxy_thread.join()


print("Waiting 10 seconds...")
time.sleep(10)
print(str(len(checked_proxies)) + " proxies work.")
