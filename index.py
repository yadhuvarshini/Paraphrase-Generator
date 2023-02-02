from flask import Flask,render_template,request,redirect,url_for
from parrot.parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
b = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

@app.route("/", methods=['GET','POST'])
def home():
	if request.method == 'POST':
		question = request.form["nm"]
		# return redirect(url_for("user", usr = question))
		phrases = [question]

		for phrase in phrases:
			print("-"*100)
			print("Input_phrase: ", phrase)
			print("-"*100)
			para_phrases = b.augment(input_phrase=phrase, use_gpu=False)
			for para_phrase in para_phrases:
				print(para_phrase)
			
			render_template("home.html", para_phrase = question)
	else:
		return render_template("home.html")

@app.route("/<usr>")
def user(usr):
	return f"<h1>{usr}</h1>"

if __name__ == "__main__":
	app.run(debug = True)
