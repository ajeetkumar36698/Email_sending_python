import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()


server.login("email","votn sjtf ubzm mvqi")


server.sendmail("email",'sending email',"if you get this message please replay any message")
print("email sending")
