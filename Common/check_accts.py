# from Common.random_number import *
# caccts=Randoms().choice_accts()

def check_accts(accts):
    if accts=="leveragedForeignExchangeAccountMargin":
        busin_acty_cde="FOREX"
    elif accts=="futuresMargin":
        busin_acty_cde = "FUTURES"
    else:
        busin_acty_cde = "EQUITIES"
    return busin_acty_cde

if __name__=="__main__":
    accts="securitiesAyersCash"
    print("账户类型为：",check_accts(accts))