continueLoop = True

while continueLoop:
  print("\nEscolha uma opção: \n1-Ver familiares\n2-Adicionar familiar\n3-Sair");

  try:
    opc = int(input())

    if (opc == 3):
      continueLoop = False
    else:
      print('\n')
      with open('family-data.txt', 'a+') as file:
        if (opc == 1):
          file.seek(0)
          print('Seus familiares:')
          for line in file:
            data = line.split(',')
            print(f'Nome: {data[0]}\nParentesco: {data[1]}\nIdade: {data[2]}\n')
        elif (opc == 2):
          print("Informe os dados")
          print("Nome:")
          name = input()
          print("Parentesco:")
          parentesco = input()
          print("Idade:")
          age = input()

          file.write(f'\n{name},{parentesco},{age}')
        else:
          print('Opção inválida!')
  except ValueError:
    print("Informe um número válido")
  except:
    print("Ops! Tente novamente")

print('Valeu')
