numero=int(input("DIGITE UM NUMERO -999"))
if numero<=999 and numero >99:
    cent = numero//100
    dec = numero//10
    uni = (dec*10)-numero
    if uni >1 and dec > 1 and cent < 1:
        print("UNIDADES {} DEZENAS {} CENTENAS {}".format(abs(uni), dec, cent))
    elif uni ==1 and dec > 1 and cent < 1:
        print("UNIDADE {} DEZENAS {} CENTENAS {}".format(abs(uni), dec, cent))
    elif uni ==1 and dec == 1 and cent < 1:
        print("UNIDADE {} DEZENA {} CENTENAS {}".format(abs(uni), dec, cent))
    elif uni ==1 and dec == 1 and cent == 1:
        print("UNIDADE {} DEZENAS {} CENTENAS {}".format(abs(uni), dec, cent))
if numero<99 and numero >10:
    dec = numero // 10
    uni = (dec * 10) - numero
    if uni >1 and dec > 1 :
        print("UNIDADES {} DEZENAS {}".format(abs(uni), dec))
    elif uni ==1 and dec ==1:
        print("UNIDADE {} DEZENA {}".format(abs(uni), dec))
    elif uni>1 and dec==0:
        print("UNIDADES {} DEZENA {}".format(abs(uni), dec))
    elif uni==1 and dec==1:
        print("UNIDADE {} DEZENAS {}".format(abs(uni), dec))
if numero<=9:
    uni=numero
    if numero >1:
        print("UNIDADES: ",abs(uni))
    elif numero ==1:
        print("UNIDADE: ", abs(uni))


