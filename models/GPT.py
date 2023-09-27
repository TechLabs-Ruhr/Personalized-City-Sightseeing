from flask import Flask, render_template
import openai
import time  # Importieren Sie das time-Modul
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__, template_folder='views')
app.jinja_env = Environment(loader=FileSystemLoader('views'))

@app.route('/')
def index():
    openai.api_key = "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"

    a = "1. Kultur, Musik, Kunst. 2. Entspannende Urlaube am Strand. 3. Gemäßigt. 4. Asien, insbesondere Japan. 5. Städtische Gebiete. 6. Luxushotels. 7. Konzertbesuche und Museumsbesuche. 8. Keine besonderen Anforderungen. 9. Bevorzuge ruhigere Aktivitäten. 10. 10 Tage im April. 11. 3500€. 12. Alleine."

    max_retries = 5
    wait_seconds = 10
    
    for i in range(max_retries):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=0,
                messages=[
                    {"role": "system", "content": "Du bist ein Experte für Urlaubsberatung und -empfehlung. Du kennst an jeden Ort alle möglichen Urlaubsziele, Unternehmungen, Geheimtipps und Aktivitäten.  Dein Aufgabe ist es mir einen perfekten Urlaub zu empfehlen. Ein perfekter Urlaub ist für jedes einzelnen Tag durchgeplant und hat Aktivitäten Vormittags, Mittags und Nachmittags. Hierfür stellst du mir die folgenden Fragen, die ich beantworten werde: 1. Was sind Ihre Interessen? (z.B. Natur, Kultur, Geschichte, Kunst, Musik, Essen, Sport, Entspannung, etc.) 2. Mögen Sie Aktivurlaube (Wandern, Radfahren, Skifahren etc.) oder bevorzugen Sie eher entspannende Urlaube (z.B. am Strand, Wellness-Erlebnisse)? 3. Welche Klimazone bevorzugen Sie? Wärmer, kühler, gemäßigt? 4. Gibt es bestimmte Kontinente oder Länder, die Sie besonders interessieren oder die Sie vermeiden möchten? 5. Haben Sie eine Vorliebe für städtische oder ländliche Gebiete? Oder vielleicht eine Mischung aus beidem? 6. Gibt es bestimmte Aktivitäten, die Sie während Ihres Urlaubs machen möchten? (z.B. Tauchen, Museumsbesuche, Wandern, lokale Küche probieren) 7. Sind Sie offen für abenteuerliche Erfahrungen wie Wildwasser-Rafting, Bungee-Jumping, etc. oder bevorzugen Sie eher ruhigere Aktivitäten? 8. Wie lange planen Sie zu verreisen? Gibt es bestimmte Zeiträume, in denen Sie verreisen möchten? 9. Reisen Sie alleine, mit einem Partner, mit der Familie oder in einer Gruppe? Gebe mir die Antwort stichwortartig aus, sodass sie folgende Informationen enthält: Aktivität, Datum, Adresse, Tageszeit(vormittag, mittag, nachmittag). Nenne zuerst das Reiseziel."},
                    {"role": "user", "content": a}
                ]
            )
            break  # Wenn die Anfrage erfolgreich ist, brechen Sie aus der Schleife aus
        except openai.error.ServiceUnavailableError:
            if i < max_retries - 1:  # Nicht schlafen nach dem letzten Versuch
                time.sleep(wait_seconds)
            else:
                return render_template('Error.ejs')  # Rendern Sie eine Fehlerseite oder geben Sie eine Fehlermeldung zurück, wenn alle Versuche fehlschlagen
    
    recommendation = response['choices'][0]['message']['content']
    
    return render_template('SightseeingSpots.html', Sightseeing=recommendation)


if __name__ == '__main__':
    app.run(debug=True)
