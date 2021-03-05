import re

def allTrue():

    my_file=open("calc.in")

    all_list=[]

    for line in my_file:
        stripped_line=line.strip()
        if(stripped_line!=[]):
            all_list.append(stripped_line)

    isContain=True
    while(isContain):
        if('' in all_list):
            all_list.remove("")
        else:
            isContain=False

    if ("AnaDegiskenler" not in all_list):

        return True

    if  ("Sonuc" not in all_list):
        return True

    if ("YeniDegiskenler" not in all_list):
        return True

    if(all_list[0]!="AnaDegiskenler"):
        return True

    #print(all_list)



    indexOfAD=all_list.index("AnaDegiskenler")

    indexOfYD=all_list.index("YeniDegiskenler")

    initStatements=all_list[indexOfAD+1:indexOfYD]

    #print(initStatements)

    Initdict=dict()
    valuesDict=dict()
    typeDict=dict()
    for elemInit in initStatements:

        stripped_elemInit=elemInit.split()

        if (len(stripped_elemInit) <= 3):
            return True


        if(stripped_elemInit[1]!="degeri"):
            return True

        if(stripped_elemInit[-1]!="olsun"):
            return True
        if(stripped_elemInit[-2]=="olsun"):
            return True

        regex_list=re.findall("(.+)degeri(.+)olsun",elemInit)

        var=regex_list[0][0]
        var=var.strip()
        ascii_list = []
        for ascnmb in range(48, 58):
            ascii_list.append(ascnmb)
        for ascnmb in range(65, 91):
            ascii_list.append(ascnmb)
        for ascnmb in range(97, 123):
            ascii_list.append(ascnmb)

        for elemvar in var:
            if (ord(elemvar) not in ascii_list):
                return True
        val=regex_list[0][1]
        val=val.strip()
        #print(var)

        #print(val)

        if(len(var)>10):
            return True

        Initdict[var]=Initdict.get(var,0)+1
        valuesDict[var]=val

        valValidator=False

        if(val=="0" or val=="1" or val=="2" or val=="3"or val=="4" or val=="5" or val=="6" or val=="7" or val=="8" or val=="9"):
            valValidator=True
            typeDict[var]="sayi"
        if val=="sifir" or val=="bir" or val=="iki" or val=="uc"or val=="dort" or val=="bes" or val=="alti" or val=="yedi" or val=="sekiz" or val=="dokuz":
            valValidator=True
            typeDict[var] = "sayi"
        if val=="dogru" or val=="yanlis":
            valValidator=True
            typeDict[var] = "boolean"


        if((len(val)==3) and(val[0]=="0" or val[0]=="1" or val[0]=="2"
                                      or val[0]=="3"or val[0]=="4" or val[0]=="5"
                                      or val[0]=="6" or val[0]=="7" or val[0]=="8" or val[0]=="9") and (val[1]==".") and
                    (val[2]=="0" or val[2]=="1" or val[2]=="2"
                                      or val[2]=="3"or val[2]=="4" or val[2]=="5"
                                      or val[2]=="6" or val[2]=="7" or val[2]=="8" or val[2]=="9")):
            valValidator=True
            typeDict[var] = "sayi"


        if("nokta" in val):
            val_list=val.split()

            if(len(val_list)==3 and (val_list[0]=="sifir" or val_list[0]=="bir" or val_list[0]=="iki"
                                      or val_list[0]=="uc"or val_list[0]=="dort" or val_list[0]=="bes"
                                      or val_list[0]=="alti" or val_list[0]=="yedi" or val_list[0]=="sekiz" or val_list[0]=="dokuz") and (val_list[1]=="nokta") and
                    (val_list[2]=="sifir" or val_list[2]=="bir" or val_list[2]=="iki"
                                      or val_list[2]=="uc"or val_list[2]=="dort" or val_list[2]=="bes"
                                      or val_list[2]=="alti" or val_list[2]=="yedi" or val_list[2]=="sekiz" or val_list[2]=="dokuz")):
                valValidator=True
                typeDict[var] = "sayi"


        #print(valValidator)


        if(valValidator==False):
            return True

    indexOfS=all_list.index("Sonuc")

    mid_statements=all_list[indexOfYD+1:indexOfS]

    #print(mid_statements)


    for elemMid in mid_statements:

        stripped_elemMid=elemMid.split()

        if(len(stripped_elemMid)<=3):
            return True

        if(stripped_elemMid[1]!="degeri"):
            return True

        if(stripped_elemMid[-1]!="olsun"):
            return True

        if (stripped_elemInit[-2] == "olsun"):
            return True


        regex_listMS = re.findall("(.+)degeri(.+)olsun", elemMid)

        #print(regex_listMS)
        varMS = regex_listMS[0][0]
        varMS = varMS.strip()
        ascii_listMS=[]
        for ascnmbMS in range(48,58):
            ascii_listMS.append(ascnmbMS)
        for ascnmbMS in range(65,91):
            ascii_listMS.append(ascnmbMS)
        for ascnmbMS in range(97, 123):
            ascii_listMS.append(ascnmbMS)

        for elemvarMS in varMS:
            if(ord(elemvarMS) not in ascii_listMS):
                return True



        valMS = regex_listMS[0][1]
        valMS = valMS.strip()
        #print(varMS)

        #print(valMS)

        value_of_val_ms=valMS.split()
        #print(value_of_val_ms)

        for elemlistMs in range(0,len(value_of_val_ms)-1):
            if((value_of_val_ms[elemlistMs]=="(" or value_of_val_ms[elemlistMs]=="ac-parantez") and
            (value_of_val_ms[elemlistMs+1]==")" or value_of_val_ms[elemlistMs+1]=="kapa-parantez")):
                return True

        nbrofsolp=0  #number of sol parantez
        nbrofsagp = 0    #number of sag parantez
        indexofsolp=[0]
        indexofsagp = [0]
        for elemofvovm in range(0,len(value_of_val_ms)):
            if(value_of_val_ms[elemofvovm]=="(" or value_of_val_ms[elemofvovm]=="ac-parantez"):
                nbrofsolp = nbrofsolp+1
                indexofsolp.append(elemofvovm)

            if (value_of_val_ms[elemofvovm] == ")" or value_of_val_ms[elemofvovm] == "kapa-parantez"):
                nbrofsagp = nbrofsagp+1
                indexofsagp.append(elemofvovm)

        #print(indexofsagp)

        #print(indexofsolp)

        if(sum(indexofsolp)>sum(indexofsagp)):
            return True

        if(nbrofsolp!=nbrofsagp):
            return True

        for elemindexfp in range(1, len(indexofsagp)):
            if(indexofsagp[elemindexfp]<indexofsolp[elemindexfp]):
                return True



        isContainpar = True
        while (isContainpar):
            if ("(" in value_of_val_ms):
                value_of_val_ms.remove("(")

            elif (")" in value_of_val_ms):
                value_of_val_ms.remove(")")

            elif ("ac-parantez" in value_of_val_ms):
                value_of_val_ms.remove("ac-parantez")

            elif ("kapa-parantez" in value_of_val_ms):
                value_of_val_ms.remove("kapa-parantez")
            else:
                isContainpar = False

        #print(value_of_val_ms)


        if(len(value_of_val_ms)==0 or len(value_of_val_ms)==2):
            return True



        str_is_expression = ""

        for elemisexpress in value_of_val_ms:
            str_is_expression += elemisexpress

        #print(str_is_expression)
        splitted_str_is_expression=""
        splitted_str_numerical_is_expression = ""
        #print(Initdict)
        #print(typeDict)

        if("ve" in value_of_val_ms or "veya" in value_of_val_ms):
            if("ve" in value_of_val_ms):
                if(value_of_val_ms.index("ve")==0 or value_of_val_ms.index("ve")==len(value_of_val_ms)-1):
                    return True

            if ("veya" in value_of_val_ms):
                if (value_of_val_ms.index("veya") == 0 or value_of_val_ms.index("veya") == len(value_of_val_ms) - 1):
                    return True

            var_is_contain=False

            for dictinitelem in Initdict.keys():
                if("ve" in dictinitelem or "veya" in dictinitelem):
                    var_is_contain=True

            #print(var_is_contain)
            #print(str_is_expression)
            #print(Initdict.keys())
            if(var_is_contain==False):
                splitted_str_is_expression = re.split("veya|ve",str_is_expression)

            else:
                for errorelem in range(0,len(value_of_val_ms)-1):
                    if((value_of_val_ms[errorelem]=="veya" or value_of_val_ms[errorelem]=="ve") and
                    (value_of_val_ms[errorelem+1]=="veya" or value_of_val_ms[errorelem+1]=="ve")):
                        return True

                isContainve = True
                while (isContainve):
                    if ("ve" in value_of_val_ms):
                        value_of_val_ms.remove("ve")

                    elif ("veya" in value_of_val_ms):
                        value_of_val_ms.remove("veya")

                    else:
                        isContainve = False

                splitted_str_is_expression=value_of_val_ms.copy()

            #print(splitted_str_is_expression)


            for elem_splitted_str in splitted_str_is_expression:
                #print(elem_splitted_str)

                is_logicalexpression_true = False
                #print(is_logicalexpression_true)
                if(elem_splitted_str=="dogru" or elem_splitted_str=="yanlis" or elem_splitted_str=="nlis"):
                    is_logicalexpression_true=True
                elif(elem_splitted_str in typeDict):
                    if(typeDict[elem_splitted_str]=="boolean"):
                        is_logicalexpression_true=True

                #print(is_logicalexpression_true)
                if(is_logicalexpression_true==False):
                    return True

                typeDict[varMS]="boolean"



        elif("+" in value_of_val_ms or "-" in value_of_val_ms or "*" in value_of_val_ms or
        "arti" in value_of_val_ms or "eksi" in value_of_val_ms or "carpi" in value_of_val_ms or "nokta" in value_of_val_ms
        or "." in value_of_val_ms):
            if ("+" in value_of_val_ms):
                if (value_of_val_ms.index("+") == 0 or value_of_val_ms.index("+") == len(value_of_val_ms) - 1):
                    return True

            if ("-" in value_of_val_ms):
                if (value_of_val_ms.index("-") == 0 or value_of_val_ms.index("-") == len(value_of_val_ms) - 1):
                    return True

            if ("*" in value_of_val_ms):
                if (value_of_val_ms.index("*") == 0 or value_of_val_ms.index("*") == len(value_of_val_ms) - 1):
                    return True

            if ("arti" in value_of_val_ms):
                if (value_of_val_ms.index("arti") == 0 or value_of_val_ms.index("arti") == len(value_of_val_ms) - 1):
                    return True

            if ("eksi" in value_of_val_ms):
                if (value_of_val_ms.index("eksi") == 0 or value_of_val_ms.index("eksi") == len(value_of_val_ms) - 1):
                    return True

            if ("carpi" in value_of_val_ms):
                if (value_of_val_ms.index("carpi") == 0 or value_of_val_ms.index("carpi") == len(value_of_val_ms) - 1):
                    return True

            splitted_str_numerical_is_expression = re.split("\+|-|\*|arti|eksi|carpi", str_is_expression)

            for elem_splitted_numerical_str in splitted_str_numerical_is_expression:

                #print(elem_splitted_numerical_str)
                is_numericalexpression_true = False
                if (elem_splitted_numerical_str == "0" or elem_splitted_numerical_str == "1" or elem_splitted_numerical_str == "2"
                        or elem_splitted_numerical_str == "3" or elem_splitted_numerical_str == "4"
                        or elem_splitted_numerical_str == "5" or
                        elem_splitted_numerical_str== "6" or elem_splitted_numerical_str == "7" or
                        elem_splitted_numerical_str == "8" or elem_splitted_numerical_str == "9"):
                    is_numericalexpression_true=True
                elif (elem_splitted_numerical_str == "sifir" or elem_splitted_numerical_str == "bir" or elem_splitted_numerical_str == "iki"
                        or elem_splitted_numerical_str == "uc" or elem_splitted_numerical_str == "dort"
                        or elem_splitted_numerical_str == "bes" or
                        elem_splitted_numerical_str== "alti" or elem_splitted_numerical_str == "yedi" or
                        elem_splitted_numerical_str == "sekiz" or elem_splitted_numerical_str == "dokuz"):
                    is_numericalexpression_true=True

                elif (elem_splitted_numerical_str in typeDict):
                    if (typeDict[elem_splitted_numerical_str] == "sayi"):
                        is_numericalexpression_true = "True"

                if(is_numericalexpression_true==False and "nokta" in elem_splitted_numerical_str):
                    splitted_elem_splitted=elem_splitted_numerical_str.split("nokta")
                    if ( (splitted_elem_splitted[0] == "sifir" or splitted_elem_splitted[0] == "bir" or splitted_elem_splitted[0] == "iki"
                                                or splitted_elem_splitted[0] == "uc" or splitted_elem_splitted[0] == "dort" or splitted_elem_splitted[0] == "bes"
                                                or splitted_elem_splitted[0] == "alti" or splitted_elem_splitted[0] == "yedi" or splitted_elem_splitted[
                                                    0] == "sekiz" or splitted_elem_splitted[0] == "dokuz") and
                            (splitted_elem_splitted[1] == "sifir" or splitted_elem_splitted[1] == "bir" or splitted_elem_splitted[1] == "iki"
                             or splitted_elem_splitted[1] == "uc" or splitted_elem_splitted[1] == "dort" or splitted_elem_splitted[1] == "bes"
                             or splitted_elem_splitted[1] == "alti" or splitted_elem_splitted[1] == "yedi" or splitted_elem_splitted[1] == "sekiz" or splitted_elem_splitted[
                                 1] == "dokuz")):
                        is_numericalexpression_true=True

                if (is_numericalexpression_true == False and "." in elem_splitted_numerical_str):
                    splitted_elem_splitted = elem_splitted_numerical_str.split(".")
                    if ((splitted_elem_splitted[0] == "0" or splitted_elem_splitted[0] == "1" or
                         splitted_elem_splitted[0] == "2"
                         or splitted_elem_splitted[0] == "3" or splitted_elem_splitted[0] == "4" or
                         splitted_elem_splitted[0] == "5"
                         or splitted_elem_splitted[0] == "6" or splitted_elem_splitted[0] == "7" or
                         splitted_elem_splitted[
                             0] == "8" or splitted_elem_splitted[0] == "9") and
                            (splitted_elem_splitted[1] == "0" or splitted_elem_splitted[1] == "1" or
                             splitted_elem_splitted[1] == "2"
                             or splitted_elem_splitted[1] == "3" or splitted_elem_splitted[1] == "4" or
                             splitted_elem_splitted[1] == "5"
                             or splitted_elem_splitted[1] == "6" or splitted_elem_splitted[1] == "7" or
                             splitted_elem_splitted[1] == "8" or splitted_elem_splitted[
                                 1] == "9")):
                        is_numericalexpression_true = True

                if (is_numericalexpression_true == False):
                    return True

                typeDict[varMS] = "sayi"

        elif(len(value_of_val_ms)==1):
            is_onlyexpression_true = False
            if (
                    value_of_val_ms[0] == "0" or value_of_val_ms[0] == "1" or value_of_val_ms[0] == "2"
                    or value_of_val_ms[0] == "3" or value_of_val_ms[0]== "4" or value_of_val_ms[0] == "5"
                    or value_of_val_ms[0] == "6" or value_of_val_ms[0] == "7" or value_of_val_ms[0] == "8" or value_of_val_ms[0] == "9"):
                is_onlyexpression_true=True
                typeDict[varMS]="sayi"

            if (
                    value_of_val_ms[0] == "sifir" or value_of_val_ms[0] == "bir" or value_of_val_ms[0] == "iki"
                    or value_of_val_ms[0] == "uc" or value_of_val_ms[0] == "dort" or value_of_val_ms[0] == "bes"
                    or value_of_val_ms[0] == "alti" or value_of_val_ms[0] == "yedi" or value_of_val_ms[0] == "sekiz" or
                    value_of_val_ms[0] == "dokuz"):
                is_onlyexpression_true = True
                typeDict[varMS] = "sayi"

            if value_of_val_ms[0] == "dogru" or value_of_val_ms[0] == "yanlis":

                is_onlyexpression_true=True
                typeDict[varMS] = "boolean"

            if(value_of_val_ms[0] in typeDict):
                is_onlyexpression_true=True
                typeDict[varMS] =typeDict[value_of_val_ms[0]]

            if ( "nokta" in value_of_val_ms[0]):
                splitted_elem_splitted = value_of_val_ms[0].split("nokta")
                if ((splitted_elem_splitted[0] == "sifir" or splitted_elem_splitted[0] == "bir" or
                     splitted_elem_splitted[0] == "iki"
                     or splitted_elem_splitted[0] == "uc" or splitted_elem_splitted[0] == "dort" or
                     splitted_elem_splitted[0] == "bes"
                     or splitted_elem_splitted[0] == "alti" or splitted_elem_splitted[0] == "yedi" or
                     splitted_elem_splitted[
                         0] == "sekiz" or splitted_elem_splitted[0] == "dokuz") and
                        (splitted_elem_splitted[1] == "sifir" or splitted_elem_splitted[1] == "bir" or
                         splitted_elem_splitted[1] == "iki"
                         or splitted_elem_splitted[1] == "uc" or splitted_elem_splitted[1] == "dort" or
                         splitted_elem_splitted[1] == "bes"
                         or splitted_elem_splitted[1] == "alti" or splitted_elem_splitted[1] == "yedi" or
                         splitted_elem_splitted[1] == "sekiz" or splitted_elem_splitted[
                             1] == "dokuz")):
                    is_onlyexpression_true = True
                    typeDict[varMS] = "sayi"

            if ( "." in value_of_val_ms[0]):
                splitted_elem_splitted = value_of_val_ms[0].split(".")
                if ((splitted_elem_splitted[0] == "0" or splitted_elem_splitted[0] == "1" or
                     splitted_elem_splitted[0] == "2"
                     or splitted_elem_splitted[0] == "3" or splitted_elem_splitted[0] == "4" or
                     splitted_elem_splitted[0] == "5"
                     or splitted_elem_splitted[0] == "6" or splitted_elem_splitted[0] == "7" or
                     splitted_elem_splitted[
                         0] == "8" or splitted_elem_splitted[0] == "9") and
                        (splitted_elem_splitted[1] == "0" or splitted_elem_splitted[1] == "1" or
                         splitted_elem_splitted[1] == "2"
                         or splitted_elem_splitted[1] == "3" or splitted_elem_splitted[1] == "4" or
                         splitted_elem_splitted[1] == "5"
                         or splitted_elem_splitted[1] == "6" or splitted_elem_splitted[1] == "7" or
                         splitted_elem_splitted[1] == "8" or splitted_elem_splitted[
                             1] == "9")):
                    is_onlyexpression_true = True
                    typeDict[varMS] = "sayi"

            if(is_onlyexpression_true==False):
                return True

        if(len(varMS)>10):
            return True
        #print("kabadayı")



        Initdict[varMS]=Initdict.get(varMS,0)+1
        valuesDict[varMS] = valMS

    final_statements = all_list[indexOfS + 1:]
    #print(final_statements)


    for elemFinal in final_statements:


        value_of_val_fs=elemFinal.split()
        #print(value_of_val_fs)

        for elemlistfs in range(0,len(value_of_val_fs)-1):
            if((value_of_val_fs[elemlistfs]=="(" or value_of_val_fs[elemlistfs]=="ac-parantez") and
            (value_of_val_fs[elemlistfs+1]==")" or value_of_val_fs[elemlistfs+1]=="kapa-parantez")):
                return True

        nbrofsolp=0  #number of sol parantez
        nbrofsagp= 0    #number of sag parantez
        indexofsolp=[0]
        indexofsagp= [0]
        for elemofvovf in range(0,len(value_of_val_fs)):
            if(value_of_val_fs[elemofvovf]=="(" or value_of_val_fs[elemofvovf]=="ac-parantez"):
                nbrofsolp = nbrofsolp+1
                indexofsolp.append(elemofvovf)

            if (value_of_val_fs[elemofvovf] == ")" or value_of_val_fs[elemofvovf] == "kapa-parantez"):
                nbrofsagp = nbrofsagp+1
                indexofsagp.append(elemofvovf)

        #print(indexofsagp)

        #print(indexofsolp)

        #print(nbrofsagp)

        #print(nbrofsolp)

        if(sum(indexofsolp)>sum(indexofsagp)):
            return True



        if(nbrofsolp!=nbrofsagp):
            return True



        for elemindexfp in range(1, len(indexofsagp)):
            if(indexofsagp[elemindexfp]<indexofsolp[elemindexfp]):
                return True



        isContainparf = True
        while (isContainparf):
            if ("(" in value_of_val_fs):
                value_of_val_fs.remove("(")

            elif (")" in value_of_val_fs):
                value_of_val_fs.remove(")")

            elif ("ac-parantez" in value_of_val_fs):
                value_of_val_fs.remove("ac-parantez")

            elif ("kapa-parantez" in value_of_val_fs):
                value_of_val_fs.remove("kapa-parantez")
            else:
                isContainparf = False

        #print(value_of_val_fs)

        if(len(value_of_val_fs)==0 or len(value_of_val_fs)==2):
            return True

        str_is_expression = ""

        for elemisexpress in value_of_val_fs:
            str_is_expression += elemisexpress

        #print(str_is_expression)
        splitted_str_is_expression=""
        splitted_str_numerical_is_expression = ""



        if("ve" in value_of_val_fs or "veya" in value_of_val_fs):
            if("ve" in value_of_val_fs):
                if(value_of_val_fs.index("ve")==0 or value_of_val_fs.index("ve")==len(value_of_val_fs)-1):
                    return True

            if ("veya" in value_of_val_fs):
                if (value_of_val_fs.index("veya") == 0 or value_of_val_fs.index("veya") == len(value_of_val_fs) - 1):
                    return True

            var_is_contain = False

            for dictinitelem in Initdict.keys():
                if ("ve" in dictinitelem or "veya" in dictinitelem):
                    var_is_contain = True

            #print(var_is_contain)
            # print(str_is_expression)
            # print(Initdict.keys())
            if (var_is_contain == False):
                splitted_str_is_expression = re.split("veya|ve", str_is_expression)

            else:
                for errorelem in range(0, len(value_of_val_fs) - 1):
                    if ((value_of_val_fs[errorelem] == "veya" or value_of_val_fs[errorelem] == "ve") and
                            (value_of_val_fs[errorelem + 1] == "veya" or value_of_val_fs[errorelem + 1] == "ve")):
                        return True

                isContainve = True
                while (isContainve):
                    if ("ve" in value_of_val_fs):
                        value_of_val_fs.remove("ve")

                    elif ("veya" in value_of_val_fs):
                        value_of_val_fs.remove("veya")

                    else:
                        isContainve = False

                splitted_str_is_expression = value_of_val_fs.copy()

            #print(splitted_str_is_expression)

            #print(splitted_str_is_expression)

            for elem_splitted_str in splitted_str_is_expression:
                is_logicalexpression_true = False
                if(elem_splitted_str=="dogru" or elem_splitted_str=="yanlis" or elem_splitted_str=="nlis"):
                    is_logicalexpression_true=True
                elif(elem_splitted_str in typeDict):
                    if(typeDict[elem_splitted_str]=="boolean"):
                        is_logicalexpression_true=True


                if(is_logicalexpression_true==False):
                    return True



        elif("+" in value_of_val_fs or "-" in value_of_val_fs or "*" in value_of_val_fs or
        "arti" in value_of_val_fs or "eksi" in value_of_val_fs or "carpi" in value_of_val_fs or "nokta" in value_of_val_fs
        or "." in value_of_val_fs ):
            if ("+" in value_of_val_fs):
                if (value_of_val_fs.index("+") == 0 or value_of_val_fs.index("+") == len(value_of_val_fs) - 1):
                    return True

            if ("-" in value_of_val_fs):
                if (value_of_val_fs.index("-") == 0 or value_of_val_fs.index("-") == len(value_of_val_fs) - 1):
                    return True

            if ("*" in value_of_val_fs):
                if (value_of_val_fs.index("*") == 0 or value_of_val_fs.index("*") == len(value_of_val_fs) - 1):
                    return True

            if ("arti" in value_of_val_fs):
                if (value_of_val_fs.index("arti") == 0 or value_of_val_fs.index("arti") == len(value_of_val_fs) - 1):
                    return True

            if ("eksi" in value_of_val_fs):
                if (value_of_val_fs.index("eksi") == 0 or value_of_val_fs.index("eksi") == len(value_of_val_fs) - 1):
                    return True

            if ("carpi" in value_of_val_fs):
                if (value_of_val_fs.index("carpi") == 0 or value_of_val_fs.index("carpi") == len(value_of_val_fs) - 1):
                    return True

            splitted_str_numerical_is_expression = re.split("\+|-|\*|arti|eksi|carpi", str_is_expression)

            #print(splitted_str_numerical_is_expression)

            for elem_splitted_numerical_str in splitted_str_numerical_is_expression:
                is_numericalexpression_true = False
                if (elem_splitted_numerical_str == "0" or elem_splitted_numerical_str == "1" or elem_splitted_numerical_str == "2"
                        or elem_splitted_numerical_str == "3" or elem_splitted_numerical_str == "4"
                        or elem_splitted_numerical_str == "5" or
                        elem_splitted_numerical_str== "6" or elem_splitted_numerical_str == "7" or
                        elem_splitted_numerical_str == "8" or elem_splitted_numerical_str == "9"):
                    is_numericalexpression_true=True
                elif (elem_splitted_numerical_str == "sifir" or elem_splitted_numerical_str == "bir" or elem_splitted_numerical_str == "iki"
                        or elem_splitted_numerical_str == "uc" or elem_splitted_numerical_str == "dort"
                        or elem_splitted_numerical_str == "bes" or
                        elem_splitted_numerical_str== "alti" or elem_splitted_numerical_str == "yedi" or
                        elem_splitted_numerical_str == "sekiz" or elem_splitted_numerical_str == "dokuz"):
                    is_numericalexpression_true=True

                elif (elem_splitted_numerical_str in typeDict):
                    if (typeDict[elem_splitted_numerical_str] == "sayi"):
                        is_numericalexpression_true = "True"

                if(is_numericalexpression_true==False and "nokta" in elem_splitted_numerical_str):
                    splitted_elem_splitted=elem_splitted_numerical_str.split("nokta")
                    if ( (splitted_elem_splitted[0] == "sifir" or splitted_elem_splitted[0] == "bir" or splitted_elem_splitted[0] == "iki"
                                                or splitted_elem_splitted[0] == "uc" or splitted_elem_splitted[0] == "dort" or splitted_elem_splitted[0] == "bes"
                                                or splitted_elem_splitted[0] == "alti" or splitted_elem_splitted[0] == "yedi" or splitted_elem_splitted[
                                                    0] == "sekiz" or splitted_elem_splitted[0] == "dokuz") and
                            (splitted_elem_splitted[1] == "sifir" or splitted_elem_splitted[1] == "bir" or splitted_elem_splitted[1] == "iki"
                             or splitted_elem_splitted[1] == "uc" or splitted_elem_splitted[1] == "dort" or splitted_elem_splitted[1] == "bes"
                             or splitted_elem_splitted[1] == "alti" or splitted_elem_splitted[1] == "yedi" or splitted_elem_splitted[1] == "sekiz" or splitted_elem_splitted[
                                 1] == "dokuz")):
                        is_numericalexpression_true=True

                if (is_numericalexpression_true == False and "." in elem_splitted_numerical_str):
                    splitted_elem_splitted = elem_splitted_numerical_str.split(".")
                    if ((splitted_elem_splitted[0] == "0" or splitted_elem_splitted[0] == "1" or
                         splitted_elem_splitted[0] == "2"
                         or splitted_elem_splitted[0] == "3" or splitted_elem_splitted[0] == "4" or
                         splitted_elem_splitted[0] == "5"
                         or splitted_elem_splitted[0] == "6" or splitted_elem_splitted[0] == "7" or
                         splitted_elem_splitted[
                             0] == "8" or splitted_elem_splitted[0] == "9") and
                            (splitted_elem_splitted[1] == "0" or splitted_elem_splitted[1] == "1" or
                             splitted_elem_splitted[1] == "2"
                             or splitted_elem_splitted[1] == "3" or splitted_elem_splitted[1] == "4" or
                             splitted_elem_splitted[1] == "5"
                             or splitted_elem_splitted[1] == "6" or splitted_elem_splitted[1] == "7" or
                             splitted_elem_splitted[1] == "8" or splitted_elem_splitted[
                                 1] == "9")):
                        is_numericalexpression_true = True

                if (is_numericalexpression_true == False):
                    return True



        elif(len(value_of_val_fs)==1):
            is_onlyexpression_true = False
            if (
                    value_of_val_fs[0] == "0" or value_of_val_fs[0] == "1" or value_of_val_fs[0] == "2"
                    or value_of_val_fs[0] == "3" or value_of_val_fs[0]== "4" or value_of_val_fs[0] == "5"
                    or value_of_val_fs[0] == "6" or value_of_val_fs[0] == "7" or value_of_val_fs[0] == "8" or value_of_val_fs[0] == "9"):
                is_onlyexpression_true=True


            if (
                    value_of_val_fs[0] == "sifir" or value_of_val_fs[0] == "bir" or value_of_val_fs[0] == "iki"
                    or value_of_val_fs[0] == "uc" or value_of_val_fs[0] == "dort" or value_of_val_fs[0] == "bes"
                    or value_of_val_fs[0] == "alti" or value_of_val_fs[0] == "yedi" or value_of_val_fs[0] == "sekiz" or
                    value_of_val_fs[0] == "dokuz"):
                is_onlyexpression_true = True


            if value_of_val_fs[0] == "dogru" or value_of_val_fs[0] == "yanlis":

                is_onlyexpression_true=True


            if(value_of_val_fs[0] in typeDict):
                is_onlyexpression_true=True


            if ( "nokta" in value_of_val_fs[0]):
                splitted_elem_splitted = value_of_val_fs[0].split("nokta")
                if ((splitted_elem_splitted[0] == "sifir" or splitted_elem_splitted[0] == "bir" or
                     splitted_elem_splitted[0] == "iki"
                     or splitted_elem_splitted[0] == "uc" or splitted_elem_splitted[0] == "dort" or
                     splitted_elem_splitted[0] == "bes"
                     or splitted_elem_splitted[0] == "alti" or splitted_elem_splitted[0] == "yedi" or
                     splitted_elem_splitted[
                         0] == "sekiz" or splitted_elem_splitted[0] == "dokuz") and
                        (splitted_elem_splitted[1] == "sifir" or splitted_elem_splitted[1] == "bir" or
                         splitted_elem_splitted[1] == "iki"
                         or splitted_elem_splitted[1] == "uc" or splitted_elem_splitted[1] == "dort" or
                         splitted_elem_splitted[1] == "bes"
                         or splitted_elem_splitted[1] == "alti" or splitted_elem_splitted[1] == "yedi" or
                         splitted_elem_splitted[1] == "sekiz" or splitted_elem_splitted[
                             1] == "dokuz")):
                    is_onlyexpression_true = True


            if ( "." in value_of_val_fs[0]):
                splitted_elem_splitted = value_of_val_fs[0].split(".")
                if ((splitted_elem_splitted[0] == "0" or splitted_elem_splitted[0] == "1" or
                     splitted_elem_splitted[0] == "2"
                     or splitted_elem_splitted[0] == "3" or splitted_elem_splitted[0] == "4" or
                     splitted_elem_splitted[0] == "5"
                     or splitted_elem_splitted[0] == "6" or splitted_elem_splitted[0] == "7" or
                     splitted_elem_splitted[
                         0] == "8" or splitted_elem_splitted[0] == "9") and
                        (splitted_elem_splitted[1] == "0" or splitted_elem_splitted[1] == "1" or
                         splitted_elem_splitted[1] == "2"
                         or splitted_elem_splitted[1] == "3" or splitted_elem_splitted[1] == "4" or
                         splitted_elem_splitted[1] == "5"
                         or splitted_elem_splitted[1] == "6" or splitted_elem_splitted[1] == "7" or
                         splitted_elem_splitted[1] == "8" or splitted_elem_splitted[
                             1] == "9")):
                    is_onlyexpression_true = True


            if(is_onlyexpression_true==False):
                return True







    #print(Initdict)
    #print(valuesDict)
    #print(typeDict)

    for keyy,vall in Initdict.items():
        if(vall!=1):
            return True
        if(keyy=="Anadegiskenler"):
            return True
        if (keyy == "Yenidegiskenler"):
            return True
        if (keyy == "Sonuc"):
            return True
        if ( keyy == "0" or keyy == "1" or keyy == "2" or keyy == "3" or keyy == "4" or keyy == "5" or keyy == "6" or keyy == "7" or keyy == "8" or keyy == "9"):
            valValidator = True
        if keyy == "sifir" or keyy == "bir" or keyy == "iki" or keyy == "uc" or keyy == "dort" or keyy == "bes" or keyy == "alti" or keyy == "yedi" or keyy == "sekiz" or keyy == "dokuz":
            valValidator = True
        if keyy == "dogru" or keyy == "yanlis":
            valValidator = True
        if(keyy=="+" or keyy=="-" or keyy=="*" or keyy=="/" or keyy=="eksi" or keyy=="bolu" or keyy=="arti" or keyy=="carpi"):
            return True
        if(keyy=="ve" or keyy=="veya" or keyy=="olsun" or keyy=="nokta" or keyy=="degeri" or keyy=="ac-parantez" or keyy=="kapa-parantez" ):
            return True



    my_file.close()

Valueis=allTrue()
if(Valueis==True):
    totol_file=open("calc.out", "w")
    totol_file.write("Dont Let Me Down")
    totol_file.close()
else:
    totol_file = open("calc.out", "w")
    totol_file.write("Here Comes the Sun")
    totol_file.close()