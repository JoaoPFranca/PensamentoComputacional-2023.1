# Faça um programa que transforme uma temperatura fornecida em Celsius para a correspondente em Fahrenheit.

# A formula de conversão de Celsius para Fahrenheit é a seguinte: C=(5/9)*(F– 32).

                                                                         
# Digite a Temperatura em Celsius: 30
# A conversão de 30° para Fahrenheit é: 86° F

celsius = float(input("Digite a Temperatura em Celsius: ")) #Coloquei float pq tem que ser um número e pode ter casas decimais

fahrenheit = (celsius * 9/5) + 32 #conversão para fahrenheit quando isolado o F

print(f"A conversão de {celsius}° para Fahrenheit é: {fahrenheit}°F")