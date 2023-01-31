from flask import Flask,render_template,request,redirect,url_for
# from parrot import parrot
# import torch
# import warnings
# warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
	if request.method == 'POST':
		question = request.form["nm"]
		# return redirect(url_for("user", usr = question))
		return render_template("home.html", question = question)

	else:
		return render_template("home.html")

@app.route("/<usr>")
def user(usr):
	return f"<h1>{usr}</h1>"

# For reproducibility
# def random_state(seed):
#   torch.manual_seed(seed)
#   if torch.cuda.is_available():
#     torch.cuda.manual_seed_all(seed)
# pip install --upgrade jupyter_http_over_ws>=0.0.7 && \jupyter serverextension enable --py jupyter_http_over_ws
# random_state(1234)
# parrot = parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

# phrases = ["what do you want?"]

# for phrase in phrases:
#   print("-"*100)
#   print("Input_phrase: ", phrase)
#   print("-"*100)
#   para_phrases = parrot.augment(input_phrase=phrase)
#   for para_phrase in para_phrases:
#    print(para_phrase)


if __name__ == "__main__":
	app.run(debug = True)
  