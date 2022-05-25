a = {"c":3, "b":2, "a":1 }

keys = sorted(a)
sorted_a = {key:a[key] for key in keys}
print(keys)
