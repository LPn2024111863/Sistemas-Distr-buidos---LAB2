from cliente.interacao import interacao

def main():
	"""
	Esta função cria dois objetos: m, que é uma instância de Maquina, e i, uma
	instância de Interacao.

	A Interacao fornecerá os dados obtidos por input do utilizador à Maquina e esta
	efetuará a operação necessária, caso esta seja válida.

	"""
	i:object = interacao.Interacao()
	i.execute()

if __name__ == '__main__':
	main()
