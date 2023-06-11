# no retorna y no recibe
def sumar_f1():
    num_1 = int(input("Ingrese un numero: "))
    num_2 = int(input("Ingrese otro numero: "))
    rta = num_1 + num_2
    print("La suma es " + str(rta))

# no retorna pero recibe
def sumar_f2(num_1, num_2):
    rta = num_1 + num_2
    print("La suma es " + str(rta))

# retorna pero no recibe
def sumar_f3():
    num_1 = int(input("Ingrese un numero: "))
    num_2 = int(input("Ingrese otro numero: "))
    rta = num_1 + num_2
    return rta

# retorna y recibe
def sumar_f4(num_1, num_2):
    rta = num_1 + num_2
    return rta

def sumar(a: int, b: int)-> int:
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """

    rta = a + b
    return rta

def restar(a, b):
    """
    resta dos numeros enteros\n
    a = minuendo de la operacion\n
    b = sustraendo de la operacion\n
    devuelve la resta de los enteros ingresados
    """
    return a - b
