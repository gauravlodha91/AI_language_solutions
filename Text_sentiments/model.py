from flask import Flask,render_template,request
import util as p




app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    first_name = request.form.get("document_text")
    inputt = [first_name]
    dictt = p.res1(inputt)
    # dictt = {"Text" : first_name , "confidence_score" : 0.9, "sentiment": "positive" }
    return render_template("result.html", value=dictt) 



if __name__ == '__main__':
    app.run(debug=True)