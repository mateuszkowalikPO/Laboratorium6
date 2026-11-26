import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("magazyny.csv", encoding="utf-8-sig")

df = df[["magazyn", "miasto", "wojewodztwo", "produkty"]]

wojewodztwo = input("Podaj wojewodztwo: ")
produkty = int(input("Minimalna liczba produktow: "))

wynik = df[(df["wojewodztwo"] == wojewodztwo) & (df["produkty"] >= produkty)]
sorted = wynik.sort_values("produkty", ascending=False)

print(sorted[["magazyn", "miasto", "produkty"]])

liczba_magazynow = len(sorted)
suma_produktow = sorted["produkty"].sum()
print(f"\nLiczba magazynow: {liczba_magazynow}")
print(f"Suma produktow: {suma_produktow}")

top5 = sorted.head(5).iloc[::-1]  # odwrócenie kolejności, by największy był na górze wykresu
etykiety = top5["magazyn"] + " (" + top5["miasto"] + ")"

plt.figure(figsize=(8, 4))
plt.barh(etykiety, top5["produkty"], color="steelblue")
plt.title(f"Top magazyny - woj. {wojewodztwo} (min. {produkty} szt.)")
plt.xlabel("Liczba produktow")
plt.ylabel("Magazyn")
plt.tight_layout()
plt.show()
