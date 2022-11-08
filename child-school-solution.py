from logic import *

persons = ["Ayça", "Burcu", "Ceyda", "Deniz"]
classes = ["Papatya", "Karanfil", "Zambak", "Lale"]

symbols = []
for person in persons:
    for combination in classes:
        symbols.append(Symbol(f"{person}-{combination}"))

knowledge = And()

for person in persons:
    Symbol(f"{person}-{classes[0]}"),
    Symbol(f"{person}-{classes[1]}"),
    Symbol(f"{person}-{classes[2]}"),
    Symbol(f"{person}-{classes[3]}"),


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"{symbol}: YES")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


for classroom in classes:
    for person1 in persons:
        for person2 in persons:
            if person1 != person2:
                knowledge.add(
                    Implication(
                        Symbol(f"{person1}-{classroom}"), Not(Symbol(f"{person2}-{classroom}"))
                    )
                )

for person in persons:
    for class1 in classes:
        for class2 in classes:
            if class1 != class2:
                knowledge.add(
                    Implication(
                        Symbol(f"{person}-{class1}"), Not(Symbol(f"{person}-{class2}"))
                    )
                )

knowledge.add(
    Symbol(f"{persons[2]}-{classes[0]}")
)
knowledge.add(
    Not(Symbol(f"{persons[1]}-{classes[1]}"))
)
knowledge.add(
    Not(Symbol(f"{persons[1]}-{classes[2]}"))
)
knowledge.add(
    Not(Symbol(f"{persons[0]}-{classes[2]}"))
)
knowledge.add(
    Not(Symbol(f"{persons[0]}-{classes[3]}"))
)
knowledge.add(
    Symbol(f"{persons[0]}-{classes[1]}")
)


print(check_knowledge(knowledge))
