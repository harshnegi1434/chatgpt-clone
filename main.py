from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai

openai.api_key = "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"

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://harshnegi1434:dFV1pgC7mug6tWbv@gptclone.18xwqt4.mongodb.net/chatgpt"
mongo = PyMongo(app)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    mychats = [chat for chat in chats]
    print(mychats)
    return render_template("index.html", mychats = mychats);

@app.route("/api", methods={"GET", "POST"})
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question":question})
        if chat:
            data = {"result" : f"{chat['answer']}"}
            return jsonify(data)
        else:
            # response = openai.Completion.create(
            #     model="text-davinci-003",
            #     prompt=question,
            #     temperature=1,
            #     max_tokens=256,
            #     top_p=1,
            #     frequency_penalty=0,
            #     presence_penalty=0
            # )
            # data= {{"question": question, "answer": response["choices"][0]["text"]}}
            data= {"result" : f"Answer of {question}"}
            mongo.db.chats.insert_one({"question": question, "answer": f"Answer from OPENAI for {question}"})
            return jsonify(data)
    data = {"result" : "Thank You"}
    return jsonify(data)

app.run(debug=True)