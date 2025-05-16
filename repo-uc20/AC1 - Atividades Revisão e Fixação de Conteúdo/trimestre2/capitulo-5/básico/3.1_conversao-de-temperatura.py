'''
3.1 Conversão de temperatura
Crie uma função celsius_para_fahrenheit(c) que retorne a temperatura convertida.
'''
temperatura_celsius = float(input("Temperatura em °C: "))

def celsius_para_fahrenheit(temperatura_celsius):
    return (temperatura_celsius * 9/5) + 32

print("Temperatura em °F:", celsius_para_fahrenheit(temperatura_celsius))
