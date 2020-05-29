import requests as r
import socket


domains = ["finlaw.kz", "energyproject.kz", "kolgotka.kz", "law-protection.kz", "groof.kz", "goldenroof.org", "akun.dev", "focuskeeper.app", "shi.pper.men"]
protocols = ["http://", "https://"]
prefixes = ["", "www."]

test_cases = {}
for domain in domains:
    for protocol in protocols:
        for prefix in prefixes:
            url = "".join([protocol,prefix, domain])
            test_cases[url] = 0
            
            
def make_calls(test_cases):

    for key in test_cases.keys():
        try:
            res = r.get(key, verify=True)
        except:
            test_cases[key] = {"Error": "Time out"}
            
        test_cases[key] = {
                "Status Code": res.status_code,
                "Server": res.headers["Server"],
                }
    return test_cases
    

error = []
for key, value in test_cases.items():
    if value["Status Code"] != 200:
        print(key, value)

domains_look_up = []
for domain in domains:
    for prefix in prefixes:
        domains_look_up.append("".join([prefix, domain]))
        
dns_list = []
for domain_pref in domains_look_up:
    addr1 = socket.gethostbyname(domain_pref)
    dns_list.append((domain_pref, addr1))
    
    
for a in dns_list:
    print(a)
   
   
   
   


