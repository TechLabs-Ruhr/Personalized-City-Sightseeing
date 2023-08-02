import userPrompt  

user_answers = userPrompt.main()

#Erweiterung von template_prompt um die genaue Ausgestaltung der Ausgabe zur Weitergabe an die Web-Anwendung und Anzeige für den Nutzer
template_prompt = "Der Nutzer interessiert sich für: {}, bevorzugt: {} Urlaube, mag {} Klima, ist interessiert an {} Kontinenten, bevorzugt {} Gebiete und reist {}."
user_input_formatted = template_prompt.format(user_answers['Interessen'], user_answers['Urlaubstyp'], user_answers['Klimazone'], user_answers['Kontinente'], user_answers['Stadt oder Land'], user_answers['Alleine oder in einer Gruppe'])
