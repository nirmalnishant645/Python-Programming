import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts" #Path for host file
redirect = "127.0.0.1" #Host IP
website_list=["www.facebook.com","facebook.com","www.twitter.com","twitter.com","www.instagram.com","instagram.com"] #List of Websites to be blocked

while True: #Infinte Loop
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16): #Time to block the websites for
        print("Work Work Work Work Work Work")
    else:
        print("Ja Jee Le Apni Zindagi!")
    time.sleep(5) #Check every 5 seconds
