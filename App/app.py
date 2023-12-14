from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv, find_dotenv
import os
from QA import *

load_dotenv(find_dotenv(), override=True)
app = Flask(__name__)
index_name = 'ask-document'
vector_store = insert_of_fetch_embeddings(index_name)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/chat", methods=['POST', 'GET'])
def chat():
    if request.method == "POST":
        question = request.form["question"]
        answer = ask_get_answer(vector_store, question)
        return render_template("chat.html", answer=answer, question=question)
    return render_template("chat.html", answer="")


if __name__ == "__main__":
    app.run(host=os.environ.get("HOST"), debug=True)
    # print("Loading Data..")
    # data = load_from_wikipedia("استراتيجيات للوقاية من مرض القلب", 'ar')
    # print("Chunk Data ..")
    # chunks = chunk_data(data)
    # delete_index("all")
    # index_name = 'ask-document'
    # vector_store = insert_of_fetch_embeddings(index_name)

