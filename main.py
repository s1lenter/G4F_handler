from flask import Flask, jsonify, request, Response
import json
from g4f.client import Client

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/api/hello', methods=['POST'])
def hello():
    messages = request.json

    return Response(
        json.dumps(send_request_to_ai(messages), ensure_ascii=False),
        mimetype='application/json'
    )

def send_request_to_ai(messages):
    client = Client()
    
    response = ""
    while (True):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            web_search=False
        )
        if response.choices[0].message.content[:5] != "Error":
            break
        else:
            print("err")
    return response.choices[0].message.content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
