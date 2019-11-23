with open('F.txt') as inp, open('G.txt', 'w') as out:
    out.write(inp.read().replace('.', '...'))
