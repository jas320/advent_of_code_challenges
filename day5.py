for i in range(7,26):
    with open(f"day{i}.py", 'w') as file:
        file.write('''from utils import loadInput


inputLines = loadInput()''')