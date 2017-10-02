from flask import Flask

app=Flask(__name__)

@app_route('/')

def script():
 return "Hi How are you, This is the First Web app"

if __name__=='__main__':
 app.run(port = 5001)

