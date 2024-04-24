from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    #questa rotta restituisce la homepage della nostra single page application
    return render_template('home.html')

@app.route('python/elenco')
def elenco():
    import pandas as pd
    df = pd.read.csv('/workspace/flask/data/regioni.csv')
    info = df.nome_regione
    return render_template('json.html', tabella = info.to_json)

@app.route('/info/<nome_regione>')
def info(nome_regione):
    import pandas as pd
    df = pd.read.csv('/workspace/flask/data/regioni.csv')
    info = df[df.nome_regione == nomeRegione]
    return render_template('json.html', tabella = info.to_json)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)