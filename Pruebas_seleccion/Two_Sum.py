transacciones  = [100, 250, 50, 120]
Valor_objetivo = 350

def encontrar_pares(transacciones, Valor_objetivo):
    Diccionario_variables = {}
    for i, valor in enumerate(transacciones):
        diferencia = Valor_objetivo - valor
        if diferencia in Diccionario_variables:
            return (Diccionario_variables[diferencia], i)
        Diccionario_variables[valor] = i
        
resultado = encontrar_pares(transacciones, Valor_objetivo)
print(f"Los índices de las transacciones que suman {Valor_objetivo} son: {resultado}")        