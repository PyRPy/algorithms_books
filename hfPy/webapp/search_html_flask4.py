from flask import Flask, render_template, request

def search4letters(phrase: str, letters: str='aeiou') -> set:
    """ returns the set of 'letters' found in 'phrase'.""" 
    return set(letters).intersection(set(phrase)) 

app = Flask(__name__) 

# @app.route('/') 
# def hello() -> '302':
#     return redirect('/entry')

@app.route('/search4', methods = ['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'here are your results: '
    results = str(search4letters(phrase, letters))
    return render_template('results.html', the_phrase = phrase, 
                            the_letters = letters,
                            the_title = title,
                            the_results = results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title = 'welcome to search4letter on the web!')


if __name__ == '__main__':
    app.run(debug=True) 