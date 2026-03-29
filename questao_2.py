# Analise a função abaixo e responda: ela funciona corretamente? 
# Se sim, o que ela retorna para as chamadas indicadas? 
# Se houver algum problema, aponte e sugira uma correção. 

def somar(a, b=10): 
    return a + b 
print(somar(5)) 
print(somar(5,3))
print(somar(b=2,a=4))

# RESPOSTA:
# A nomenclatura def é para definir o nome da função que deseja utilizar posteriormente.
# Neste caso, é definido para fazer a soma dois números
# Com isso, é para retornar a soma de a+b
# Por fim, é printado a função com os números passados dentro dela.
# Na primeira impressão, retorna o valor de 15, pois o "a" ainda não foi atribuido nenhum valor e o "b" foi atribuído o valor de 10.
# Na segunda impressão, retorna o valor de 8, pois o "a" ainda não foi atribuído nenhum valor e o "b" é atribuído outro valor já que é um parâmetro que está sobrescrevendo o outro valor.
# Na terceira impressão, retorna o valor de 6, pois a ordem dos parâmetro nomeados não impede a função de ser carregada normalmente em Python.