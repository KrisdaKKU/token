from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/<text>')
def my_function(text):
  import nltk
  nltk.download('punkt')
  sent = text
  sent = sent.lower()
  list_word = nltk.word_tokenize(sent)
  list_word = str(list_word)
  return list_word

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)