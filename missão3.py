# Recuperando o Sistema de Notas
# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

nota = int(input('Podera me informar qual foi a sua pontuação? '))
if nota >= 90:
    print("Parabéns, tirou A!")
elif nota >= 80:
    print("Muito Bem, você tirou B")
elif nota >= 70:
    print("Bom trabalho, você tirou C")
elif nota >= 60:
    print("Fique atento,Você tirou D.")
else:
    print("Estude um pouco mais , Você tirou F")
