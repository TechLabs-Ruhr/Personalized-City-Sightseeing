from flask import Flask, render_template
import openai

app = Flask(__name__, template_folder='views')

@app.route('/')
def index():
    openai.api_key = "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"

    a = "1. Kultur, Musik, Kunst. 2. Entspannende Urlaube am Strand..."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "Du bist ein Experte für Urlaubsberatung..."
            },
            {"role": "user", "content": a}
        ]
    )
    
    recommendation = response['choices'][0]['message']['content']
    
    # Render the ejs template and pass the recommendation to it.
    return render_template('SightseeingSpots.ejs', Sightseeing=recommendation)

if __name__ == '__main__':
    app.run(debug=True)
