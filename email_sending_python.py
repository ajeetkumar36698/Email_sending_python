import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()


server.login("ajeetkumar36697@gmail.com","votn sjtf ubzm mvqi")
a=["ajeetkumar36698@gmail.com"]
for i in range(len(a)):
	server.sendmail("ajeetkumar36697@gmail.com",a[i],"if you get this message please replay any message")
print("email sending")