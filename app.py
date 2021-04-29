import os
from flask import *
app = Flask(__name__)


@app.route('/mainpage',methods=['POST'])
def show_main_page():
    name=request.form.get('name','Random User')
    return render_template('./mainpage.html',name=name)

@app.route('/')
def sample():
    return render_template('./index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
