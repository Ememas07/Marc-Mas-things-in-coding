Afirmacions = ["Si","si","Seh","seh","sip","Sip","Yes","yes"]
print("nota: Aquí tens totes les maneres de afirmar les preguntes, i, si vols aturar, basta diguis 'atura' en qualsevol moment")
print(Afirmacions)
Aturada = ["Atura","atura","stop","Stop"]
Negacions = ["No","no","Nah","nah"]
Noms = ["Marc", "Pere"]
print("Noms acceptats:",Noms)
##Approval=input("vols continuar? ")
while "si" in Afirmacions:
   
    

    

    nombre=input("Com te noms?")
    if nombre in Noms:
        print("hola",nombre)
    else:
        if nombre in Aturada:
            print("Aturant Projecte...")
            break
        else:

            llista=input("No sé qui ets,voldires afegir-te a la llista?")
            if  llista in Afirmacions:
                Noms.append(nombre)
                print("ja està")
                print("la llista ara és:",Noms)
            else:
                if(llista in Aturada):
                    print("Aturant Projecte...")
                    break
                else:
                    print("val")
    ##Approval=input("vols continuar? ")
        