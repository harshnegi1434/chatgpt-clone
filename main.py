from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from bardapi import Bard

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://harshnegi1434:6jtJRfySD5xrnMt4@projects.0rrxqmw.mongodb.net/GPTClone"
mongo = PyMongo(app)

token = 'XAiB_aiN9bJ_U4pGJTWcwwTlPnhJLt6A_enGufQV9o0q0H13Z6YRuMlRZCP1nN_HW9_ZaA.'
bard = Bard(token=token)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    mychats = [chat for chat in chats]
    #print(mychats)
    return render_template("index.html", mychats = mychats);

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
            answer = bard.get_answer(question)['content']
            #print (answer)
            data= {"question": question, "answer": answer}
            mongo.db.chats.insert_one({"question": question, "answer": answer})
            return jsonify(data)
    data = {"result" : "Thank You"}
    return jsonify(data)

app.run(debug=True)