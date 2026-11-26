import pandas as pd
import matplotlib.pyplot as plt

df_mag = pd.read_csv("magazyny.csv", encoding="utf-8-sig")
df_kli = pd.read_csv("klienci.csv", encoding="utf-8-sig")

df_mag = df_mag[["wojewodztwo", "produkty"]]
df_kli = df_kli[["wojewodztwo", "zamowienia"]]

prod_woj = df_mag.groupby("wojewodztwo", as_index=False)["produkty"].sum()
zam_woj = df_kli.groupby("wojewodztwo", as_index=False)["zamowienia"].sum()

zestawienie = pd.merge(prod_woj, zam_woj, on="wojewodztwo", how="outer").fillna(0)
zestawienie["produkty"] = zestawienie["produkty"].astype(int)
zestawienie["zamowienia"] = zestawienie["zamowienia"].astype(int)

zestawienie["roznica"] = zestawienie["produkty"] - zestawienie["zamowienia"]

zestawienie = zestawienie.sort_values(by="roznica", ascending=True)
print(zestawienie.to_string(index=False))

x = range(len(zestawienie))
szerokosc = 0.4

plt.figure(figsize=(10, 5))
plt.bar([i - szerokosc / 2 for i in x], zestawienie["produkty"], width=szerokosc, label="Produkty")
plt.bar([i + szerokosc / 2 for i in x], zestawienie["zamowienia"], width=szerokosc, label="Zamówienia")

plt.xticks(x, zestawienie["wojewodztwo"], rotation=30, ha="right")
plt.title("Produkty i zamówienia w województwach")
plt.xlabel("Województwo")
plt.ylabel("Liczba sztuk")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.barh(zestawienie["wojewodztwo"], zestawienie["roznica"], color="teal")
plt.axvline(0, color="black", linewidth=0.8)
plt.title("Różnica (produkty - zamówienia) w województwach")
plt.xlabel("Różnica")
plt.ylabel("Województwo")
plt.tight_layout()
plt.show()
