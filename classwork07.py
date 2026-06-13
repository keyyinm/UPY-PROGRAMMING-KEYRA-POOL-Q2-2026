rol=int(input("Enter your rol: "))
switched = 0
i = 2
while rol > 0:
    digit =  rol % 10
    switched = switched * 10 + digit
    rol = rol // 10
print("Numero Invertido: ", switched)
i=2
total=0
for digit in str(switched):
    digit = int(digit)
    mul_seq = digit * i
    total += mul_seq
    print(digit, "*", i, "=", mul_seq)
    i += 1
    if i > 7:
        i = 2

print("Total =", total)
modulo = total%11
digit2= 11-modulo
while switched > 0:
    digit = switched % 10
    rol=rol*10+digit
    switched = switched // 10
dig_ver = rol -digit2
print(f"Digito verificador {dig_ver}")