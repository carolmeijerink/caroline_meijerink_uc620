aluno1= 12
aluno2= 15
aluno3= 18
aluno4= 17
aluno5= 13
aluno6= 16
aluno7= 17
aluno8= 17
aluno9= 16
aluno10= 13

media = (aluno1+aluno2+aluno3+aluno4+aluno5+aluno6+aluno7+aluno8+aluno9+aluno10) / 10

quant_acima_media=0

if aluno1>=media:
    quant_acima_media = quant_acima_media + 1
    
if aluno2>=media:
    quant_acima_media = quant_acima_media + 1

if aluno3>=media:
    quant_acima_media = quant_acima_media + 1

if aluno4>=media:
    quant_acima_media = quant_acima_media + 1

if aluno5>=media:
    quant_acima_media = quant_acima_media + 1

if aluno6>=media:
    quant_acima_media = quant_acima_media + 1

if aluno7>=media:
    quant_acima_media = quant_acima_media + 1

if aluno8>=media:
    quant_acima_media = quant_acima_media + 1

if aluno9>=media:
    quant_acima_media = quant_acima_media + 1

if aluno10>=media:
    quant_acima_media = quant_acima_media + 1

print(f"A média é {media}. {quant_acima_media} aluno(s) ficou(aram) acima da média.")