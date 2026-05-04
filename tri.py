lado_1 = float(input("Medida em cm - primeiro lado  "))
lado_2 = float(input("Medida em cm - segundo lado  "))
lado_3 = float(input("Medida em cm - terceiro lado  "))

if lado_1 == lado_2 == lado_3 :
     print ("triângulo equilátero")

elif lado_1 >= lado_2 == lado_3 :
     print("triângulo isósseles")

elif lado_2 >= lado_1 == lado_3 :
     print("triÂngulo isósseles")

elif lado_1 >= lado_3 == lado_2 :
     print("triângulo isósseles")

else :
     print("triângulo escaleno")