from flask import Flask, render_template, url_for
from psutil import process_iter, AccessDenied

app = Flask(__name__)

@app.route('/')
def index():
    proc_list = []
    for proc in process_iter():
        try:
            proc_list.append([proc.name(), proc.pid, proc.username()])
        except AccessDenied:
            pass
    
    return render_template('index.html', proc_list=proc_list)

app.run(debug=True)