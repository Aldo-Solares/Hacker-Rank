
#LINK https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
#NOTE Esta parte del código va en la parte predeterminada del ejercicio.

def merge_the_tools(string, k):
    
    division = int(len(string)/k)
    i=0
    j=k
    for x in range(division):
        texto = string[i:j]
        nuevo_texto = ""
        for d in texto:
            if d in texto and d not in nuevo_texto:
                nuevo_texto += d
        print(nuevo_texto)
        i +=k
        j +=k


#NOTE_2 Mi ejemplo para comprobar el programa.
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


texto = "AAAAABBCC"
lista = list(texto)
texto_pasado = ""
for x in range(len(lista)):
    if lista[x] in(texto) and lista[x] not in texto_pasado:
        texto_pasado += lista[x]

print(texto_pasado)