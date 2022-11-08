from logic import *

persons = ["Berat", "Melih", "Enes", "Samet"]
combinations = ["Tavuk Kanat & Tavuk Sarma", "Palamut & Karides", "Kuzu Pirzola & Dana Bonfile", "Sucuk & Köfte"]

symbols = []
for person in persons:
    for combination in combinations:
        symbols.append(Symbol(f"{person}-{combination}"))

knowledge = And()

for person in persons:
    Symbol(f"{person}-{combinations[0]}"),
    Symbol(f"{person}-{combinations[1]}"),
    Symbol(f"{person}-{combinations[2]}"),
    Symbol(f"{person}-{combinations[3]}"),


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"{symbol}: YES")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

for combination in combinations:
    for person1 in persons:
        for person2 in persons:
            if person1 != person2:
                knowledge.add(
                    Implication(
                        Symbol(f"{person1}-{combination}"), Not(Symbol(f"{person2}-{combination}"))
                    )
                )

for person in persons:
    for comb1 in combinations:
        for comb2 in combinations:
            if comb1 != comb2:
                knowledge.add(
                    Implication(
                        Symbol(f"{person}-{comb1}"), Not(Symbol(f"{person}-{comb2}"))
                    )
                )

knowledge.add(
    Symbol(f"{persons[1]}-{combinations[0]}")
)
knowledge.add(
    Symbol(f"{persons[2]}-{combinations[2]}")

)
knowledge.add(
    Or(Symbol(f"{persons[3]}-{combinations[2]}"),Symbol(f"{persons[3]}-{combinations[3]}"))
)
knowledge.add(
    Or(Symbol(f"{persons[0]}-{combinations[1]}"),Symbol(f"{persons[0]}-{combinations[3]}"))
)
print(check_knowledge(knowledge))
