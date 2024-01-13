lista_zadan = []

def dodawanie():
    dodawana = str(input('Jakie zadanie chcesz dodac do listy zadan?: '))
    lista_zadan.append(dodawana)

def usuwanie():
    print(lista_zadan)
    usun = input('Ktore zadanie chcialbys usunac? Podaj pelna nazwe: ')
    
    for i in lista_zadan:
        if usun.lower() == lista_zadan[i].lower():
            lista_zadan.pop(usun)
            break

def wykonanie():
    print(lista_zadan)
    wykon = input('Status ktorego zadania chcialbys zmienic na wykonane? Podaj pelna nazwe: ')
    for i in lista_zadan:
        if lista_zadan[i].lower() == wykon.lower() == lista_zadan[i].lower():
            lista_zadan[i] = 'wykonane'
            break

def wyswietl():
    print('\n', lista_zadan)

while True:
    wybor = int(input('1. Dodawanie zadania \n2. Usuniecie zdania\n3. Oznaczenie zadania jako wykonane\n4. Wyswietl cala liste zadan\n5. Zakoncz program\n'))
    
    
    if wybor == 1:
        dodawanie()
    elif wybor == 2:
        usuwanie()
    elif wybor == 3:
        wykonanie()
    elif wybor == 4:
        wyswietl()
    elif wybor == 5:
        break
    else:
        continue
        
    
    
    
    #dodawanie zadannia na if
    #usuwanie zadan na if
    #oznaczanie zadan za wykonane
    #wyswietlanie wszystkich zadan
    #zakonczenie programu