

cod = 0

while(cod <= 254):
    
    if cod <= 24:
        print ("Código: ", cod+1, " | Símbolo invisível", chr(cod+1))
        
    else:
        print("Código: ", cod+1, " | ", chr(cod+1))
        
    cod += 1
    
    if cod % 20 == 0:
        
        print()
        opc = input("Deseja visualizar os próximos 20 códigos? Prima S para sim ou carregue em qualquer tecla para sair: ")
        print()

        if opc != "S":
            print("Ok, até à próxima!")
            break


