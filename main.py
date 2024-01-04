import os
from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
# from bardapi import Bard
# from bardapi import BardCookies
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')
client = OpenAI(api_key=token)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://harshnegi1434:6jtJRfySD5xrnMt4@projects.0rrxqmw.mongodb.net/GPTClone"
mongo = PyMongo(app)
# load_dotenv()

# token = os.getenv('token')
# bard = Bard(token=token)
# bard = BardCookies(cookie_dict=cookie_dict)

collection = mongo.db.chats

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    mychats = [chat for chat in chats]
    #print(mychats)
    return render_template("index.html", mychats = mychats);

@app.route('/get_chat/<question>')
def get_chat(question):
    chat = collection.find_one({'question': question})
    if chat:
        return jsonify({
            'question': chat['question'],
            'answer': chat['answer']
        })
    else:
        return jsonify({'error': 'Chat not found'})

@app.route('/fetch_chat', methods=['POST'])
def fetch_chat():
    data = request.get_json()
    question = data['question']
    response = get_chat(question)
    return response

@app.route('/delete_chat', methods=['POST'])
def delete_chat():
    question = request.json['question']
    collection.delete_one({'question': question})
    return jsonify({'message': 'Chat deleted successfully'})

@app.route("/api", methods={"GET", "POST"})
def qa():
    if request.method == "POST":
        #print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question":question})
        if chat:
            data = {"question": question, "answer":  f"{chat['answer']}"}
            return jsonify(data)
        else:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                      "role": "user",
                      "content": question
                    }
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            #print (answer)
            data = {"question": question, "answer": response.choices[0].message.content}
            mongo.db.chats.insert_one({"question": question, "answer":  response.choices[0].message.content})
            return jsonify(data)
    data = {"result" : "Thank You"}
    return jsonify(data)

app.run(debug=True, host='0.0.0.0', port=5000)
