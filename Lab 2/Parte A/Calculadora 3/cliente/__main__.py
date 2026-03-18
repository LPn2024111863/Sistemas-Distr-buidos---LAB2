from cliente.interacao import interacao
from servidor.gestor import maquina

def main():
	"""
	Esta função cria dois objetos: m, que é uma instância de Maquina, e i, uma
	instância de Interacao.

	A Interacao fornecerá os dados obtidos por input do utilizador à Maquina e esta
	efetuará a operação necessária, caso esta seja válida.

	"""
	m:object = maquina.Maquina()
	i:object = interacao.Interacao(m)
	i.execute()

if __name__ == '__main__':
	main()
