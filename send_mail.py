import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("kittybankorg@gmail.com","Pkalyanram143$")
server.sendmail("kittybankorg@gmail.com","rampalla2005@gmail.com","Hai ra babu bonnaavaaa")
print("haa mail ochindhi no worries")