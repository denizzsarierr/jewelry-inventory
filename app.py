
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

jewelry = []

@app.route("/")
def index():
    total_value = sum(item["price"] * item["quantity"] for item in jewelry)
    return render_template("index.html", jewelry=jewelry, total_value=total_value)

@app.route("/add", methods=["POST"])
def add_jewelry():
    name = request.form["name"]
    category = request.form["category"]
    price = float(request.form["price"])
    quantity = int(request.form["quantity"])

    jewelry.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    })

    return redirect("/")

@app.route("/delete/<int:index>", methods=["POST"])
def delete_jewelry(index):
    if 0 <= index < len(jewelry):
        jewelry.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
