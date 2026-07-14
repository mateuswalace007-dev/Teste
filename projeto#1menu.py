participantes=[]
while (True):
	print("========================")
	print("     MENU DO MT")
	print("========================")
	print("digite 1 para cadastrar")
	print("digite 2 para listar")
	print("digite 3 para atualizar")
	print("digite 4 para remover")
	print("digite 0 para sair")
	escolha=int(input("qual sua escolha ? "))
	print("========================")
	if (escolha == 1):
		n1=input("qual nome voce quer castrar ? ").strip().capitalize()
		participantes.append(n1)
	
	elif (escolha == 2):
		
		if (len(participantes)> 0):
		     for i, nome in enumerate (participantes):
		     	print(f"participante {i} : {nome}")
		     	
		else:
		 	print("você nao adicionou nenhum nome na lista digite 1")
		 	 
	
	elif (escolha == 3):
		idx=int(input("qual o numero participante que deseja atualizar o nome ? "))
		nv_nome=input("qual nome deseja colocar no lugar ? ").strip().capitalize()
		participantes[idx]=nv_nome
		
	
	elif (escolha == 4):
		n2=input("qual nome voce quer remover ? ").strip().capitalize()
		participantes.remove(n2)
	
	elif(escolha==0):
		print("voce escolheu parar o programa ")
		break
