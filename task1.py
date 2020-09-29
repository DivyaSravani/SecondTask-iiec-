#!/usr/bin/python3

print("content-type: text/html")
print()


import subprocess as sp
#import speech_recognition as sr
import cgi




yo = cgi.FieldStorage()

#yo1 = yo.getvalue("username")
#yo2 = yo.getvalue("password")
#yo3 = yo.getvalue("email")
yo4 = yo.getvalue("name1")
yo5 = yo.getvalue("firstname")
yo6 = yo.getvalue("version")
#yo7 = yo.getvalue("mic")

print(yo4+" "+yo5+" "+yo6+" ")



"""if(True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("mic onn...")
        audio=r.listen(source)
        print("mic off...")
    data = r.recognize_google(audio)
    print(data)

else:
    print("MIC is OFF")
"""
cmd = "sudo docker run -dit --name {0} {1}:{2}".format(yo4, yo5, yo6)

output = sp.getstatusoutput(cmd)
status = output[0]
out = output[1]
if(status == 0):
    print("OS launched {}".format(yo4))
else:
    print("some error : {}".format(out))


"""else:
     
	cmd=" sudo docker run -dit --name {} {}:{}".format(yo4,y05,yo6)
	output=subprocess.getstatusoutput(cmd)
	status =output[0]
	out=output[1]
	if(status==0):
	    print("OS launched {}".format(yo4))
	else:
	    print("some error :{}"format.(out) 

"""
