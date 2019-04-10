numero=int(input("DIGITE UM NUMERO -999"))
if numero<=999 and numero >99:
    cent = numero//100
    dec = numero//10
    uni = (dec*10)-numero
    print("UNIDADE {} DEZENAS {} CENTENAS {}".format(abs(uni), dec, cent))
if numero<99 and numero >10:
    dec = numero // 10
    uni = (dec * 10) - numero
    print("UNIDADE {} DEZENAS {}".format(abs(uni), dec))
if numero<=9:
    uni=numero
    print("UNIDADE :",abs(uni))






