import OpenAI from 'openai';
const a = '1. Kultur, Musik, Kunst. 2. Entspannende Urlaube am Strand. 3. Gemäßigt. 4. Asien, insbesondere Japan. 5. Städtische Gebiete. 6. Luxushotels. 7. Konzertbesuche und Museumsbesuche. 8. Keine besonderen Anforderungen. 9. Bevorzuge ruhigere Aktivitäten. 10. 10 Tage im April. 11. 3500€. 12. Alleine.';
const openAI = new OpenAI({apiKey: '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'});
alert('test2');
const completion = openAI.completions.createChatCompletion({
    model: 'gpt-3.5-turbo',
    messages: [
        {role: 'system', content: 'Du bist ein Experte für Urlaubsberatung und -empfehlung. Du kennst an jeden Ort alle möglichen Urlaubsziele, Unternehmungen, Geheimtipps und Aktivitäten.  Dein Aufgabe ist es mir einen perfekten Urlaub zu empfehlen. Ein perfekter Urlaub ist für jedes einzelnen Tag durchgeplant und hat Aktivitäten Vormittags, Mittags und Nachmittags. Hierfür stellst du mir die folgenden Fragen, die ich beantworten werde: 1. Was sind Ihre Interessen? (z.B. Natur, Kultur, Geschichte, Kunst, Musik, Essen, Sport, Entspannung, etc.) 2. Mögen Sie Aktivurlaube (Wandern, Radfahren, Skifahren etc.) oder bevorzugen Sie eher entspannende Urlaube (z.B. am Strand, Wellness-Erlebnisse)? 3. Welche Klimazone bevorzugen Sie? Wärmer, kühler, gemäßigt? 4. Gibt es bestimmte Kontinente oder Länder, die Sie besonders interessieren oder die Sie vermeiden möchten? 5. Haben Sie eine Vorliebe für städtische oder ländliche Gebiete? Oder vielleicht eine Mischung aus beidem? 6. Gibt es bestimmte Aktivitäten, die Sie während Ihres Urlaubs machen möchten? (z.B. Tauchen, Museumsbesuche, Wandern, lokale Küche probieren) 7. Sind Sie offen für abenteuerliche Erfahrungen wie Wildwasser-Rafting, Bungee-Jumping, etc. oder bevorzugen Sie eher ruhigere Aktivitäten? 8. Wie lange planen Sie zu verreisen? Gibt es bestimmte Zeiträume, in denen Sie verreisen möchten? 9. Reisen Sie alleine, mit einem Partner, mit der Familie oder in einer Gruppe? Gebe mir die Antwort stichwortartig aus, sodass sie folgende Informationen enthält: Aktivität, Datum, Adresse, Tageszeit(vormittag, mittag, nachmittag). Nenne zuerst das Reiseziel.'},
        {role: 'user', content: a}],
    temperature: 0,
    });
alert(completion['data']['choices'][0]['message']['content']);
