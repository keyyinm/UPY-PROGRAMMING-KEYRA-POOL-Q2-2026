class VerbError(Exception):
    pass


try:
    verb = input("Verb to conjugate: ").lower()

    if len(verb) < 3:
        raise VerbError("The verb is too short.")

except VerbError as e:
    print(e)

else:
    try:
        pronouns = ["Yo", "Tu", "El", "Nosotros", "Vosotros", "Ellos"]

        endings = {
            "ar": ["o", "as", "a", "amos", "ais", "an"],
            "er": ["o", "es", "e", "emos", "eis", "en"],
            "ir": ["o", "es", "e", "imos", "is", "en"]
        }

        ending = verb[-2:]

        if ending not in endings:
            raise VerbError("The verb must end in ar, er or ir.")

        stem = verb[:-2]
        ending_list = endings[ending]

    except VerbError as e:
        print(e)

    else:
        for index, pronoun in enumerate(pronouns):
            end = ending_list[index]
            print(f"{pronoun} {stem}{end}")
