# Вступ
# Python: парадигма: мульти, основна - функціональна, покоління - 4
x = 10                # змінні типізовані, задаються ініціалізацією
print( x, type(x) )   # 10 <class 'int'>
x = 1 + 2j            # типізація не статична, змінюється присвоюванням
print( x, type(x) )   # (1+2j) <class 'complex'>
s = "string"
y = 10
# print(s + y)        # TypeError: can only concatenate str (not "int") to str
# print(y + s)        # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(y) + s)
print(y + int("20"))
# сувора типізація (не плутати зі статичною) - неможливість операцій з різними типами
# даних (відсутність неявного перетворення типів)
print(y + x,          # (11+2j) <class 'complex'>
      type(y + x))    # висновок - різні типи можуть брати участь в операціях, типізація не сувора

print(type((1,2,3)))  # <class 'tuple'>
print(type([1,2,3]))  # <class 'list'>

s = "%d %d %d" % (1,2,3)  # зчеплення кортежів
print(s)
print(3 % 2)              # залишок ділення
s = f"{y} {y}"
print(s)
print(2 ** 1000)          # цілі числа не мають формальної межі