try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is not installed. Run: pip install Pillow")
    exit()

#INPUT
    
config = {}

try:
    archivo = open("config.txt", 'r')
except FileNotFoundError:
    print("Error: 'config.txt' not found. Make sure it is in the same folder.")
    exit()

try:
    for linea in archivo:
        clave, valor = linea.strip().split("=")
        config[clave] = float(valor) if "." in valor else int(valor)
except ValueError:
    print("Error: 'config.txt' has an invalid line (expected format key=value).")
    archivo.close()
    exit()
finally:
    archivo.close()

try:
    with open("clase.csv", 'r') as data:
        datos = data.readlines()  #
except FileNotFoundError:
    print("Error: 'clase.csv' not found. Run the math classwork first to generate it.")
    exit()
    
try:
    alto, ancho, max_iter = config["alto"], config["ancho"], config["max_iter"]
except KeyError as e:
    print(f"Error: missing key {e} in 'config.txt'.")
    exit()

try:
    img = Image.new("HSV", (ancho, alto))
except Exception as e:
    print(f"Error creating the image: {e}")
    exit()

if not datos:
    print("Error: 'clase.csv' is empty.")
    exit()

encabezados = datos.pop(0)

#PROCESS
try:
    for dato in datos:
        fila, columna, iteraciones = map(int, dato.strip().split(","))
        brillo = 0 if (iteraciones == max_iter) else int((iteraciones / max_iter) * 255)
        img.putpixel((columna, fila), (brillo, 255, 255))

except ValueError:
    print("Error: 'clase.csv' contains a malformed row.")
    exit()

except ZeroDivisionError:
    print("Error: 'max_iter' cannot be zero.")
    exit()

except IndexError:
    print("Error: a pixel coordinate is outside the image size.")
    exit()

except Exception as e:
    print(f"Unexpected error while rendering the image: {e}")
    exit()

#PROCESS
try:
    img_rgb = img.convert('RGB')
except Exception as e:
    print(f"Error converting the image: {e}")
    exit()

#OUTPUT
try:
    img_rgb.save("mandelbrot-clase.png")
except OSError:
    print("Error: could not save 'mandelbrot-clase.png'.")
    exit()

print("DONE")
