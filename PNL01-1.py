#Processamento de Linguagem Natural sem StopWords
#Grafico com ID das palavras, Zipf, Frequência.

#Importation of libraries:
import numpy as np
import matplotlib.pyplot as plt



from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from operator import itemgetter


#Extair o texto de um arquivo
arq = open('arquivo.txt', 'r')
texto = arq.readlines()
palavras = texto[0] #Passando de lista para uma variável
#Deixar o texto em letras miúdas e dividir por palavras:
palavras = word_tokenize(palavras.lower())

#Filtrar as palavras tirando pontuações e stopwords:
filtro = set(stopwords.words('portuguese')+['\'','\"','\\','/','?','!', '@','#','$','%','&','*','(',')','-','_','+','{','}','[',']','{','}','ª','º','´','`','~','^','<','>',';',':','.',',','...','´´','``','\'\'','”'])
semStopwords = [palavra for palavra in palavras if palavra not in filtro]

#Tirando repetições de palavras
contagem=[]#Frequência das palavras
p_filtradas=[]#palavras sem stopwords ou repetições

#Tira a repetições de palavras e conta a frequencia
for i in range(len(semStopwords)):
    palavra=semStopwords[i]
    if palavra not in p_filtradas:#Verifica se a palavra já existe me p_filtradas
        contagem.append(1)
        p_filtradas.append(palavra)
    else:
        contagem[p_filtradas.index(palavra)]=contagem[p_filtradas.index(palavra)]+1

#Listas de Output:
matriz = []
zipf = []
index = []

##Adiciona as palavras e as frequências da mesmas a uma matriz
for i in range(len(contagem)):
  matriz.append([p_filtradas[i], contagem[i], ''])


#Ordena de forma decrescente por frequência a matriz
matriz = sorted(matriz[0:], key = itemgetter(1), reverse=True)

#Acrescentando a Terceira Lei de Zipf a matriz
for i in range(len(contagem)):
    matriz[i][2]= (i+1)* matriz[i][1]

#Incorporando os valores às variàveis de Output.
for i in range(len(contagem)):
    zipf.append(matriz[i][2])
    contagem[i]=matriz[i][1]
    index.append((i+1))

#Criar txt
arquivo = open(input('\n\nDigite o nome do arquivo:')+'.txt','a')
arquivo.write("Resultados do teste\n")


#Colunas no text
arquivo.write('ID da palavra | Frequência | Terceira Lei de Zipf | Palavra\n')
print('ID da palavra| Palavra')
for i in range(len(contagem)):
    print(i+1,'\t\t', matriz[i][0])
    #convertendo resultado para string e escrevendo string no texto
    arquivo.write(str(i+1)+'\t\t\t'+str(matriz[i][1])+'\t'+str(matriz[i][2])+'\t\t\t'+matriz[i][0])
    arquivo.write('\n')

#Fechando arquivo txt
arquivo.close()    

plt.title('Processamento de Linguagem Natural sem StopWords')
plt.bar(index, contagem, width=0.4, color ='red', label ="frequência")
plt.bar(index, zipf, width=0.2, color = 'blue', label = "zipf")
plt.axis([0, 35, -0.5, 230])
plt.legend(loc='upper left')
plt.xlabel('ID da palavra')
plt.grid(True)
plt.show()
