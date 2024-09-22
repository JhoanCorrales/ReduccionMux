def calcular_min_terminos(entrada):
    try:
        min_terminos = list(map(int, entrada.split(',')))
        min_terminos.sort()
        maximo_termino = max(min_terminos)
        num_variables = maximo_termino.bit_length()

        if num_variables > 1:
            mux_info, resultado = reduccion(min_terminos, num_variables)
            return f"Número de variables: {num_variables}\n{mux_info}\n\t {resultado}"
        else:
            return "Error: No se puede reducir un mux 2x1"
    except ValueError:
        return "Error: Ingrese números válidos separados por comas"


def reduccion(min_terminos, variables):
    selectoras = variables - 1
    num_entradas = 2 ** selectoras

    variable_negada = list(range(num_entradas))
    variable_no_negada = list(range(num_entradas, 2 * num_entradas))

    resultado = []
    for negada, no_negada in zip(variable_negada, variable_no_negada):
        if negada in min_terminos and no_negada in min_terminos:
            resultado.append("1")
        elif negada in min_terminos:
            resultado.append("~A")
        elif no_negada in min_terminos:
            resultado.append("A")
        else:
            resultado.append("0")

    mux_info = f"Mux {2**selectoras}x1\n\u0100:\t {variable_negada}\nA:\t {variable_no_negada}"
    return mux_info, resultado


if __name__ == "__main__":
    calcular_min_terminos()