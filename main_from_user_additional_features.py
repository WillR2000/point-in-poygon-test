from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from functions import classify_point_experiment
import smtplib
from plotter import Plotter






def email():
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login('additional_feature@outlook.com', 'Isntthiscool')

    mail = str(input('Would you like the results to your inbox? [y/n]'))

    if mail != 'y' and mail != 'n':
        raise Exception('Error: Please state "y" for yes, or "n" for no')

    if mail == 'y':
        address = str(input('Please enter your email: '))

    if mail == 'n':
        classify_point_experiment()

    if mail == 'y':
        msg = MIMEMultipart()

        msg['From'] = 'additional_feature@outlook.com'
        msg['To'] = address
        msg['Subject'] = "Your point is..."

        msg.attach(MIMEText(classify_point_experiment()))

        s.send_message(msg)

def main():
    plotter = Plotter()
    print(email())

    plotter.show()


if __name__ == '__main__':
    main()


