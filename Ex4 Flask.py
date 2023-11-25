from flask import Flask, render_template,request,jsonify,url_for


app = Flask(__name__)

@app.route('/')
def hello():
    print("home")
    return render_template('Webpage.html')

@app.route("/submit",methods=["GET","POST"]) 
def sub():
    
    if request.method == "POST":
        year = request.form.get("years")
        discipline = request.form.get("discipline")       

        if len(year) and len(discipline):            
            return render_template("Entered.html", years = year, discipline = discipline)

    return render_template("Webpage.html")
            
if __name__ == '__main__':
   
    app.run()