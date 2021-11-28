import sys, os, re
#import zipfile
import gzip
import datetime
__author__="yasmin"
__date__ ="$Nov. 8, 2012 11:58:37 AM$"

#Converted to python3 By
#__author__="himarsha"
#__date__ ="$Oct. 26, 2021 10:17:15 AM$"

#To sessionize whole day - By
#__author__="himarsha"
#__date__ ="$Nov. 27, 2021 10:17:15 AM$"

#ipDict
#For each ip
#   ua: line

def calculate_sessions(last_ip,ipDict):    
    robot= 0
    ipAdd = last_ip
    #print(last_ip)    
    agCount = len(ipDict.keys())
    if agCount >19:
        robot= 1
    #print("IP", last_ip)
    #print("Robot", robot)
    #print(ipDict.keys())
    for idx, ag  in enumerate(ipDict):        
        userSession = 0
        #print(idx,ag)
        for idv, item in enumerate(ipDict[ag]):
            #print(idv,item)
            if robot==1:
                newitem = item.replace(ipAdd,"x"+ipAdd)
            else:
                try:
                    list = item.split(' ')
                    if len(list)<12:
                        #w1.write(item)
                        continue
                        
                    if idv == 0:
                        oldtt = datetime.datetime.strptime( list[3][-8:],"%H:%M:%S")
                    tt =datetime.datetime.strptime( list[3][-8:],"%H:%M:%S")
                    if tt> oldtt:
                        tdelta = tt -oldtt
                    else:
                        tdelta = oldtt-tt

                    if tdelta.seconds > 600:
            #            print ipAdd+str(idx)+"\t"+str(tdelta.seconds)
             #           print str(tt) +"\t"+ str(oldtt)
                        userSession = userSession+1
                        
                    oldtt = tt

                    # if robot==1:
                    #     newitem = item.replace(ipAdd,ipAdd+"_"+'x'+str(idx)+"_"+str(userSession));
                    # else:
                    newitem = item.replace(ipAdd,ipAdd+"_"+str(idx)+"_"+str(userSession))
        #                if robot==0:
        #                      print newitem
                except:
                    continue

            w.write(newitem);
    #print("\n")


if __name__ == "__main__":
    fh = open(sys.argv[1],'r')
    lines = fh.readlines()
    last_line = len(lines)

    w = open(sys.argv[2],'w')   

    ipDict = {}

    last_ip = 0
    count = 1

    for line in lines: 
        list = line.split(' ');

        this_ip = list[0]
        this_ip = this_ip.strip()
        #print(this_ip)
        
        # if len(list[3])<2:
        #     continue;

        agent = "";
        for i in range(11, len(list)):
            agent = agent +" "+list[i]
        agent = agent[2:-2].lower()

        if last_ip == this_ip:
            is_newIP = False
            #print("A")
        else:
            is_newIP = True
            #print("B")

        #print(ipDict.keys())

        if not is_newIP:
            #print("Same IP")
            #Not a new IP - same session
            #save things in dictionairy (adding)
            #ipDict[agent] = [line]
            if agent not in ipDict.keys():
                ipDict[agent] = [line]
            else:
                ipdipaua = ipDict[agent]
                ipdipaua.append(line)


        if is_newIP:  
            #print("new IP")
            #New ip - new session         
            #check if there is a dict then process the dictionairy           
            if ipDict:
                #print("Next IP")    
                #dictionary is NOT empty
                #print(ipDict["IP"])
                #process the dictionary - calculate sessions    
                calculate_sessions(last_ip,ipDict)
                #break
                #then create new dictionairy(initialize+plus that line)  
                ipDict = {}
                #ipDict["IP"] = this_ip
                ipDict[agent] = [line]
                #print(ipDict["IP"])
            else:
                #print("First run")  
                #dictionary is empty
                #first run
                #ipDict["IP"] = this_ip                
                #print(ipDict["IP"])   
                ipDict[agent] = [line]
                #print(ipDict.keys())

        if count == last_line:
            #print("EOF")  
            calculate_sessions(last_ip,ipDict)
            
        last_ip = this_ip 
        print(count)
        count = count + 1 
        #break
    #print(len(ipDict))   
    #print(len(ipDict.keys())) 
    w.close()