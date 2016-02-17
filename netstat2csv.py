'''
Function: Netstat to csv to easily see and manipulate connections on your computer
Priviledges Needed: Sudo to run the netstat (in order to see all connections), along with priveledges to output a temporary file in the directory this program is ran
Output: Csv of netstat -pla
'''

import subprocess

#Netstat to generate the file
subprocess.run("netstat -pla > ./tempConnections", shell=True)

#Set up csv file
netstatCon = open("netstatConnections.csv", "w")

#now to read the file
tempCon = open("./tempConnections", "r")
# This get rid of a static line
tempCon.readline()

#Start processing of each line to break it down for the csv file
for line in tempCon:
	if line == "Active UNIX domain sockets (servers and established)\n":
    break
	bufferSeg = line.split()
	netstatCon.write(', '.join(bufferSeg))
	netstatCon.write('\n')


#close and delete temp file
netstatCon.close()
tempCon.close()
tempDel = open("./tempConnections", "w")
tempDel.write("n\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn")
tempDel.close()
subprocess.run("rm ./tempConnections", shell=True)
