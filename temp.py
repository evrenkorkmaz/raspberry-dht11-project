import ipinfo
import grovepi
import time
import smtplib
dht_sensor_port=4
dht_sensor_type=0
import time
import re
data=open('data.txt','w')
[ temp,hum ] = grovepi.dht(dht_sensor_port,dht_sensor_type)
print ('Temp: '+ str(temp) + '*C' + '\tHumidity:' + ' %'+ str(hum) + ' ' + str(time.strftime("%s",time.gmtime())))

access_token = '9d363e5856b384'
handler = ipinfo.getHandler(access_token)
ip_address = '185.136.56.2'
details = handler.getDetails(ip_address)

print details.org
location=details.org
location=location.replace(" ", "\ ")
print location


data.write('temperature,location='+ location + ' temp='+ str(temp))
data.write('\n')
data.write('temperature,location='+ location + ' hum='+ str(hum))



def mail(content):
    mail = smtplib.SMTP("smtp.gmail.com",587) 
    mail.starttls()
    mail.login('gozenintern@gmail.com','iskenHub123**')
    mail.sendmail("gozenintern@gmail.com","muhammetkrn19@gmail.com",content)


if temp>=21.0: 
    content = 'Oda sicakligi ' + str(temp) + '*C' + ' Sicaklik yuksek!'
    mail(content)
elif temp<=15:
    content = 'Oda sicakligi ' + str(temp) + '*C' + ' Sicakligi artirmaniz onerilir.'
    mail(content)
elif hum >=35:
    content = 'Odadaki nem orani  %' +  str(hum)  + ' Nem orani cok yuksek!'
    mail(content)
elif hum <=15:
    content = 'Odadaki nem orani  %' +  str(hum)  + ' Nem orani cok dusuk!'
    mail(content)
