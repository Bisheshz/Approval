import requests

def ipkamu():
    a = requests.get("http://ip-api.com/json/", headers={
                     "Referer": "http://ip-api.com/", "Content-Type": "application/json; charset=utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()

    ip = a.get("query", " ")
    bn = a.get("status", " ")
    ng = a.get("country", " ")
    pr = a.get("regionName", " ")
    sp = a.get("isp", " ")

    print("\nStatus : " + bn)
    print("IP Kamu : " + ip)
    print("Negara : " + ng)
    print("Provinsi : " + pr)
    print("Provider : " + sp)

ipkamu()
