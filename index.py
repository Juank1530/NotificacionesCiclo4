from flask import Flask, request
import json
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#Here we create a flask object
app = Flask(__name__)
 
#Here we loaded our file configuration config.json
f = open("config.json", "r")
env = json.loads(f.read())

#Here we create our first web service
@app.route('/', methods=['GET'])
def test():
    return "Hello word"


@app.route('/send_sms', methods=['POST'])
def send_sms():
    try:
        account_sid = env['TWILIO_ACCOUNT_SID']
        auth_token = env['TWILIO_AUTH_TOKEN']
        origin = env['TWILIO_PHONE_NUMBER']
        client = Client(account_sid, auth_token)
        data = request.json
        content = data["content"]
        destiny = data["destiny"]
       
        message = client.messages.create(
                            body=content,
                            from_=origin,
                            to='+57' + destiny
                        )
        print(message)
        return "send success"
    except Exception as e:
        print(e)
        return "error"


@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    content = data["content"]
    destiny = data["destiny"]
    subject = data["subject"]
    print(content, destiny, subject)
    message = Mail(
    from_email= env['SENDGRID_FROM_EMAIL'],
    to_emails= destiny,
    subject= subject,
    html_content= content)
    try:
        sg = SendGridAPIClient(env['SENDGRID_API_KEY'])
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return "send success"
    except Exception as e:
        print(e)
        return "error"



#Here we execute the server on port 5000 to can use the webs service
if __name__ == '__main__':
    app.run()