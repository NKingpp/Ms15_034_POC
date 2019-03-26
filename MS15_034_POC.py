import requests

def is_iis(url):
    if "http" or "https" in url:
        domain = url
        rq = requests.get(str(domain))
        rqs = rq.headers["server"]
        if "Microsoft-IIS" in rqs:
            print ("server is Microsoft-IIS ")

        else:
            print ("server is " +rqs)
    else:
        print ("url erro")
def ms15_034(domain):
    headers={'Host': 'stuff',
             'Range': 'bytes = 0 - 18446744073709551615'
    }
    req = requests.get(str(domain),headers=headers)
    if "Requested Range Not Satisfiable" in req:
        print ("detected ms15_034"+domain)
        fopen = open("url_detected","a")
        fopen.write(str(domain))
        fopen.close()
    elif "The request has an invalid header name" in req:
        print ("ms15_034 has been fixed")
    else:
        print("Not detected")
if __name__ == '__main__':
    fopen = open("url.txt","r")
    alllines = fopen.readlines()
    for eachline in alllines:
        eachline = eachline.strip("/n")
        eachline = eachline.strip(" ")
        is_iis(eachline)
