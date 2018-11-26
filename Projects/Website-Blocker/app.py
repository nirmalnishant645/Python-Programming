import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts" #Path for host file
redirect = "127.0.0.1" #Host IP
website_list=["www.facebook.com","facebook.com","www.twitter.com","twitter.com","www.instagram.com","instagram.com"] #List of Websites to be blocked

while True: #Infinte Loop
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 13): #Time to block the websites for
        print("Work Work Work Work Work Work")
        with open(hosts_path,'r+') as file: #open Host file for read & write
            content=file.read() #Store content of file in a variable
            for website in website_list: #for loop to check if websites are already blocked
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n") #add blocked websites
    else: #If not in the working hours, unblock sites
        with open(hosts_path, 'r+') as file: #open Host file for read & write
            content=file.readlines()
            file.seek(0) #Place the cursor at starting position
            for line in content:
                if not any(website in line for website in website_list): #print every line of the file that does not have the name of blocked websites
                    file.write(line)
            file.truncate() #delete the contents of the file
        print("Have Fun!")
    time.sleep(5) #Check every 5 seconds
