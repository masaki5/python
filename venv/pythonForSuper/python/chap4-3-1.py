def create_mail(recv, bill) :
    tmp = '''{}様
PT企画の斉藤です。
今月の請求額は{}円です。
'''　

    msg = tmp.format(recv,bill)
    print(msg)

create_mail('山本', 40000)

def add_charge(bill) :
    return int(bill * 1.07)

print(add_charge(40000))