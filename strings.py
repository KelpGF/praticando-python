from datetime import datetime

print(repr('O strip remove caracteres especiais de fim de linha \n\t'.strip()))
print('Count conta a quantidade de ocorrências em uma string'.count(' '))
print('O split quebrar a string de acordo com o caractere escolhido'.split(' '))
print('  '.join(['O', 'join', 'junta', 'separando', 'por', 'caractere']))
print(f'O f"conteúdo" serve para utilizar variáveis na string: {423*92398/523}\n e também para formatar valores: {2.3213:1.2f}, {datetime.now():%d/%m}')