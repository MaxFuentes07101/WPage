from flask import Flask, render_template, request, redirect

app = Flask(__name__)
print(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def about(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        with open("./database.txt", mode="a") as info:
            info.writelines(('email: ', data['email']))
            info.write('\n')
            info.writelines(('subject: ',data['subject']))
            info.write('\n')
            info.writelines(('message: ',data['message']))
            info.write('\n')
        print(data)
        return redirect('/ThankYou.html')
    else:
        return 'something went wrong!!'