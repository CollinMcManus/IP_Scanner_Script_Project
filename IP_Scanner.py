import requests
def get_info_for_ip(ip):
    # I was able to sign up for a free api service at ipinfo which is free for non-business use
    url = "http://ipinfo.io/" + ip + "/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json() # this is for getting the response
        print("IP address that was scanned:", ip)
        print("Location:", data['loc'])
        print("City:", data['city'])
        print("Region:", data['region'])
    else:
        print("Could not get any results for the IP address:", ip)

ip_to_scan = input("Enter the IP address you would like to scan: ")
get_info_for_ip(ip_to_scan)