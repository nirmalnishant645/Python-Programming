'''
Create a new file and name it with the current time
'''
import datetime
filename = datetime.datetime.now()
def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
        file.write("")

create_file()
