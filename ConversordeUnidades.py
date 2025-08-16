def menu():
    print("=== Conversor de Unidades ===")
    print("1. Converter Celsius para Fahrenheit")
    print("2. Converter Fahrenheit para Celsius")
    print("3. Converter Quilômetros para Milhas")
    print("4. Converter Milhas para Quilômetros")
    print("5. Sair")


def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def km_para_milhas(km):
    return km * 0.621371


def milhas_para_km(milhas):
    return milhas / 0.621371


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção (1/2/3/4/5): ")

        if opcao == '1':
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F\n")
        elif opcao == '2':
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit}°F equivalem a {celsius:.2f}°C\n")
        elif opcao == '3':
            km = float(input("Digite a distância em Quilômetros: "))
            milhas = km_para_milhas(km)
            print(f"{km} km equivalem a {milhas:.2f} milhas\n")
        elif opcao == '4':
            milhas = float(input("Digite a distância em Milhas: "))
            km = milhas_para_km(milhas)
            print(f"{milhas} milhas equivalem a {km:.2f} km\n")
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()