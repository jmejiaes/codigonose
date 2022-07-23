from codecs import escape_encode


def divisors(num):
    try:
        if num <= 0:
            raise ValueError("Solo estan permitidos numeros negativos")
        return [i for i in range(1, num+1) if num % i == 0]
    except ValueError as ve:
        print(ve)


def run():
    print(divisors(-1))

if __name__ == '__main__' :
    run()