import sys, os, re
#import zipfile
import gzip
import datetime
__author__="yasmin"
__date__ ="$Nov. 8, 2012 11:58:37 AM$"

#Converted to python3 By
#__author__="himarsha"
#__date__ ="$Oct. 26, 2021 10:17:15 AM$"


if __name__ == "__main__":
    count =0
    fh = open(sys.argv[1],'r');
    #fh = open("Z:\\LOGs\\Experiments\\2Feb2012\\samples\\s3.txt",'r');

    ipDict = {}

    w = open(sys.argv[2],'w')

    for line in fh: #zf.read(filename).split("\n"):
        #count= count+1;
        #if count%200000==0:
            #print count
        #            break;
        list = line.split(' ');

        ip= list[0]
        ip = ip.strip()

        if len(list[3])<2:
            continue;
            
        agent = "";
        for i in range(11, len(list)):
            agent = agent +" "+list[i]
        agent = agent[2:-2].lower()

        if ip not in ipDict:
            ipDict[ip] = {agent: [line]}
        else:
            if agent not in ipDict[ip]:
                ipDict[ip][agent] = [line]
            else:
                ipdipaua = ipDict[ip][agent]
                ipdipaua.append(line);
        #break

    #w1 = open(sys.argv[3],'w')

    #w6 = open("Fig6_data",'w')
    #r_count=0
    #0.24.230.1630 - - [02/Feb/2012:07:05:38 +0000] "GET http://web.archive.org/web/*/http://www.winamp.com HTTP/1.1" 302 0 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.25) Gecko/20111212 Firefox/3.6.25 (.NET CLR 3.5.30729)"
    #print(ipDict.keys())
    for ipAdd, val in ipDict.items():
        robot= 0;

        agCount = len(ipDict[ipAdd])
        if agCount >19:
            robot= 1;
            #w1.write(ipAdd+"\t"+agcount+)
        #     r_count=r_count+1
            #print "robot found ==================="
        #uricount = 0;
        for idx, ag  in enumerate(ipDict[ipAdd]):
            #uricount = uricount+len(ipDict[ipAdd][ag]);
           # print uricount
            userSession = 0
            for idv, item in enumerate(ipDict[ipAdd][ag]):

                if robot==1:
                    newitem = item.replace(ipAdd,"x"+ipAdd);
                else:
                    try:
                        list = item.split(' ');
                        if len(list)<12:
                            #w1.write(item)
                            continue;
                            
                        if idv == 0:
                            oldtt = datetime.datetime.strptime( list[3][-8:],"%H:%M:%S");
                        tt =datetime.datetime.strptime( list[3][-8:],"%H:%M:%S");
                        if tt> oldtt:
                            tdelta = tt -oldtt
                        else:
                            tdelta = oldtt-tt

                        if tdelta.seconds > 600:
                #            print ipAdd+str(idx)+"\t"+str(tdelta.seconds)
                 #           print str(tt) +"\t"+ str(oldtt)
                            userSession = userSession+1;
                            
                        oldtt = tt

                        # if robot==1:
                        #     newitem = item.replace(ipAdd,ipAdd+"_"+'x'+str(idx)+"_"+str(userSession));
                        # else:
                        newitem = item.replace(ipAdd,ipAdd+"_"+str(idx)+"_"+str(userSession));
            #                if robot==0:
            #                      print newitem
                    except:
                        continue;

                w.write(newitem);
        #w6.write(ipAdd+"\t"+str(len(ipDict[ipAdd]))+"\t"+str(uricount)+"\n")

    #print("robocount"+str(r_count))

    w.close()
