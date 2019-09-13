
'''
Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''

from copy import deepcopy

# Sua classe algoritmo de ordenação precisar ter um método ordenar
class InsertionSort(object):
    def ordenar(self, colecao, inicio, fim):
        cont = inicio + 1
        while(cont < fim):
            aux = colecao[cont]['weight'] #cont pega os pesos
            contAux = cont - 1
            flag = False
            while(contAux >= 0 and int(colecao[contAux]['weight']) > int(aux)):
                colecao[contAux + 1]['weight'] = colecao[contAux]['weight']
                contAux -= 1
                flag = True
            if(flag == True):
                colecao[contAux + 1]['weight'] = aux
            cont += 1
        return colecao

class MergeSort(object):
    def ordenar(self, colecao, inicio, fim):
        if(inicio < fim):
            meio = (fim + inicio) // 2
            self.ordenar(colecao, inicio, meio)
            self.ordenar(colecao, meio + 1, fim)
            self.Intercalar(colecao, inicio, meio, fim)
        return colecao
    def Intercalar(self, colecao, inicio, meio, fim):
        colCopia = deepcopy(colecao)
        left = inicio
        right = meio + 1
        contCop = inicio # contador da copia: conta de inicio ate fim
        while(contCop <= fim):
            if(left > meio):
                colecao[contCop]['weight'] = colCopia[right]['weight']
                right += 1
            elif(right > fim):
                colecao[contCop]['weight'] = colCopia[left]['weight']
                left += 1
            elif(int(colCopia[left]['weight']) < int(colCopia[right]['weight'])):
                colecao[contCop]['weight'] = colCopia[left]['weight']
                left += 1
            else:
                colecao[contCop]['weight'] = colCopia[right]['weight']
                right += 1
            contCop += 1

class QuickSort(object):
    def ordenar(self, colecao, inicio, fim):
        if(inicio < fim):
            pos = self.particionar(colecao, inicio, fim)
            self.ordenar(colecao, inicio, pos - 1)
            self.ordenar(colecao, pos + 1, fim)
        return colecao
    def particionar(self, colecao, inicio, fim):
        pivoEsq = colecao[inicio]['weight']
        destPivo = inicio
        andarColecao = inicio + 1

        while(andarColecao < fim):
            if(int(colecao[andarColecao]['weight']) < int(pivoEsq)):
                destPivo += 1
                self.trocar(colecao, destPivo, andarColecao)
            andarColecao += 1
        self.trocar(colecao, inicio, destPivo)
        return destPivo
    def trocar(self, colecao, inicio, fim):
        temp = colecao[inicio]['weight']
        colecao[inicio]['weight'] = colecao[fim]['weight']
        colecao[fim]['weight'] = temp















