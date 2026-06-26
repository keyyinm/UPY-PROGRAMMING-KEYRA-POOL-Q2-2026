#INPUT
verb = input("Verbo a conjugar: ")

#PROCESS
pronouns = ['Yo', 'Tu', 'El', 'Nosotros', 'Vosotros', 'Ellos']
endings = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

stem = verb[:-2]
ending = verb[-2:]
ending_list = endings[ending]

#OUTPUT
for index, pronoun in enumerate(pronouns):
    end = ending_list[index]
    print(f"{pronoun} {stem}{end}")
