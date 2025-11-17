from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    item_list = []
    with open('items.json', 'r') as f:
        data = json.load(f)
    for key,value in data.items():
        item_list = value
    return render_template('items.html', items=item_list)

@app.route("/products")
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error_message = None
    products = []

    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    else:
        error_message = "Wrong source"
        return render_template("product_display.html",
                               products=products,
                               error_message=error_message)
    
    if product_id:
        filtered = [p for p in products if str(p.get("id")) == str(product_id)]
        if not filtered:
            error_message = "Product not found"
            return render_template("product_display.html",
                                   products=products,
                                   error_message=error_message)
        products = filtered
    
    return render_template("product_display.html",
                           products=products,
                           error_message=error_message)

def read_json():
    file_path = os.path.join(app.root_path, "products.json")
    with open(file_path, "r") as f:
        return json.load(f)

def read_csv():
    file_path = os.path.join(app.root_path, "products.csv")
    products = []
    with open(file_path, "r", newline='') as f:
        data = csv.DictReader(f)
        for row in data:
            products.append(row)
        return products

if __name__ == '__main__':
    app.run(debug=True, port=5000)
