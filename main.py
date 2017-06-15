from flask import Flask, request
#flask imports a "request" object, which allows us to access the data that the user submits to our server
app = Flask(__name__)
app.config['DEBUG'] = True

#this form is made on the server, it's not a file hosted on my home computer or anything. The server is building it dynamically. form action /hello is telling it to submit the user's input to path "/hello" on our server
form = """
<!DOCTYPE html>
<html>
  <body>
    <form action="/hello" method="POST">
      <label for="first-name">First Name:</label>
      <input id="first-name" type="text" name="first_name" />
      <input type="submit" />
    </form>
  </body>
</html>
"""

@app.route("/")  #using the tools of FLask to specify that this function should recieve requests at the root url (route "/")
def index(): #this function will recieve requests at that root path (request is being handled by index function)
    return form #what this function returns is what the user will see in their browser (what's returned to the user)

@app.route("/hello", methods=['POST']) #this is a handler for the /hello path, handle requests to /hello.
def hello(): #takes data that the user enters into the form, which will be submitted to our server (to the /hello route on our server). This allows us to get the data, and then return a personalized greeting with the input user name
    first_name = request.form['first_name']
    #first_name = request.args.get('first_name') #python parses the data that i'm requesting by variable name, and sets it to the var i've defined here
    return '<h1>Hello, ' + first_name + '</h1>'
app.run()

# 
# To create a form in a Python file, to be returned by a handler function in Flask, use triple-quotes """ to enclose strings that break across lines. This allows us to write large amounts of text (e.g. HTML) within a Python file.
# If this form is a global variable (i.e. it is defined outside of any function) then it can be used by multiple handler functions.
# By default, the action of a form is the same URL that the form is displayed at.
# By default, the method of a form is GET.
# The name attribute of a form element determines the key that will be used to pass the parameter to the server in the HTTP request. Thus, if an element has name='first_name' then the string 'first_name' must be used to access the value of the form element on the server.
