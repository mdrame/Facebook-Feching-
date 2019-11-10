from flask import Flask, render_template



app = Flask(__name__)


# home route 
@app.route('')
def index():

    return render_template('index.html')
    










# main module page 
if __name__ == "__main__":
    app.run(debug=True)
