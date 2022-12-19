# from crypt import methods
from flask import Flask, jsonify,request
import flask
# from  import Resource,Api
import os
import random
from flask_cors import CORS,cross_origin
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
CORS(app)
run_with_ngrok(app)
# api = Api(app)

WordList=[]

# os.chdir(r'C:\Users\HP\Desktop\Web Development Projects.c++\ImproveYourVocaboularyChromeExtension')
file = open('words.txt','r')
# f = open('words.txt','r')

for line in file:
    WordList.append(line.strip())

# print(WordList)

# x = random.choice(WordList)
# print(x)

# api.add_resource(FrequentlyUsedRandomWords,'/Word/<string:word>')

# @app.route('/Word/<string:word>',methods=['GET','POST','DELETE'])
# def FrequentlyUsedRandomWords1(word):
#     if request.method == 'GET':
#         for x in WordList:
#             if x == word:
#                 return jsonify(x)
#         return jsonify({'Data':"404 Not Found error"})
#     if request.method == 'POST':
#         w = {'Data': word}
#         w = request.get_data()
#         WordList.append(w)
#         return jsonify({"message: word has been added"})
#     if request.method == 'DELETE':
#         for idx,x in enumerate(WordList):
#             if x['Data'] == word:
#                 w = WordList.pop(idx)
#                 return {'Data':"Deleted"}


@app.route('/')
@cross_origin()
def get():
    x = random.choice(WordList)
    return jsonify(word=x)
    # return x


if __name__ == '__main__':
    app.run()







#  Here, in this project I have focused only on get requests as my, words.txt is not having data in json format, so, thought, it will take time to convert my data into json format, I could have work on other crud operations as well, but, thought, in my project , there is the need of fixed daily used words. So, havent tried for my api 