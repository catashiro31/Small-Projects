from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<word>')
def api(word):
    df = pd.read_csv('dictionary.csv', sep=',')
    if word in df['word'].values:
        definition = df[df['word'] == word]['definition'].squeeze()
        result_dict = {'definition' : definition,
                       'word' : word}
        return result_dict
    else:
        return "404 NOT FOUND"

if __name__ == '__main__':
    app.run(debug=True, port=5001)