import requests
import threading
import time
import os






#add your links to the list
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

]

print("Gathering SOCKS5 proxies, this will only take a few seconds")

proxy_list = open("socks5.txt" , "a")

#for every line in the list of links, try to open a link and if it works put the content in a file
counter = []
counter_item = 0

for i in socks5:
	counter.append("-")
for line in socks5:
	counter[counter_item] = "+"
	try:
		getproxy = requests.get(line)
		proxy_list.write(getproxy.text)
	except:
		pass
	counter_item += 1
	print(f"Completed: [{''.join(counter)}]", end='\r')
proxy_list.close()
	


os.system("clear")


print("Removing duplicates\n")
os.system("./duplicates.sh")

print("Done fetching proxies. \nNow checking...")
proxy_list = open("socks5.txt" , "r")



line_num = 0



checked_proxies = []

proxy_threads = []

def proxy_check(unchecked_proxy):
	try:
		unc_proxy = {
			"http": "socks5://" + unchecked_proxy,
			"https": "socks5://" + unchecked_proxy 
		}
		
		
		requests.get(
		    'http://detectportal.firefox.com/success.txt',
		    proxies=unc_proxy,
		    timeout=20,
		    
		)

		response = requests.get(
		    'https://google.com',
		    proxies=unc_proxy,
		    timeout=20,
		    
		)
		
		
		if '<title>Google</title>' in response.text:
			checked_proxies.append(unchecked_proxy)
			print(unchecked_proxy)
		else:
			pass
		

	except requests.exceptions.Timeout:
		pass
	except:
		pass
	

for unchecked_proxy in proxy_list:
	time.sleep(0.05)
	unchecked_proxy = unchecked_proxy.strip()
	proxy_thread = threading.Thread(target=proxy_check, args=(unchecked_proxy,))
	proxy_thread.start()
	proxy_threads.append(proxy_thread)

for proxy_thread in proxy_threads:
	proxy_thread.join()


print("Waiting 10 seconds...")
time.sleep(10)
print(str(len(checked_proxies)) + " proxies work.")
