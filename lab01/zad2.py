import pandas as pd
import matplotlib.pyplot as plt

miasta_csv = "D:\coding\inteligencja-obliczeniowa\lab01\miasta.csv"
miasta = pd.read_csv(miasta_csv, sep=",")

# Wyświetlenie ramki danych
# print(miasta.values)

# Dodanie wiersza z danymi z 2010 roku 
miasta.loc[len(miasta)] = [2010, 460, 555, 405]
# print(miasta)

# Stwórz wykres dla ludności Gdańska (skorzystaj z paczki matplotlib). Dodaj odpowiednie oznaczenia osi, tytuły. Wykres ma być liniowy z punktami i w kolorze czerwonym.

# Wykres dla ludności Gdańska
plt.plot(miasta['Rok'], miasta['Gdansk'], 'ro-')
plt.xlabel('Rok')
plt.ylabel('Ludność')
plt.title('Ludność Gdańska')
# plt.show()

# Stwórz dodatkowo wykres, który będzie zestawiał zmiany ludności wszystkich miasta na jednym wykresie w różnych kolorach. Dodaj legendę.

# Wykres dla ludności wszystkich miast
plt.plot(miasta['Rok'], miasta['Gdansk'], 'ro-', label='Gdańsk')
plt.plot(miasta['Rok'], miasta['Poznan'], 'bo-', label='Poznań')
plt.plot(miasta['Rok'], miasta['Szczecin'], 'go-', label='Szczecin')
plt.xlabel('Rok')
plt.ylabel('Ludność')
plt.title('Ludność wszystkich miast')
plt.legend()
# plt.show()

# Przeskaluj wszystkie danewzorem 𝑧𝑖=𝑥𝑖−𝑚𝑒𝑎𝑛(𝑥)σ(x)(standaryzacja). Podaj odpowiedź na pytanie: jaką średnią i odchylenie standardowe mają dane po skalowaniu?

# Przeskalowanie danych
miasta['Gdansk'] = (miasta['Gdansk'] - miasta['Gdansk'].mean()) / miasta['Gdansk'].std()
miasta['Poznan'] = (miasta['Poznan'] - miasta['Poznan'].mean()) / miasta['Poznan'].std()
miasta['Szczecin'] = (miasta['Szczecin'] - miasta['Szczecin'].mean()) / miasta['Szczecin'].std()

# Wyświetlenie ramki danych po przeskalowaniu
# print(miasta)

# Średnia i odchylenie standardowe po przeskalowaniu
# print(miasta['Gdansk'].mean())
# print(miasta['Gdansk'].std())
# print(miasta['Poznan'].mean())
# print(miasta['Poznan'].std())
# print(miasta['Szczecin'].mean())
# print(miasta['Szczecin'].std())

# Przeskaluj wszystkie dane wzorem 𝑧𝑖=𝑥𝑖−𝑚𝑖𝑛(𝑥)𝑚𝑎𝑥(𝑥)−𝑚𝑖𝑛(𝑥)(normalizacja). Podaj odpowiedź na pytanie: jakąwartość minimalną i maksymalną mają dane po skalowaniu?

# Przeskalowanie danych
miasta['Gdansk'] = (miasta['Gdansk'] - miasta['Gdansk'].min()) / (miasta['Gdansk'].max() - miasta['Gdansk'].min())
miasta['Poznan'] = (miasta['Poznan'] - miasta['Poznan'].min()) / (miasta['Poznan'].max() - miasta['Poznan'].min())
miasta['Szczecin'] = (miasta['Szczecin'] - miasta['Szczecin'].min()) / (miasta['Szczecin'].max() - miasta['Szczecin'].min())

# Wyświetlenie ramki danych po przeskalowaniu
print(miasta)

# Wartość minimalna i maksymalna po przeskalowaniu
print(miasta['Gdansk'].min())
print(miasta['Gdansk'].max())
print(miasta['Poznan'].min())
print(miasta['Poznan'].max())
print(miasta['Szczecin'].min())
print(miasta['Szczecin'].max())
