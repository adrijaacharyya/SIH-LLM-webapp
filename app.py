from flask import Flask, render_template, redirect, url_for, request
from models.llmModel import BartModel
from models.grammar import grammar
from models.scibert import scimodel
from models.t5model import t5model
import json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    if request.method == 'POST':
        inputText = request.form.get('inputtext')
        if modelName == 'news':
            mod = BartModel(inputText)
        elif modelName == 'science':
            mod = scimodel(inputText)
        elif modelName == 'misc':
            mod = t5model(inputText)
        else:
            mod = grammar(inputText)
        out = mod.output()
        return render_template('submit.html', output = out)
    return render_template('index.html')




@app.route('/submit', methods=['GET', 'POST'])
def submit():
    return render_template('submit.html')


@app.route('/ProcessModel/<string:model>', methods=['POST'])
def ProcessModel(model):
    global modelName 
    modelName = json.loads(model)
    print(modelName)
    return('/')
if __name__ == '__main__':
    app.run(debug=True)

