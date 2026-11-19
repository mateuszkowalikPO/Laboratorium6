import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("klienci.csv", encoding="utf-8-sig")
df = df[["klient", "miasto", "wojewodztwo", "zamowienia"]]
print(df.head())
posortowane = df.sort_values("zamowienia", ascending=False)
suma_zamowien = df["zamowienia"].sum()
print("\n")
print(posortowane[["klient", "miasto", "zamowienia"]].head())
print(f"Laczna ilosc zamowionych sztuk: {suma_zamowien}")
posortowane["udzial_procent"] = (df["zamowienia"] / df["zamowienia"].sum()) * 100
print(posortowane.head())

top10 = posortowane.head(10)

plt.bar(top10["klient"] ,top10["zamowienia"])
plt.xlabel("Klienci")
plt.ylabel("Ilosc zamowien")
plt.title("Top 10 klientow z nawieksza liczba zamowien")
plt.tight_layout()
plt.show()

suma_top10 = top10["zamowienia"].sum()
suma_pozostalych = suma_zamowien - suma_top10

plt.pie([suma_top10, suma_pozostalych], labels=["Top 10 klientow", "Suma pozostalych"], autopct="%.2f%%", startangle=90)
plt.title("Udzial top 10 klientow w calkowitej liczbie zamowionych sztuk")

plt.show()