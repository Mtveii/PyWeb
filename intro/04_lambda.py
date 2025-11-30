x = 10
lam2 = None

def make_lambda() :
    x = 20
    return lambda : print(x)  # 20 - захват (capture) локальної змінної

def make_lambda1() :
    return lambda : print(x)  # 10 - звернення до глобальної змінної


def make_lambda2() :
    global lam2
    x = 40
    lam2 = lambda : print(x)  # 50 - захват області відбувається при її руйнації 
    x = 50                    # (а не на момент оголошення lambda)


def fact(n) :
    return 1 if n < 2 else n * fact(n-1)


def main() :
    x = 30
    lam = make_lambda()
    lam()
    make_lambda1()()
    make_lambda2()
    lam2()
    print(fact(5))


if __name__ == '__main__':
    main()
