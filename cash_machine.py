from num2words import num2words as n2w

while True:
    num = int(input("Введите сумму к выдаче (от 1 до 100000): "))
    if num >= 1 and num <= 100000:
        break
    else:
        print("Банкомат не может выдать такую сумму.")

to_matching = num % 10
match to_matching:
    case 0:
        print(n2w(num, lang="ru").capitalize(), "рублей")
    case 1:
        print(n2w(num, lang="ru").capitalize(), "рубль")
    case 2:
        print(n2w(num, lang="ru").capitalize(), "рубля")
    case 3:
        print(n2w(num, lang="ru").capitalize(), "рубля")
    case 4:
        print(n2w(num, lang="ru").capitalize(), "рубля")
    case 5:
        print(n2w(num, lang="ru").capitalize(), "рублей")
    case 6:
        print(n2w(num, lang="ru").capitalize(), "рублей")
    case 7:
        print(n2w(num, lang="ru").capitalize(), "рублей")
    case 8:
        print(n2w(num, lang="ru").capitalize(), "рублей")
    case 9:
        print(n2w(num, lang="ru").capitalize(), "рублей")

