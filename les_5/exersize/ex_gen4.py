# Перед вами несколько строк кода. Напишите что по вашему мнению выведет print,
# не запуская код. У вас 3 минуты.
def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)
for item in gen(10, 1):
    print(f'{item = }')