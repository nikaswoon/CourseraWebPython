def calculate(data, findall):
    matches = findall(r"([a-c])((?:\+|\-)?)\=(?:([a-c]?)((?:\+|\-)?[\d]+)|([a-c]?))")
    for v1, s, v2, n, v2_ in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number], [var2v2],
        if s:
            if v2_:
                data[v1] = data.get(v1, 0) + data.get(v2_, 0) if s == '+' else data.get(v1, 0) - data.get(v2_, 0)
            else:
                data[v1] = data.get(v1, 0) + (data.get(v2, 0) + int(n or 0)) if s == '+' else data.get(v1, 0) - (data.get(v2, 0) + int(n or 0))
        else:
            data[v1] = data.get(v2_, 0) if v2_ else data.get(v2, 0) + int(n or 0)
    return data
