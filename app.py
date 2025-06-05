from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

# Replace with your Twilio credentials
account_sid = 'YOUR_TWILIO_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_number = '+1XXXXXXXXXX'  # Your Twilio number
from_number = '+1YYYYYYYYYY'    # Your staff/clinic callback number

client = Client(account_sid, auth_token)

@app.route('/call', methods=['GET'])
def call():
    to_number = request.args.get('to')
    call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        url='https://twilio-click2call.onrender.com/twiml'
    )
    return f"Calling {to_number}"

@app.route('/twiml', methods=['POST'])
def twiml():
    return '''
        <Response>
            <Say voice="alice">This is My NuRx Pharmacy calling you back.</Say>
        </Response>
    '''

if __name__ == "__main__":
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
