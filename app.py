from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # loads MONGO_URI from .env

app = Flask(__name__)

print("Feature branch update")

# ---------- simple / and /api from previous step ----------
@app.route('/')
def home():
    return "Flask is working!"

@app.route('/api')
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

# ---------- MongoDB setup ----------
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("MONGO_URI not set in environment (.env)")

client = MongoClient(MONGO_URI)
# Use database 'flaskdb' — replace if you used a different DB name in connection string
db = client.get_default_database()  # gets DB from the URI if provided
# or: db = client['flaskdb']
collection = db['users']  # collection name 'users'

# ---------- Form routes ----------
@app.route('/form', methods=['GET'])
def form():
    # render empty form, no error by default
    return render_template('form.html', error=None)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()

    # basic validation
    if not name or not email:
        error = "Name and Email are required."
        return render_template('form.html', error=error, name=name, email=email)

    # attempt to insert into MongoDB
    try:
        doc = {"name": name, "email": email}
        result = collection.insert_one(doc)
        # success -> redirect to success page
        return redirect(url_for('success'))
    except Exception as e:
        # show error on the same page without redirect
        error = f"An error occurred: {str(e)}"
        return render_template('form.html', error=error, name=name, email=email)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    itemName = request.form.get('itemName')
    itemDescription = request.form.get('itemDescription')

    doc = {
        "itemName": itemName,
        "itemDescription": itemDescription
    }

    collection.insert_one(doc)

    return "To-Do item saved successfully!"
