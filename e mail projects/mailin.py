import smtplib
import ssl
# import getpass

sender="davesarath@gmail.com"
recvr="davesarath@gmail.com"

# pwd=getpass.getpass()

pwd=input("password:")

# print "dadaa"
text='''hai 
how are you
bye'''


# context=ssl.create_default_context()
server=smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender,pwd)
server.sendmail(sender,recvr,text)
