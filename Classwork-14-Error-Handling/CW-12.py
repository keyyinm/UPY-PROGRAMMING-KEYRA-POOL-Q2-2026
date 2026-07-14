from PIL import Image

# INPUT
config = {}

try:
    # 1. Leer y parsear el archivo de configuración de forma segura
    with open("config.txt", 'r') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            if not linea_limpia or "=" not in linea_limpia:
                continue
            clave, valor = linea_limpia.split("=")
            # Conversión dinámica según el tipo de dato numérico
            config[clave.strip()] = float(valor.strip()) if "." in valor else int(valor.strip())

    alto = int(config["alto"])
    ancho = int(config["ancho"])
    max_iter = int(config["max_iter"])

    # 2. Leer los datos de iteraciones desde el archivo CSV generado previamente
    with open("clase.csv", 'r') as data:
        datos = data.readlines()

    if len(datos) <= 1:
        raise ValueError("El archivo 'clase.csv' está vacío o solo contiene encabezados.")

    # PROCESS
    # Inicialización del lienzo usando el modo HSV para un mejor manejo del color
    img = Image.new("HSV", (ancho, alto))
    
    # Remover los encabezados de forma segura
    encabezados = datos.pop(0)

    # Procesamiento por píxel leyendo fila por fila del CSV
    for num_linea, dato in enumerate(datos, start=2):
        linea_limpia = dato.strip()
        if not linea_limpia:
            continue  # Ignorar líneas en blanco accidentales en el CSV
        
        try:
            fila, columna, iteraciones = map(int, linea_limpia.split(","))
            
            # Cálculo del brillo proporcional al escape del fractal
            brillo = 40 if (iteraciones == max_iter) else int((iteraciones / max_iter) * 255)
            
            # Asignar color al píxel (columna corresponde a X, fila corresponde a Y)
            img.putpixel((columna, fila), (brillo, 255, 255))
            
        except ValueError:
            print(f"Advertencia: Línea {num_linea} corrupta u omitida en clase.csv: '{linea_limpia}'")
            continue

    # Conversión final y almacenamiento de la imagen resultante
    img_rgb = img.convert('RGB')
    img_rgb.save("mandelbrot-clase.png")

    # OUTPUT
    print("DONE: Visualización generada con éxito. Archivo guardado como 'mandelbrot-clase.png'.")

# ERROR HANDLING
except FileNotFoundError as e:
    print(f"Error Crítico: Archivo requerido no encontrado. Detalles: {e}")
except KeyError as e:
    print(f"Error de Configuración: Falta una variable esencial en config.txt: {e}")
except ValueError as e:
    print(f"Error de Datos: Conflicto en el parseo o estructura de archivos. Detalles: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado durante la renderización: {e}")

