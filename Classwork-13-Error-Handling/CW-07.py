class DigitoVerificadorError(Exception):
    pass

try:
    rol = input("Ingrese el rol: ")

    if rol.count("-") != 1:
        raise ValueError("Rol inválido: No tiene el formato XXXXXXXXX-X")

    rol_sin_digito, digito = rol.split("-")

except ValueError as e:
    print(e)

else:
    try:
        invertido = rol_sin_digito[::-1]

        if not invertido.isnumeric():
            raise ValueError("Los digitos del rol deben ser numéricos")

        if not digito.isnumeric():
            raise ValueError("El digito verificador debe ser numérico")

    except ValueError as e:
        print(e)

    else:
        secuencia = [2, 3, 4, 5, 6, 7]
        suma = 0

        for index in range(len(invertido)):
            multiplicando = secuencia[index % 6]
            numero = int(invertido[index:index + 1])
            suma += numero * multiplicando

        total = suma % 11

        verificador = 11 - total

        if verificador == 11:
            verificador = 1
        elif verificador == 10:
            verificador = 0

        try:
            if verificador != int(digito):
                raise DigitoVerificadorError(
                    f"Error: El dígito verificador no conicide, se esperaba {verificador}"
                )

        except DigitoVerificadorError as e:
            print(e)

        else:
            print(f"{rol_sin_digito}-{verificador}")

