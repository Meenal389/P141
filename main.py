from flask import Flask,jsonify,request
import csv

with open("articles.csv") as a:
    reader= csv.reader(a)
    data= list(reader)
    all_articles=data[1:]

liked_articles=[]
unliked_articles=[]

app= Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        data:all_articles[0],
        "status":"success"
    })

@app.route("/liked-article",methods=["POST"])
def liked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unliked-article",methods=["POST"])
def unliked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    unliked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

    
if __name__ == "__main__":
    app.run()
