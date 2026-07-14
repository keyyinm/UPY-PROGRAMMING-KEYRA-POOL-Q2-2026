
# INPUT
config = {}

try:
    # Intenta abrir y procesar el archivo de configuración de manera segura
    with open("config.txt", 'r') as archivo:
        for linea in archivo:
            # Quitamos espacios vacíos y omitimos líneas que no aporten datos
            linea_limpia = linea.strip()
            if not linea_limpia or "=" not in linea_limpia:
                continue
            
            clave, valor = linea_limpia.split("=")
            config[clave.strip()] = float(valor.strip())

    # PROCESS
    # Parsear y extraer de forma segura los valores enteros necesarios
    ancho = int(config["ancho"])
    alto = int(config["alto"])
    max_iter = int(config["max_iter"])
    
    real_min = config["real_min"]
    real_max = config["real_max"]
    imag_min = config["imag_min"]
    imag_max = config["imag_max"]

    # Validación preventiva de seguridad matemática para evitar división entre cero
    if ancho <= 0 or alto <= 0:
        raise ValueError("El ancho y el alto en config.txt deben ser mayores a 0.")

    # Generación y cálculo de la matriz de Mandelbrot guardando directo en CSV
    with open("clase.csv", 'w') as salida:
        salida.write("fila,columna,iteraciones\n")

        for fila in range(alto):
            for columna in range(ancho):
                # Mapeo del plano complejo
                real = real_min + (columna / ancho) * (real_max - real_min)
                imag = imag_min + (fila / alto) * (imag_max - imag_min)
                c = complex(real, imag)
                
                z = 0 + 0j
                iteraciones = 0
                
                # Bucle de escape del fractal
                while (abs(z) <= 2) and (iteraciones < max_iter):
                    z = z * z + c
                    iteraciones += 1
                
                # Escritura de resultados por pixel
                salida.write(f"{fila},{columna},{iteraciones}\n")

    # OUTPUT
    print("DONE: Proceso matemático completado exitosamente y guardado en 'clase.csv'.")

# ERROR HANDLING
except FileNotFoundError:
    print("Error Crítico: El archivo 'config.txt' es obligatorio y no fue encontrado en la ruta actual.")
except ValueError as e:
    print(f"Error de Datos: Comprueba el formato de 'config.txt'. Detalles: {e}")
except KeyError as e:
    print(f"Error de Configuración: Falta una variable requerida en config.txt: {e}")
except ZeroDivisionError:
    print("Error Matemático: Se detectó un intento de división por cero al calcular los límites.")
except Exception as e:
    print(f"Ocurrió un error inesperado al procesar el programa: {e}")
