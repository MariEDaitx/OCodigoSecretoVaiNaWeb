# O Sistema Eleitoral Secreto 
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).
votar = input("Qual é a sua Idade ? ")

if votar > 18:
    print("Você está apto a votar!")
else: 
    print("Você não está apto a votar!")