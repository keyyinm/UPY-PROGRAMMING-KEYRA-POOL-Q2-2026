config = {}

#INPUT
try:
    archivo = open("config.txt", 'r')
except FileNotFoundError:
    print("Error: 'config.txt' not found. Make sure it is in the same folder.")
    exit()

#PROCESS
try:
    for linea in archivo:
        clave, valor = linea.strip().split("=")
        config[clave] = float(valor)
except ValueError:
    print("Error: 'config.txt' has an invalid line (expected format key=value).")
    archivo.close()
    exit()
finally:
    archivo.close()

#PROCESS
try:
    ancho, alto, max_iter = int(config["ancho"]), int(config["alto"]), int(config["max_iter"])
except KeyError as e:
    print(f"Error: missing key {e} in 'config.txt'.")
    exit()

#OUTPUT
try:
    salida = open("clase.csv", 'w')
except OSError:
    print("Error: could not create 'clase.csv'.")
    exit()

salida.write("fila, clumna, iteraciones\n")

# PROCESS
try:
    for fila in range(alto):
        for columna in range(ancho):
            real = config["real_min"] + (columna / ancho) * (config["real_max"] - config["real_min"])
            imag = config["imag_min"] + (fila / alto) * (config["imag_max"] - config["imag_min"])
            c = complex(real, imag)

            z = 0 + 0j
            iteraciones = 0

            while (abs(z) <= 2) and (iteraciones < max_iter):
                z = z * z + c
                iteraciones += 1

            #OUTPUT
            salida.write(f"{fila},{columna},{iteraciones}\n")

except KeyError as e:
    print(f"Error: missing key {e} in 'config.txt'.")

except ZeroDivisionError:
    print("Error: 'ancho' or 'alto' cannot be zero.")

except Exception as e:
    print(f"Unexpected error while computing the Mandelbrot set: {e}")

finally:
    salida.close()

print("DONE")
