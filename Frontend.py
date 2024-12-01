from flask import Flask, render_template, request, flash, redirect
import Formatter
import os
import DatabaseHandler

app = Flask(__name__, template_folder="./templates")
app.config['UPLOAD_FOLDER'] = "./static/image"
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cards/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('create.html')
    elif request.method == "POST":

        if len(request.files) == 0:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        title = formatter.leetify(request.form['title'])
        rec = formatter.leetify(request.form['receiver'])
        sender = formatter.leetify(request.form['sender'])
        content = formatter.leetify(request.form['content'])


        # Insert the new card into the database
        DB.execute_query("INSERT INTO cards (title, receiver, sender, content, image) VALUES (?, ?, ?, ?, ?)",
                  (title, rec, sender, content, filename))

        return redirect('/cards')

@app.route('/cards')
def cards():
    cards = DB.fetch_all("SELECT * FROM cards")
    
    cards_dict = []
    for card in cards:
        card_dict = {
            'id': card[0],
            'title': card[1],
            'receiver': card[2],
            'sender': card[3],
            'content': card[4],
            'image': card[5],
            'image_url': os.path.join('image/', card[5])
        }
        cards_dict.append(card_dict)

    cards = cards_dict
    
    return render_template('cards.html', cards=cards)

if __name__ == '__main__':
    DB = DatabaseHandler.DatabaseHandler("database.db")
    formatter = Formatter.Formatter()
    DB.connect()
    DB.setup_tables()
    app.run(debug=True)