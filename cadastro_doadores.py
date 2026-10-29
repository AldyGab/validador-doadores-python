idadmin= 16
pesomin=50
resposta = 'S'
doadores=[]

print('Cadastro de doadores')

while resposta=='S':
    try: 
        nome=str(input('Nome: '))
        idade=int(input('Idade: '))
        altura=float(input('Altura: '))
        peso=float(input('Peso: '))
    except ValueError:
        print('Erro: Por favor, digite valores numéricos válidos para idade, altura e peso.')
        continue

    if peso < pesomin and idade < idadmin:
        print('Esta pessoa não possui peso e idade ideal para realizar a doação!')
        continue
    elif peso < pesomin:
        print('Esta pessoa não possui o peso minimo para realizar a doação de sangue!')
        continue
    elif idade < idadmin:
        print(' Esta pessoa não possui idade o suficiente para realizar a doação de sangue')
        continue
    else:
        doadores.append(nome)
        doadores.append(idade)
        doadores.append(altura)
        doadores.append(peso)
    
    resposta=str(input('Deseja realizar mais um cadastro?S/N: ')).upper()

print('Salvando dados no arquivo TXT...')

with open('informacoes_salvas.txt','a', encoding='utf-8') as arquivo:
    for i in range(0, len(doadores), 4):
        nome = doadores[i]
        idade = doadores[i+1]
        altura = doadores[i+2]
        peso = doadores[i+3]
        arquivo.write(f"Nome: {nome} | Idade: {idade} anos | Altura: {altura}m | Peso: {peso}kg\n")

print("Programa encerrado. Arquivo TXT atualizado!")