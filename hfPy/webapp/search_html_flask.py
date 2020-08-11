from flask import Flask, render_template, request

def search4letters(phrase: str, letters: str='aeiou') -> set:
    """ returns the set of 'letters' found in 'phrase'.""" 
    return set(letters).intersection(set(phrase)) 

app = Flask(__name__) 

@app.route('/') 
def hello() -> str:
    return 'hello world from Flask!' 

@app.route('/search4', methods = ['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(search4letters(phrase, letters))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title = 'welcome to search4letter on the web!')

app.run(debug=True) 
