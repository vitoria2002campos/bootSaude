dorDeCabecaAlop = ['paracetamol', 'Dipirona', 'ibufreno']
dorEstomacalAlop = ['omeprazol', 'esomeprazol', 'aluminio de magnésio']
dorDeDenteAlop = ['Ácido acetilsalicilico']
dorMuscularAlop = ['Advil', 'Flanax', 'Voltaren Celebra']
dorDeOuvidoAlop = ['cataflam, amoxicilina', 'azitromicina', 'feneflan']

dorDeCabecaNat = ['Chá de camomila', 'Chá de taneceto', 'Chá de gengibre']
dorEstomacalNat = ['Suco de batata crua', 'Chá de dente de leão', 'Chá de boldo', 'Chá de hortelã com pimenta']
dorDeDenteNat = ['Água morna com sal', 'Hortelã, cravo da india, Alho']
dorMuscularNat = ['gelo', 'Compressa de sal quente', 'arnica']
dorDeOuvidoNat = ['inalação de vapor camomila, óleo de alho']

listaAlopatico = []
listaNatural = []


print('LISTA REMÉDIOS ALOPATICOS')
listaAlopatico.extend(dorDeCabecaAlop + dorEstomacalAlop + dorDeDenteAlop + dorMuscularAlop + dorDeOuvidoAlop)
print(listaAlopatico)

print('LISTA REMÉDIOS NATURAIS')
listaNatural.extend(dorDeCabecaNat + dorEstomacalNat + dorDeDenteNat + dorMuscularNat + dorDeOuvidoNat)
print(listaNatural)

nivelDor = ""

nivelDor =  int(input('Antes de prosseguirmos, de 0 a 10, qual o seu nivel de dor?'))

if nivelDor > 7:
    print('Voce precisa consultar um médico!')
else:
    print("Qual sua preferencia para remédios? Digite 'N' para NATURAIS e 'L' para  ALOPÁTICOS" )



"""print tipoDor =int(input('Informe o tipo de dor que voce está sentindo'))"""