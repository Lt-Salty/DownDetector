#Import time to allow you to sleep the script, urllib to load the site, subprocess will allow you to run a process on the machine outside of the script (in this instance it's send mail) 
import time
from urllib.request import urlopen
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
counter = 0
fails = 0
WebsiteName = 'testsite'
url = 'http://www.testsite.com/'
SMTPserver = 'secure.emailsrvr.com:587'
login = 'text@testserver.com'
password = 'testpass!'
FromEmail = 'test@testserver.com'
ToEmail = 'recipient@testserver.com'
def send_alert():
    from smtplib import SMTP
    from email.mime.text import MIMEText

    msg = MIMEText(testsite' is down')
    msg['Subject'] = testsite' IS UNREACHABLE'
    msg['From'] = FromEmail
    msg['To'] = ToEmail

    server = SMTP(SMTPserver)
    server.ehlo()
    server.starttls()
    server.login(login, password)
    server.sendmail(FromEmail, [ToEmail], msg.as_string())
    server.quit()



#This loops while the script is running.
# It gets the status returned from the urllib call, if it's not 200 it will email the email contents above.  
while True:
    try:
        urlopen(url)
        counter = counter+1
        if fails == 0:print ("OK",counter,)
        if fails > 0: print ("OK",counter,"  ---   FAILURES=",fails) 
    except:
        send_alert()
        fails = fails+1
        print ("FAILURE",fails)
        time.sleep(270)
    #The number of seconds the loop will pause for before checking again.  I set it to 60. 
    time.sleep(30)
