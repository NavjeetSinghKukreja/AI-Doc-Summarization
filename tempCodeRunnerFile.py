from flask import Flask, request, render_template
from models import generate_combined_summary, get_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    sentiment = ""
    
    if request.method == 'POST':
        user_text = request.form['user_text']
        if user_text:
            summary = generate_combined_summary(user_text)
            sentiment = get_sentiment(summary)
    
    return render_template('index.html', summary=summary, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
