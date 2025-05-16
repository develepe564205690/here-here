from flask import Flask, render_template, request
import random



app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("favorite_template.html")

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    try:
        values = {
            'name': request.form.get('name', 'Friend'),
            'gift': request.form.get('gift', 'present'),
            'verb': request.form.get('verb', 'playing'),
            'noun': request.form.get('noun', 'person'),
            'closing_word': request.form.get('closing_word', 'Sincerely'),
            'author': request.form.get('author', 'Me')
        }
        return render_template("tynote.html", **values)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/hello')
def hello():
   message = "Hello, Flask!"
   return message


@app.route('/rand')
def here():
   page = """
      <h1>Here's a random number: {0}</h1>
      <form>
         <button>New Number</button>
      </form>
   """
   num = random.randint(1, 25)
   return page.format(num)

@app.route('/results', methods=['POST'])
def results():
    color = request.form.get('color', '')
    luck_num = request.form.get('luck_num', '')
    fav_class = request.form.get('fav_class', '')
    best_pix = request.form.get('best_pix', '')
    return f"Your favorites - Color: {color}, Lucky Number: {luck_num}, Class: {fav_class}, Pixar Movie: {best_pix}"

if __name__ == '__main__':
   app.run()