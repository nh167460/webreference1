# Imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import time

# app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/leaderboards')
def leaderboards():
    return render_template('leaderboards.html')

@app.route('/store')
def store():
    products_1month = [
        {
            "name": "Encryption Rank",
            "price": 1.99,
            "description": "Access to exclusive commands.",
            "image": "encryption.png"
        },
        {
            "name": "Quantum Rank",
            "price": 3.99,
            "description": "Includes all VIP perks plus more.",
            "image": "quantum.png"
        },
        {
            "name": "Nexus Rank",
            "price": 8.99,
            "description": "Includes all VIP perks plus more.",
            "image": "nexus.png"
        },
        {
            "name": "Cipher Rank",
            "price": 15.99,
            "description": "Includes all VIP perks plus more.",
            "image": "cipher.png"
        },
        {
            "name": "Cipher + Rank",
            "price": 25.99,
            "description": "Includes all VIP perks plus more.",
            "image": "cipher_plus.png"
        }
    ]
    products_permanent = [
        {
            "name": "Encryption Rank",
            "price": 6.99,
            "description": "Access to exclusive commands.",
            "image": "encryption.png"
        },
        {
            "name": "Quantum Rank",
            "price": 10.99,
            "description": "Includes all VIP perks plus more.",
            "image": "quantum.png"
        },
        {
            "name": "Nexus Rank",
            "price": 20.99,
            "description": "Includes all VIP perks plus more.",
            "image": "nexus.png"
        },
        {
            "name": "Cipher Rank",
            "price": 35.99,
            "description": "Includes all VIP perks plus more.",
            "image": "cipher.png"
        },
        {
            "name": "Cipher + Rank",
            "price": 70.99,
            "description": "Includes all VIP perks plus more.",
            "image": "cipher_plus.png"
        }
    ]
    return render_template('store.html', products_1month=products_1month, products_permanent=products_permanent)

@app.route('/staff')
def staff():
    return render_template('staff.html', current_time=int(time.time()))

@app.route('/punishments')
def punishments():
    return render_template('punishments.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)