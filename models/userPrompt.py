# erstelle mit einer übergebenen Frage und den dazugehörigen Antworten eine Ausgabe, womit der nutzer eine oder mehrere
# der Antworten oder einen Freitext eingeben kann
def ask_question_with_choices(question, choices):
    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    choice_number = input("Wählen Sie die Nummer der passenden Antwort oder geben Sie einen Freitext ein: ")
    try:
        choice_number = int(choice_number)
        if 1 <= choice_number <= len(choices):
            return choices[choice_number - 1]
    except ValueError:
        pass

    # Falls keine gültige Nummer eingegeben wurde oder Freitext gewünscht ist
    return choice_number

def main():
    print("Willkommen! Beantworten Sie bitte einige Fragen, um den idealen Urlaub für Sie zu planen.")

    user_answers = {}

    interests_choices = ["Natur", "Kultur", "Geschichte", "Kunst", "Musik", "Essen", "Sport", "Entspannung"]
    user_answers["Interessen"] = ask_question_with_choices("Was sind Ihre Interessen?", interests_choices)

    vacation_type_choices = ["Aktivurlaube", "Entspannende Urlaube"]
    user_answers["Urlaubstyp"] = ask_question_with_choices("Mögen Sie Aktivurlaube oder bevorzugen Sie eher entspannende Urlaube?", vacation_type_choices)

    climate_preference_choices = ["Wärmer", "Kühler", "Gemäßigt"]
    user_answers["Klimazone"] = ask_question_with_choices("Welche Klimazone bevorzugen Sie?", climate_preference_choices)

    continent_choices = ["Europa", "Amerika", "Asien", "Afrika", "Australien"]
    user_answers["Kontinente"] = ask_question_with_choices("Gibt es Kontinente die Sie besonders interessieren?", continent_choices)

    city_or_rural_choices = ["Stadt", "Ländlich"]
    user_answers["Stadt oder Land"] = ask_question_with_choices("Städtische oder Ländliche Gebiete?", city_or_rural_choices)

    travel_type_choices = ["Alleine", "mit einem Partner", "in einer Gruppe"]
    user_answers["Alleine oder in einer Gruppe"] = ask_question_with_choices("Reisen Sie alleine, mit einem Partner, mit der Familie oder in einer Gruppe?", travel_type_choices)
    # Weitere Fragen und Antwortmöglichkeiten hier ergänzen...

    print("\nVielen Dank für Ihre Antworten! Basierend auf Ihren Angaben werden wir den idealen Urlaub für Sie planen.")
    print("Ihre Antworten:")
    for question, answer in user_answers.items():
        print(f"{question}: {answer}")

if __name__ == "__main__":
    main()
