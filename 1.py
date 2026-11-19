import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("magazyny.csv", encoding="utf-8-sig")
print(f"Kolumny: {df.columns.tolist()}")
df = df[["magazyn", "miasto", "wojewodztwo", "produkty"]]
print(df.head())
print(f"Liczba magazynow: {(len(df["magazyn"]))}")
posortowane = df.sort_values("produkty", ascending=False)
print(posortowane[["magazyn", "miasto", "produkty"]].head())
print(f"Laczna ilosc produktow: {df["produkty"].sum()}")

top10 = posortowane.head(10)

plt.barh(top10["magazyn"] ,top10["produkty"])
plt.xlabel("Liczba produktów")
plt.ylabel("Identyfikator magazynu")
plt.title("Top 10 magazynów z największą liczbą produktów")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
