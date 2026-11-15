def multiply(a, b):
    res = float(a) * float(b)
    return int(res) if res.is_integer() else res
