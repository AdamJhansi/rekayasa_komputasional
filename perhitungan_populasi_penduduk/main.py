import numpy as np
import matplotlib.pyplot as plt
import requests

#BIKIN SAMA KAYA YG PERKIRAAN CUACA

# URL endpoint API (PENTING)
country = input("Masukan Kode Negara : ")

def get_population(country):
    url = f"https://api.worldbank.org/v2/countries/{country}/indicators/SP.POP.TOTL?format=json"
    response = requests.get(url)
    data = response.json()
    return data

# if response.status_code == 200:
#     print(data)
# else:
#     print("Gagal mengambil data:", response.status_code)

def exponential_growth(country):
    if get_population.decimal == 0 :
        countryiso3code = country
        country_data = 



def exponential_growth(population, growth_rate, years):
    time = np.arange(0, years + 1)
    population_values = population * np.exp(growth_rate * time)
    return population_values

def main():
    # Parameter model
    initial_population = 1000  # populasi awal
    growth_rate = 0.03  # Tingkat pertumbuhan (3% per tahun)
    simulation_years = 50  # Jumlah tahun untuk simulasi

    # Melakukan perhitungan pertumbuhan populasi
    population_values = exponential_growth(initial_population, growth_rate, simulation_years)

    # Visualisasi hasil
    plt.plot(np.arange(simulation_years + 1), population_values, marker='o', linestyle='-')
    plt.title('Pertumbuhan Populasi')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Populasi')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
