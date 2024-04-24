from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def Climate():
    template = render_template('P7a-Climate.html')
    return(template)

@app.route('/temperature', methods=['POST','GET'])
def temperature():
    if request.method=='POST':
        temperature = request.form
    # else:
    #     temperature=request.args.get('nm')
        template = render_template('P7b-Temperature.html', temperature=temperature)
        return(template)

if __name__ == '__main__':
    app.run(debug = True)