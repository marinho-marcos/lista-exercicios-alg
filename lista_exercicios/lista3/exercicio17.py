# def mediaDuasNotas(qntdAlunos):
#     for i in range(1,qntdAlunos+1):
#         nota1 = float(input(f"Informe a primeira nota do aluno {i}: "))
#         print(nota1)
#         nota2 = float(input(f"Informe a segunda nota do aluno {i}: "))
#         print(nota2)
    
#         if nota1 <= 100 and nota2 <= 100:
#             media = (nota1+nota2)/2
#             print(f"A média das notas do aluno {i} é: {media}\n")

# turma1 = int(input("Informe quantos alunos possui a turma 1: "))
# mediaDuasNotas(turma1)

for i in range(1,11):
        nota1 = float(input(f"Informe a primeira nota do aluno {i}: "))
        print(nota1)
        nota2 = float(input(f"Informe a segunda nota do aluno {i}: "))
        print(nota2)
    
        if nota1 <= 100 and nota2 <= 100:
            media = (nota1+nota2)/2
            print(f"A média das notas do aluno {i} é: {media}\n")
        else:
            print("voce inseriu uma nota inválida")