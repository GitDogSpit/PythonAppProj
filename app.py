from flask import Flask, render_template, request

app = Flask(__name__)

def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def writeDetails(filename, message):
    with open(filename, 'a') as f:#append
        f.write(message)
        f.write("\n")

@app.route("/")#im gonna define that should happen here. "When i got to the homepage hello shouod be run"
def hello():
    name = "Myname"
    aboutMe = readDetails('static/details.txt')
    return render_template('templates/homepage.html')

#@app.route("/links")
#def anotherPage():#type slash links to go to this after IP
#    return "<p> This is another page dedicated to links</p> <a href = '/'> Link back to webpage</a>""

#@app.route("/video")
#def videoPage():#trying without html, just for testing
#    return "<video width='320' height='240' controls> <source src='static\QuickRender.mp4' type='video/mp4'> </video>"

@app.route("/moist")
def page():
    return render_template('templates/moist.html')

@app.route('/form', methods=['GET', 'POST'])#get post means read and write
def formDemo():
    name = 'None'

    comments = readDetails('static/comments.txt')

    if request.method == 'POST':
        #if request.form['name']:
        #    name = request.form['name']
        if request.form['message']:
            writeDetails('static/comments.txt', request.form['message'])
    return render_template('templates/form.html', name=name, aboutMe = [])

if __name__ == "__main__":
    app.run(debug = True)