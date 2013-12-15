import os
import requests
import simplejson as json

from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello():
  
  hello ="hello"
  print hellohea 
  return "Hello world from Sreeprasad !"

@app.route('/mytwilio', methods=['GET'])
def helloagain():
	return "this is new hello !"

@app.route('/twilio', methods=['GET'])
def convert_text_to_comment():
   
  #Get the text message sent by Twilio
  message = "this is test"
  print "message"
  #Set up the comment to send to box
  box_comment = {'message' : message}
  #build the request to send to box
  url = "https://api.box.com/2.0/files/12184423458/comments"
  print url
  headers = {'Authorization' : 'Bearer DD59aunIHmrTT2rYKQQB3Q9ikeVWlEv0'}
  print headers
  #send the request
  r = requests.post(url, data=json.dumps(box_comment), headers=headers)
  return r.text

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)