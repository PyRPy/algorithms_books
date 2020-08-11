from flask import Flask 

def search4letters(phrase: str, letters: str='aeiou') -> set:
    """ returns the set of 'letters' found in 'phrase'.""" 
    return set(letters).intersection(set(phrase)) 

app = Flask(__name__) 

@app.route('/') 
def hello() -> str:
    return 'hello world from Flask!' 

@app.route('/seach4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru'))

app.run() 
