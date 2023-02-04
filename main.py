import smtplib
print("hi")
my_email="mail@gmail.com"
password=""
#here we have to provide the gmail service provider in case of gmail, smtp.gmail.com, For Hotmail it's "smtp.live.com
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
#the above line would provide encryption while sending the mail.
#main thing is we have to turn on two step verification in gmail after that we have to create new app password and have to use it.
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="example@gmail.com",msg="subject:Hello\n\nuyuhwakhjk")
connection.close()
