# Author: Evren Korkmaz
# This project read the value on DHT11 sensor and send the value to remove server da$

import ipinfo     # locatiom lib
import grovepi    # grove pi shield lib
import smtplib    # stmp mail lib
dht_sensor_port=4 # sensor port D4
dht_sensor_type=0 # sensor type DHT11-> 0 DHT22-> 1
data=open('data.txt','w') #open file for write
[ temp,hum ] = grovepi.dht(dht_sensor_port,dht_sensor_type) # take value with grobep$
                                                            # define the value integ$
print ('Temp: '+ str(temp) + '*C' + '\tHumidity:' + ' %'+ str(hum)) # Print the valu$

# this part for the location information
access_token = '9d363e5856b384'          # token value from ipinfo.io
handler = ipinfo.getHandler(access_token)
ip_address = '185.136.56.2'              # ip addres to this pc
details = handler.getDetails(ip_address) #define the location value on details

location=details.org
location=location.replace(" ", "\ ") # change the white spaceses to \ because influx$

# write the value on data.txt
data.write('temperature,location='+ location + ' temp='+ str(temp))
data.write('\n')
data.write('temperature,location='+ location + ' hum='+ str(hum))


# mail function
def mail(content):
    mail = smtplib.SMTP("smtp.gmail.com",587) 
    mail.starttls()
    mail.login('gozenintern@gmail.com','iskenHub123**')
    mail.sendmail("gozenintern@gmail.com","muhammetkrn19@gmail.com",content)

# alert values
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
