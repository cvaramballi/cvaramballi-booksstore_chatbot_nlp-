from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__,static_url_path='/static/style.css')
app.static_folder = 'static'

booksbee = ChatBot('Bot',
             storage_adapter='chatterbot.storage.SQLStorageAdapter',
#             response_selection_method='get_first_response',
#             statement_comparison_function='levenshtein_distance',
             logic_adapters=[
   {
       'import_path': 'chatterbot.logic.BestMatch'
#       'threshold' : 0.50,
#       'default_response': 'I am sorry, but I did not understand your request. I am still learning, can you please be more accurate on your requirement? '
   }
#    {
#        "statement_comparison_function": 'chatterbot.comparisons.levenshtein_distance',
#        'import_path': 'chatterbot.logic.LowConfidenceAdapter',
#        'threshold': 0.90,
#       'default_response': 'I am sorry, but I do not understand your request. I am still learning, can you please be more accrate on your requirement?',
#        'maximum_similarity_threshold': 0.90

#   }
   
],
trainer='chatterbot.trainers.ListTrainer')
booksbee.set_trainer(ListTrainer)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
#    response = str(booksbee_bot.get_response(userText))
    response = (booksbee.get_response(userText))
    print ("Trying to print the response confidence")
    print (response.confidence)
    if (response.confidence) < 0.50 :
        return ("I am sorry, but I did not understand your request. I am still learning, can you please be more accurate on your requirement?")
    else:
        response = str(response)
        r = response.lstrip("- -")
        return r.replace("*", "<br><br>")

#    corpus.confidence) > 0.5:


if __name__ == "__main__":
    app.run(debug=True)

