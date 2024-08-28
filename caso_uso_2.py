import numpy as np

rng = np.random.default_rng()


nwalks = 5000
nsteps = 1000

draws = rng.integers(0, 2, size=(nwalks, nsteps))

steps = np.where(draws > 0, 1, -1)

#eixo y, faz a soma acumulativa por linha
walks = steps.cumsum(axis=1)

print(walks.max())
print(walks.min())

#pegando quem fez 30 p ou -30 passos
#any com axis1, vai verificar se algum elemento na linha é true
hits30 = (np.abs(walks) >= 30).any(axis=1)

#pegando o tempo de atravesia dos 30 passos
#np.abs(walks[hits30]): Primeiro, walks[hits30] seleciona apenas as "caminhadas" para as quais hits30 é True, isto é, apenas as "caminhadas" que atingem uma distância absoluta de 30 ou mais. Então np.abs() é aplicado a esta seleção, tornando todos os valores positivos
#argmax(axis=1) retorna os índices dos valores máximos ao longo do eixo 1 (ou seja, ao longo de cada linha). No caso de uma matriz booleana, True é considerado maior que False, portanto .argmax(axis=1) retorna o índice do primeiro True ao longo de cada linha
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(axis=1)

print(crossing_times.sum())
print(crossing_times.mean())

#calculo desvio padrao, quando menor, mais perto da media, maior mais espalho esta os dados
draws = 0.25 * rng.standard_normal((nwalks, nsteps))


test = np.array([[1, 2, 3],
                [5, 6, 7]])
print(test)
#indexando por boolean
print(test[:, [True, False, True]])