from flask import Flask
from flask import render_template
from flask import request
import unirest

app = Flask(__name__)


@app.route('/')
def main():
	return render_template('home.html')


@app.route('/yoda')
def yoda():
	sentence = request.args.get('sentence')
	if sentence == "":
		translated = "You forgot to enter a sentence"
	else:
		translated = translate_to_yoda(sentence)
	return render_template('yoda.html', translated=translated)


def translate_to_yoda(sentence):
	response = unirest.get("https://yoda.p.mashape.com/yoda?sentence=" + sentence,
		headers={
			"X-Mashape-Key": "<YOUR KEY HERE>",
			"Accept": "text/plain"
		}
	)
	return response.body


@app.route('/about')
def about():
	return 'This is a super cool website'


if __name__ == '__main__':
	app.run(debug=True)