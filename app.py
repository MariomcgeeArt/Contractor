from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Sketch_Book
sketchbooks = db.sketchbooks


app = Flask(__name__)

@app.route('/')
def sketch_books_index():
    """Return homepage."""
    return render_template('sketch_books_index.html', sketchbooks=sketchbooks.find())

@app.route('/sketchbooks/new')
def sketchbooks_new():
    """Create a new sketchbook."""
    return render_template('sketchbooks_new.html')
    
@app.route('/sketchbooks', methods=['POST'])
def sketchbooks_submit():
    """Submit a new sketchbook."""
    sketchbook = {
        'brand': request.form.get('brand'),
        'size': request.form.get('size'),
        'image': request.form.get('image'),
        'price': request.form.get('price')
    }
    sketchbooks.insert_one(sketchbook)
    #print(request.form.to_dict())
    return redirect(url_for('sketch_books_index'))




























if __name__ == '__main__':
    app.run(debug=True)