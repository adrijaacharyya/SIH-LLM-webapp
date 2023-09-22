from flask import Flask, render_template, redirect, url_for, request
from models.llmModel import BartModel
import pyttsx3
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    if request.method == 'POST':
        inputText = request.form.get('inputtext')
        bart = BartModel(inputText)
        out = bart.output()
        
        return render_template('submit.html', output = out)
    return render_template('index.html')




@app.route('/submit', methods=['GET', 'POST'])
def submit():
    return render_template('submit.html')
if __name__ == '__main__':
    app.run(debug=True)