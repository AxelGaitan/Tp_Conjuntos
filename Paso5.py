def evaluar_conjuntos(conjuntos):
    print("\n" + "="*10 + " Evaluación de condiciones lógicas " + "="*10)

    # 1. Ver si todos los conjuntos tienen los mismos elementos
    son_equivalentes = True
    for i in range(1, len(conjuntos)):
        if conjuntos[i] != conjuntos[0]:
            son_equivalentes = False
    if son_equivalentes:
        print("✔ Todos los conjuntos son equivalentes")

    # 2. Ver si todos los conjuntos tienen al menos 5 elementos
    diversidad_alta = True
    for c in conjuntos:
        if len(c) < 5:
            diversidad_alta = False
    if diversidad_alta:
        print("✔ Alta diversidad numérica (todos tienen al menos 5 elementos)")

    # 3. Ver si no comparten ningún dígito entre todos
    interseccion_total = conjuntos[0].copy()
    for c in conjuntos[1:]:
        interseccion_total &= c
    if len(interseccion_total) == 0:
        print("✔ Conjuntos totalmente independientes (sin elementos en común)")

    # 4. Ver si hay más conjuntos con cantidad impar de dígitos que pares
    cantidad_impares = 0
    cantidad_pares = 0
    for c in conjuntos:
        if len(c) % 2 == 1:
            cantidad_impares += 1
        else:
            cantidad_pares += 1
    if cantidad_impares > cantidad_pares:
        print("✔ Etiqueta: grupo impar (más conjuntos con cantidad impar de elementos)")

    # 5. Buscar si algún dígito aparece en todos los conjuntos
    union_total = set().union(*conjuntos)
    for digito in union_total:
        if all(digito in c for c in conjuntos):
            print(f"✔ El dígito {digito} está en todos los conjuntos.")
