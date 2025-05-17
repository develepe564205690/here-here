from flask import Flask, render_template, request, redirect, url_for, flash
import random



app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'your-secret-key-here'  # Required for flash messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        color = request.form.get('color', '').strip()
        luck_num = request.form.get('luck_num', '').strip()
        fav_class = request.form.get('fav_class', '').strip()
        best_pix = request.form.get('best_pix', '').strip()
        
        # Validate required fields
        if not all([color, luck_num, fav_class, best_pix]):
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))
        
        # Validate lucky number is a valid integer
        try:
            luck_num = int(luck_num)
            if not (1 <= luck_num <= 100):
                flash('Lucky number must be between 1 and 100!', 'error')
                return redirect(url_for('index'))
        except ValueError:
            flash('Lucky number must be a valid number!', 'error')
            return redirect(url_for('index'))
        
        # If all validation passes, redirect to results
        return redirect(url_for('results', color=color, luck_num=luck_num, 
                              fav_class=fav_class, best_pix=best_pix))
    
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

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        # Handle direct form submission
        color = request.form.get('color', '').strip()
        luck_num = request.form.get('luck_num', '').strip()
        fav_class = request.form.get('fav_class', '').strip()
        best_pix = request.form.get('best_pix', '').strip()
    else:
        # Handle redirect from index
        color = request.args.get('color', '')
        luck_num = request.args.get('luck_num', '')
        fav_class = request.args.get('fav_class', '')
        best_pix = request.args.get('best_pix', '')
    
    # Additional validation check
    if not all([color, luck_num, fav_class, best_pix]):
        flash('Invalid form submission!', 'error')
        return redirect(url_for('index'))
    
    return f"Your favorites - Color: {color}, Lucky Number: {luck_num}, Class: {fav_class}, Pixar Movie: {best_pix}"

if __name__ == '__main__':
   app.run()