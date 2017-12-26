import saham.saham
from flask import request, Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/price", methods=['POST']) 
def price():
    saham_label = str(request.form.get('saham_label'))
    days = int(request.form.get('days'))

    return saham.predict_tomorrow_price(saham_label, days)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()