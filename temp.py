# Author: Evren Korkmaz
# This project read the value on DHT11 sensor and send the value to remove server database.

import ipinfo     # locatiom lib
import grovepi    # grove pi shield lib
import smtplib    # stmp mail lib
# grovepi.dht
dht_sensor_port=4 # sensor port "D4". Check with "sudo i2cdetect -y 1" command
dht_sensor_type=0 # sensor type DHT11-> 0 DHT22-> 1

# ipinfo.io
# create a user on ipinfo.io for location information
# when sign in ipinfo take a access token for your user.
access_token = '12345678987654'
ip_address = 'xx.xx.xx.xx' #your local ip

# smtp
# this program send a mail for some temp or hum value
# Because of first define a sender and destination mail information
sender_mail='sender-mail@gmail.com'
sender_mail_passwd='sender-passwd'
destination_mail='dest-mail@gmail.com'

#alarm
# define a max and min values
max_temp=25
min_temp=15
max_hum=35
min_hum=15

#open file for write
data=open('data.txt','w')

# take value with grobepi.dht function
# define the value integer temp and hum
[ temp,hum ] = grovepi.dht(dht_sensor_port,dht_sensor_type)

# Print the value for informing the user
print ('Temp: '+ str(temp) + '*C' + '\tHumidity:' + ' %'+ str(hum) + ' ' + str(time.strftime("%s",time.gmtime())))

# ipinfo.io
# This part take the location information.
handler = ipinfo.getHandler(access_token)
details = handler.getDetails(ip_address)
location=details.org
# Influxdb insert syntax too complicated
# When add a space on the location, influxdb take a different value any word
# change the white spaceses to \ because influxdb data type
location=location.replace(" ", "\ ")

# write the value on data.txt
data.write('temperature,location='+ location + ' temp='+ str(temp))
data.write('\n')
data.write('temperature,location='+ location + ' hum='+ str(hum))


# mail function
def mail(msg):
    mail = smtplib.SMTP("smtp.gmail.com",587) 
    mail.starttls()
    mail.login(sender_mail,sender_mail_passwd)
    mail.sendmail(sender_mail,destination_mail,msg)


# alert values
if temp>=max_temp:
    msg = 'Room temperature ' + str(temp) + '*C' + ' Too Hot!'
    mail(msg)
elif temp<=min_temp:
    msg = 'Room temperature ' + str(temp) + '*C' + ' Too Cold!'
    mail(msg)
elif hum >=max_hum:
    msg = 'Room humidity  %' +  str(hum)  + ' Too High!'
    mail(msg)
elif hum <=min_hum:
    msg = 'Room humidity  %' +  str(hum)  + ' Too Low!'
    mail(msg)

