import sys 
sys.path.append('c:/programdata/anaconda3/lib/site-packages')

from flask import Flask, request, render_template

sys.path.append('c:/users/97798/appdata/roaming/python/python39/site-packages')

import json2table

from json2table import convert
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        my_var = request.form.get('myInput')
        #print('Received variable:', my_var)
        json_object = json.loads(my_var)
        #print(json_object)
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style" : "width:100%"}

        html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)

        return render_template("table.html", html = html)

   
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
