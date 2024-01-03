from flask import Flask, render_template,request
import requests


app = Flask(__name__)


@app.route('/', methods= ['POST','GET'])
def hello():
    if request.method =="GET":
        return render_template('index.html')
    else:        
        user_msg= request.form['msg']
        content = request.form['chat_content']
        # #send to rasa
        r = requests.post("http://127.0.0.1:5005/webhooks/rest/webhook", json={"sender":"test", "message": user_msg})
        # print("response is: " + str(r.json()))
        ##JSON: [{'recipient_id': 'test', 'text': 'Bye'}]
        content += "\n [YOU]:" + user_msg
        content += "\n [BOT]:" + r.json()[0]["text"]

        print(content) 
        return render_template('index.html', updatedcontent =content)
    

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 8080)