product = "iphone and android phones"
lett_d = {}
for ch in product:
    if ch not in lett_d:
        lett_d[ch] = 0
    lett_d[ch] = lett_d[ch] + 1

list_key = list(lett_d.keys())
key_with_max_value = list_key[0]
for key in list_key:
    if lett_d[key] > lett_d[key_with_max_value]:
        key_with_max_value = key
print(key_with_max_value)