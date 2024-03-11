# https://www.youtube.com/watch?v=vq-nUF0G4fI&ab_channel=mycodeschool     <-> do powtorzenia przed matura, w tym filmie jest dokladnie wytlumaczone

operator = {
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '^':3
}

# jezeli symbol ktory ma byc dodany na stos jest symbolem o wiekszym znaczeniu (popatrz na operator) niz ten co juz jest na stosie -> dodajemy go na stos
# jezeli symbol ktory ma byc dodany na stos jest symbolem o tym samym badz mniejszym znaczeniu niz ten co juz jest na stosie -> usuwamy dane ze stosu i dodajemy je do rownania do poki nie znajdziemy dzialania o #                                                                                priorytecie wyzszym, do napotkania nawiasu lub do momentu wyczerpania rzeczy ze stosu. Po tym dopiero odlozyc biezacy symbol na stos

dzialanie = '7+2*(3*4+6/3)'
stos = []
onp = ''

for w in dzialanie:
    if w =='(': # jezeli w to otwieranie nawiasu
        stos.append(w)

    elif w == ')': # jezeli w to zamykanie nawiasu
        w_stos = stos.pop() # usuwamy znaki ze stosu az znajdziemy nawias otwierajacy (znak otwierajacy tez usuwamy)
        while w_stos!='(':
            onp += w_stos
            w_stos = stos.pop()

    elif w in operator.keys(): # jezeli w to symbol dzialania 
        # w while schowane jest +=1
        while len(stos)>0 and stos[len(stos)-1]!='(' and operator[stos[-1]]>=operator[w]: # jezeli stos jest wiekszy od 0 | jezeli nie znaleziono otwarcia nawiasu | jezeli waga znaku na topie stosu jest mniejsza od
#                                                                                                                                                                                               wagi znaku dodawanego 
            onp += stos.pop()
        stos.append(w)

    else:
        onp +=w
        

while len(stos) > 0:
    onp += stos.pop()


print(onp)
    