from flask import Flask, render_template, request,jsonify
from pdf_generator import generate_pdf
import random
import urllib

app = Flask(__name__)

@app.route("/")
def Index():
    return render_template("main.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/board", methods=["GET","POST"])
def board():
    if request.method =="POST":
        password= request.form.get("password")
        if password == "123":
            return render_template("home.html")
        else:
            return render_template("login.html")      

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/analysis")
def analytics():
    return render_template("analysis.html")

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/setting")
def setting():
    return render_template("setting.html")

@app.route('/pdf', methods=['POST'])
def generate_pdf_route():
    moisture_data = [(random.randint(1, 80)) for _ in range(30)]  # 30 random moisture values between 1 and 100
    temperature_data = [(random.randint(21, 50)) for _ in range(30)]  # 30 random temperature values between 21°C and 50°C
    humidity_data = [(random.randint(50, 100)) for _ in range(30)]  # 30 random humidity values between 50% and 100%
    pdf_filename = generate_pdf(moisture_data, temperature_data, humidity_data)

    return jsonify({"message": "PDF generated successfully!", "pdf_filename": pdf_filename})
   
@app.route("/motor")
def motor():
    return render_template("motor.html")

# Run the web server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)
