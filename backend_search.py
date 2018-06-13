from datetime import datetime

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        query = dict((key, request.form.getlist(key)[0]) for key in request.form.keys())

        file = f'search_of_{query["subject"]}_{int(datetime.now().timestamp())}'
        message = f"The parameters you've entered have been passed to the search engine, you can view the results in a " \
                  f"file named {file}"


        return render_template('search.html', message=message)
    else:
        return render_template('search.html')








if __name__ == '__main__':
    app.run()