#not es un operador lógico que generalmente se usa para averiguar la negación o el valor booleano opuesto.
#En el ejercicio los numeros sean factores 
x=5
y=3
#La condicion sera una expresion cuando da un resultado falso o verdadero 
# muestra si es verdadera una de las dos 
while not (x%y==0 or y%x==0): 
    #Con while podemos ejecutar un conjunto de declaraciones siempre que una condición sea verdadera.  
    print('Rutina para saber si dos numeros son factores')
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))   
    #print imprime el mensaje especificado 
print('Son factor')
