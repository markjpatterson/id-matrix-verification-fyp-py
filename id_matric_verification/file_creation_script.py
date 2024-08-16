import time


def save_to_file(file_path):
    with open(file_path, "a") as file:
        file.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

file_path = "live-file.txt"

while True:
    file = open (file_path,"r")

    file.close

    file = open ("LIVE_FILE.txt","r")
    f = file.readlines()

    newlist = []
    for line in f:
        newlist.append(line.strip())

    file.close

    file = open("test.txt","a")

    file.write(newlist[-1] + "\n")

    file.close
    #Save the updated content to the file
    save_to_file(file_path)

    #Wait for some time before the next save (example: 10 seconds)
    time.sleep(10)






#file = open ("LIVE_FILE.txt","r")

#file.close

#file = open ("LIVE_FILE.txt","r")
#f = file.readlines()

#newlist = []
#for line in f:
    #newlist.append(line.strip())

#file.close

#print(newlist)




#file = open("test.txt","a")

#file.write(newlist[-1])

#file.close
