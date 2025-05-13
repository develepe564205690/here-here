from flask import Flask
import random
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
   message = "Hello, Flask!"
   return message


@app.route('/hello')
def here():
   page = """
      <h1>Here's a random number: {0}</h1>
      <form>
         <button>New Number</button>
      </form>
   """
   num = random.randint(1, 25)
   return page.format(num)

if __name__ == '__main__':
   app.run()