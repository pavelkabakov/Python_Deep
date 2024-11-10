placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}

for ch in placement:
    if ch not in d:
        d[ch] = 0
    d[ch] = d[ch] + 1
print(d)
list_key = list(d.keys())
print(list_key)
key_with_min_value = list_key[0]
for key in list_key:
    if d[key] < d[key_with_min_value]:
        key_with_min_value = key
print(d[key_with_min_value])