from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>  
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px; 
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
                #rot{{
                 width:25px;
                 text-align:center;}}
            </style>
        </head>
        <body>
        <form action='/' method='post'><label>Rotatate By:<input type='text' value='0' id="rot" name="rot"/></label>
        <textarea id='text' name="text">{0}</textarea>
        <input type="submit" value="Encrypt"/>
    </html>
    """

@app.route('/', methods=['GET'])
def add_form():
    new_text =''
    
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    
    new_text = ''
    rotate = request.form["rot"]
    encrypt_text = request.form["text"]
    
    if rotate.isnumeric():
        rotate = int(rotate)

    run_encry = rotate_string(encrypt_text,rotate)

    new_text = run_encry

    return form.format(run_encry)
app.run()