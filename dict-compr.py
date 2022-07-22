import math
def run():
    d = {i:i**3 for i in range(1,100) if i%3 != 0}
    print(d)

def reto():
    d = {i:i**(0.5) for i in range(1,1000)}
    print(d)

if __name__ == "__main__":
    reto()