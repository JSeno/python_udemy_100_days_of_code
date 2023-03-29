from mes01.semana01.dia01.band_name_generator import band_name_generator

def main():
    city = input('Qual o nome da cidade que você nasceu?: ')
    pet_name = input('Qual o nome do seu animal de estimação?: ')
    result = band_name_generator(city, pet_name)
    print(result)

main()
