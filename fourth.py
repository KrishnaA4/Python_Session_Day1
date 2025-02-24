data = {
    'n1':50,
    'n2':75,
    'n3':80
}

highest_scorer_key = ''
highest_score = 0

for x in data:
    highest_scorer_key = x
    highest_score = data[x]
    break

for x in data:
    if data[x]>highest_score:
        highest_score = data[x]
        highest_scorer_key = x

print(f"Highest scorer is {highest_scorer_key} with a score of {highest_score}")
