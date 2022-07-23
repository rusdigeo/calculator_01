""""
RUSDIANTO, S.PD.
"""""

# INTRODUCTION
print("Halo, saya kalkulator pribadi Anda")
print("Saya akan membantu Anda untuk menghitung angka")
print("Tolong beri saya dua nomor dan operator matematika")
print("Mari kita lihat apakah kalkulator saya benar")

#INPUT
a = int(input("Angka pertama (A): "))
b = int(input("Angka kedua (B): "))
opr = input("Operator: ")

#OUTPUT
if opr == "+":
    print(str(a) + "+" +str(b) + "=" + str(a + b))
elif opr == "-":
    print(str(a) + "-" +str(b) + "=" + str(a - b))
elif opr == "x" or opr == "*":
    print(str(a) + "x" +str(b) + "=" + str(a * b))
elif opr == ":" or opr == "/":
    print(str(a) + ":" +str(b) + "=" + str(a / b))
elif opr == "modulus" or opr == "%":
    print(str(a) + "%" +str(b) + "=" + str(a % b))
elif opr == "pangkat" or opr == "^":
    print(str(a) + "^" +str(b) + "=" + str(a ^ b))
else :
    print("operator hanya +,-,x:,% (modulus),^ (pangkat)")

#INPUT
a = int(input("Angka pertama (A): "))
b = int(input("Angka kedua (B): "))
opr = input("Operator: ")

#OUTPUT
if opr == "+":
    print(str(a) + "+" +str(b) + "=" + str(a + b))
elif opr == "-":
    print(str(a) + "-" +str(b) + "=" + str(a - b))
elif opr == "x" or opr == "*":
    print(str(a) + "x" +str(b) + "=" + str(a * b))
elif opr == ":" or opr == "/":
    print(str(a) + ":" +str(b) + "=" + str(a / b))
elif opr == "modulus" or opr == "%":
    print(str(a) + "%" +str(b) + "=" + str(a % b))
elif opr == "pangkat" or opr == "^":
    print(str(a) + "^" +str(b) + "=" + str(a ^ b))
else :
    print("operator hanya +,-,x:,% (modulus),^ (pangkat)")