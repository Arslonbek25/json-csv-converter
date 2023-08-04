import json

with open("input.json", "r") as f:
    data = json.load(f)
    if len(data) == 1:
        data = data[str(*data)]

    columns = [*data[0]]
    output = " ".join(columns)
    for v in data:
        output += "\n" + " ".join(str(v[c]) for c in columns)

    with open("output.csv", "w") as csv:
        csv.write(output)
