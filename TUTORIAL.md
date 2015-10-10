# DubHacks Intro to Web Dev Writeup *in progress*
## Creating your first web app

Hi, this is a tutorial targeted at people building their very first web app. Download the complete app/code here: https://github.com/anwell/dubhacks-yoda/archive/master.zip 

## Getting started
1. Create the folder `dubhacksworkshop` on your computer.
2. Open your text editor and paste the following contents. This will be the base of our application.
```
from flask import Flask
from flask import render_template
from flask import request
import unirest

app = Flask(__name__)

 

if __name__ == '__main__':
    app.run(debug=True)
```
3. Save the file as `app.py` inside the dubhacksworkshop folder
4. Now we'll add some beginner code. Update the file to look like this:
```
from flask import Flask
from flask import render_template
from flask import request
import unirest

app = Flask(__name__)


@app.route('/')
def main():
    return 'This is a great DubHacks workshop'


if __name__ == '__main__':
   app.run(debug=True)
```
5. Inside your terminal type the following and press enter:
```
python app.py
```
6. Now open your browser and you should see 

## Decisions
A lot of what I recommend in this tutorial is not the current best practice. Here is some reasoning behind the decisions that were made.

1. Why Python? Why not something like Node.js?
This tutorial assumes that the readers have introductory experience with programming in a language like Java. Python has similar syntax / paradigms and the Flask framework requires a very low amount of boilerplate "magic" code. Node.js might have been a good option, although teaching callbacks and the quirks of JS might get in the way of learning how to build a site end to end.

