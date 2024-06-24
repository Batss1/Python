equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
  equipamentos.append(str(input("Equipamento: ")))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamentos.append((str(input('Departamento: '))))
  resposta = input("Digite 'S' para continuar: ").upper()
    

for indice in range(0,len(equipamentos)):
  print("\nEquipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])


busca = input(" Digite o número de serial do equipamento danificado: ")
for indice in range(0,len(departamentos)):
  if seriais[indice] == busca:
   del equipamentos[indice] 
   del valores[indice]
   del seriais[indice] 
   del departamentos[indice]
   break
 
for indice in range(0,len(equipamentos)):
  print("\nEquipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])

print("Seu equipamento foi deletado do sistema!")