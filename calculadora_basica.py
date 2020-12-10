def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return  numero1 * numero2

def division(numero1, numero2):
    return numero1 / numero2

numero1 = int(input('Ingresa tu primer número: '))
simbolos = {
    '+': suma,
    '-': resta,
    '*': multiplicacion,
    '/': division,
}
for simbolo in simbolos:
    print(simbolo)

operacion = input('Ingresa una de las operaciones que aparecen arriba: ')
while operacion not in simbolos:
    operacion = input('Operación inválida, intenta nuevamente: ')

numero2 = int(input('Ingresa tu segundo número: '))
resultado = simbolos[operacion](numero1, numero2)
print(f'\n{numero1} {operacion} {numero2} = {resultado}')
