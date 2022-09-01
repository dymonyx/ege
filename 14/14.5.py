for n in range(100):
    try: #чтобы не вылезала куча ошибок
        if int('132', n) + int('13', 8) == int('124', n+1): #int переводит число из любой системы в 10ричную, bin в 2ичную, oct в 8, hex в 16
            print(n)
    except:
        pass
