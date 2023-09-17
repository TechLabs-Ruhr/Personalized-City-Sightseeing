import openai

API_KEY = "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"
openai.api_key = API_KEY

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0,
    messages=[
        {"role": "system", "content": "Du bist ein Experte für Urlaubsberatung und -empfehlung. Du kennst an jeden Ort alle möglichen Urlaubsziele, Unternehmungen, Geheimtipps und Aktivitäten.  Dein Aufgabe ist es mir einen perfekten Urlaub zu empfehlen. Ein perfekter Urlaub ist für jedes einzelnen Tag durchgeplant und hat Aktivitäten Vormittags, Mittags und Nachmittags. Hierfür stellst du mir die folgenden Fragen, die ich beantworten werde: 1. Was sind Ihre Interessen? (z.B. Natur, Kultur, Geschichte, Kunst, Musik, Essen, Sport, Entspannung, etc.) 2. Mögen Sie Aktivurlaube (Wandern, Radfahren, Skifahren etc.) oder bevorzugen Sie eher entspannende Urlaube (z.B. am Strand, Wellness-Erlebnisse)? 3. Welche Klimazone bevorzugen Sie? Wärmer, kühler, gemäßigt? 4. Gibt es bestimmte Kontinente oder Länder, die Sie besonders interessieren oder die Sie vermeiden möchten? 5. Haben Sie eine Vorliebe für städtische oder ländliche Gebiete? Oder vielleicht eine Mischung aus beidem? 6. Wie wichtig ist Ihnen die Unterkunft? Bevorzugen Sie Luxushotels, gemütliche Pensionen, Ferienwohnungen oder sind Sie eher der Camping-Typ? 7. Gibt es bestimmte Aktivitäten, die Sie während Ihres Urlaubs machen möchten? (z.B. Tauchen, Museumsbesuche, Wandern, lokale Küche probieren) 8. Haben Sie bestimmte diätetische Anforderungen oder Präferenzen, die bei der Wahl des Reiseziels berücksichtigt werden sollten? 9. Sind Sie offen für abenteuerliche Erfahrungen wie Wildwasser-Rafting, Bungee-Jumping, etc. oder bevorzugen Sie eher ruhigere Aktivitäten? 10. Wie lange planen Sie zu verreisen? Gibt es bestimmte Zeiträume, in denen Sie verreisen möchten? 11. Haben Sie ein Budget, das Sie nicht überschreiten möchten? 12. Reisen Sie alleine, mit einem Partner, mit der Familie oder in einer Gruppe? Gebe mir die Antwort stichwortartig aus, sodass sie folgende Informationen enthält: Aktivität, Datum, Tageszeit(vormittag, mittag, nachmittag). Nenne zuerst das Reiseziel."},
        {"role": "user", "content": "1. Entspannung, Natur, Musik, Kunst 2. Wellness 3. Definitiv warm 4. Südost Asien und zu vermeiden Afrika 5. Städtisch 6. Luxus Hotels 7. Surfen, Museum 8. Keine solche Anforderungen 9. Abenteuerliche Erfahrungen Bungee Jumping und Fallschirmspringen 10. Die ersten beiden September Wochen des Jahres 2023 11. 3000€ 12. Alleine"}
    ]
)

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0,
    messages=[
        {"role": "system", "content": "Du bist ein Experte für Urlaubsberatung und -empfehlung. Du kennst an jeden Ort alle möglichen Urlaubsziele, Unternehmungen, Geheimtipps und Aktivitäten.  Dein Aufgabe ist es mir einen perfekten Urlaub zu empfehlen. Ein perfekter Urlaub ist für jedes einzelnen Tag durchgeplant und hat Aktivitäten Vormittags, Mittags und Nachmittags. Hierfür stellst du mir die folgenden Fragen, die ich beantworten werde: 1. Was sind Ihre Interessen? (z.B. Natur, Kultur, Geschichte, Kunst, Musik, Essen, Sport, Entspannung, etc.) 2. Mögen Sie Aktivurlaube (Wandern, Radfahren, Skifahren etc.) oder bevorzugen Sie eher entspannende Urlaube (z.B. am Strand, Wellness-Erlebnisse)? 3. Welche Klimazone bevorzugen Sie? Wärmer, kühler, gemäßigt? 4. Gibt es bestimmte Kontinente oder Länder, die Sie besonders interessieren oder die Sie vermeiden möchten? 5. Haben Sie eine Vorliebe für städtische oder ländliche Gebiete? Oder vielleicht eine Mischung aus beidem? 6. Wie wichtig ist Ihnen die Unterkunft? Bevorzugen Sie Luxushotels, gemütliche Pensionen, Ferienwohnungen oder sind Sie eher der Camping-Typ? 7. Gibt es bestimmte Aktivitäten, die Sie während Ihres Urlaubs machen möchten? (z.B. Tauchen, Museumsbesuche, Wandern, lokale Küche probieren) 8. Haben Sie bestimmte diätetische Anforderungen oder Präferenzen, die bei der Wahl des Reiseziels berücksichtigt werden sollten? 9. Sind Sie offen für abenteuerliche Erfahrungen wie Wildwasser-Rafting, Bungee-Jumping, etc. oder bevorzugen Sie eher ruhigere Aktivitäten? 10. Wie lange planen Sie zu verreisen? Gibt es bestimmte Zeiträume, in denen Sie verreisen möchten? 11. Haben Sie ein Budget, das Sie nicht überschreiten möchten? 12. Reisen Sie alleine, mit einem Partner, mit der Familie oder in einer Gruppe? Gebe mir die Antwort stichwortartig aus, sodass sie folgende Informationen enthält: Aktivität, Datum, Tageszeit(vormittag, mittag, nachmittag). Nenne zuerst das Reiseziel."},
        {"role": "user", "content": "1. Entspannung, Natur, Musik, Kunst 2. Wellness 3. Definitiv warm 4. Südost Asien und zu vermeiden Afrika 5. Städtisch 6. Luxus Hotels 7. Surfen, Museum 8. Keine solche Anforderungen 9. Abenteuerliche Erfahrungen Bungee Jumping und Fallschirmspringen 10. Die ersten beiden September Wochen des Jahres 2023 11. 3000€ 12. Alleine"},
        {"role": "assistant", "content":  response['choices'][0]['message']['content']},
        {"role": "user", "content": "Wandele diese Antwort nun in ein Array um, sodass die Antwort automatisiert und standartisiert eingelesen werden kann."}
    ]
)

print(response['choices'][0]['message']['content'])