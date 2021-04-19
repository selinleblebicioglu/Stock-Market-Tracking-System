import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mesaj(sinyal):

        message= MIMEMultipart()

        message["From"]= "borsatakipsistemi@gmail.com" #programımız için mail gönderecek bir mail adresi açtık
        message["To"]= "selinlb37@gmail.com" #göndereceğimiz mail adresimiz
        message["Subject"]= "Borsa Takip Sistemi" #mailin konusu

        body= """
        {}
        """.format(sinyal) #mailin içeriği

        body_text= MIMEText(body,"plain")
        message.attach(body_text)

        mail= smtplib.SMTP("smtp.gmail.com",587) #gerekli smtp aayrları
        mail.ehlo()
        mail.starttls()
        mail.login("borsatakipsistemi@gmail.com","123Se456lin") #mailimize bağlanıyoruz
        mail.sendmail(message["From"], message["To"], message.as_string()) #mail gönderme fonksiyonumuz

        print("{} Başarılı bir şekilde gönderildi.".format(sinyal))

        mail.close()
