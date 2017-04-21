import datetime
import smtplib

class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body):
        ''' This must be removed '''
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.email,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            self.email,
            headers + "\r\n\r\n" + body)
gm = Gmail('your_gmail@gmail.com', 'your_password')

while(True):
  dateSTR = datetime.datetime.now().strftime("%H:%M:%S" )
  if dateSTR == ("10:00:00"):
       print(dateSTR)
       try:
           gm.send_message('Drink Water!', 'Please!')
           print "Successfully sent email"
       except:
           print "Error: unable to send email"
  if dateSTR == ("11:00:00"):
      # do function
      print(dateSTR)
      try:
          # server.sendmail("mylotarg1989@gmail.com", "mylotarg1989@gmail.com", message)
          gm.send_message('Drink Water!', 'Please!')
          print "Successfully sent email"
      except:
          print "Error: unable to send email"
  if dateSTR == ("12:00:00"):
      # do function
      print(dateSTR)
      try:
          # server.sendmail("mylotarg1989@gmail.com", "mylotarg1989@gmail.com", message)
          gm.send_message('Drink Water!', 'Please!')
          print "Successfully sent email"
      except:
          print "Error: unable to send email"
  if dateSTR == ("14:00:00"):
      # do function
      print(dateSTR)
      try:
          # server.sendmail("mylotarg1989@gmail.com", "mylotarg1989@gmail.com", message)
          gm.send_message('Drink Water!', 'Please!')
          print "Successfully sent email"
      except:
          print "Error: unable to send email"
  if dateSTR == ("15:00:00"):
      # do function
      print(dateSTR)
      try:
          # server.sendmail("mylotarg1989@gmail.com", "mylotarg1989@gmail.com", message)
          gm.send_message('Drink Water!', 'Please!')
          print "Successfully sent email"
      except:
          print "Error: unable to send email"
  if dateSTR == ("16:00:00"):
      # do function
      print(dateSTR)
      try:
          # server.sendmail("mylotarg1989@gmail.com", "mylotarg1989@gmail.com", message)
          gm.send_message('Drink Water!', 'Please!')
          print "Successfully sent email"
      except:
          print "Error: unable to send email"
  if dateSTR == ("20:00:00"):
      # do function
      print(dateSTR)
      try:
          # server.sendmail("mylotarg1989@gmail.com", "mylotarg1989@gmail.com", message)
          gm.send_message('Drink Water!', 'Please!')
          print "Successfully sent email"
      except:
          print "Error: unable to send email"
  if dateSTR == ("21:00:00"):
      # do function
      print(dateSTR)
      try:
          # server.sendmail("mylotarg1989@gmail.com", "mylotarg1989@gmail.com", message)
          gm.send_message('Drink Water!', 'Please!')
          print "Successfully sent email"
      except:
          print "Error: unable to send email"