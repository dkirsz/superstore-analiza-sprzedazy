import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "superstore.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

pd.set_option("display.width", 120)
df = pd.read_csv(DATA_PATH, encoding="latin1")

print("=== Wymiary danych ===")
print(df.shape)
print("\n=== Pierwsze wiersze ===")
print(df.head())

df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

braki_przed = df.isna().sum().sum()

df["Postal Code"] = df["Postal Code"].fillna(0).astype(int)
df["Czas_realizacji_dni"] = (df["Ship Date"] - df["Order Date"]).dt.days

df["Marza_%"] = (df["Profit"] / df["Sales"] * 100).round(2)

print(f"\nBraków danych przed czyszczeniem: {braki_przed}")
print(f"Braków danych po czyszczeniu: {df.isna().sum().sum()}")


wg_kategorii = (
    df.groupby("Category")
    .agg(Sprzedaz=("Sales", "sum"), Zysk=("Profit", "sum"), Zamowienia=("Order ID", "nunique"))
    .sort_values("Sprzedaz", ascending=False)
)
wg_kategorii["Marza_%"] = (wg_kategorii["Zysk"] / wg_kategorii["Sprzedaz"] * 100).round(2)

wg_regionu = (
    df.groupby("Region")
    .agg(Sprzedaz=("Sales", "sum"), Zysk=("Profit", "sum"))
    .sort_values("Sprzedaz", ascending=False)
)

wg_segmentu = (
    df.groupby("Segment")
    .agg(Sprzedaz=("Sales", "sum"), Zysk=("Profit", "sum"), Zamowienia=("Order ID", "nunique"))
    .sort_values("Sprzedaz", ascending=False)
)

df["Rok"] = df["Order Date"].dt.year
sprzedaz_roczna = df.groupby("Rok")["Sales"].sum()

df["Miesiac"] = df["Order Date"].dt.to_period("M")
sprzedaz_miesieczna = df.groupby("Miesiac")["Sales"].sum()

top10_produktow = (
    df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
)

straty_subkategorie = (
    df.groupby("Sub-Category")["Profit"].sum().sort_values().head(5)
)

print("\n=== Sprzedaż i zysk wg kategorii ===")
print(wg_kategorii)
print("\n=== Sprzedaż wg regionu ===")
print(wg_regionu)
print("\n=== Sprzedaż wg segmentu klienta ===")
print(wg_segmentu)
print("\n=== Sprzedaż roczna ===")
print(sprzedaz_roczna)
print("\n=== 5 najmniej rentownych podkategorii ===")
print(straty_subkategorie)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

wg_kategorii["Sprzedaz"].plot(kind="bar", ax=axes[0, 0], color="steelblue")
axes[0, 0].set_title("Sprzedaż wg kategorii produktów")
axes[0, 0].set_ylabel("Sprzedaż (USD)")
axes[0, 0].tick_params(axis="x", rotation=0)

sprzedaz_miesieczna.plot(kind="line", ax=axes[0, 1], color="darkorange")
axes[0, 1].set_title("Sprzedaż miesięczna (2015-2018)")
axes[0, 1].set_ylabel("Sprzedaż (USD)")

wg_regionu["Sprzedaz"].plot(kind="bar", ax=axes[1, 0], color="seagreen")
axes[1, 0].set_title("Sprzedaż wg regionu USA")
axes[1, 0].set_ylabel("Sprzedaż (USD)")
axes[1, 0].tick_params(axis="x", rotation=0)

straty_subkategorie.plot(kind="barh", ax=axes[1, 1], color="crimson")
axes[1, 1].set_title("Najmniej rentowne podkategorie (suma zysku)")
axes[1, 1].set_xlabel("Zysk (USD)")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "wykresy_sprzedazy.png", dpi=120)
print(f"\nZapisano wykresy do: {OUTPUT_DIR / 'wykresy_sprzedazy.png'}")

wg_kategorii.to_csv(OUTPUT_DIR / "podsumowanie_kategorie.csv")
wg_regionu.to_csv(OUTPUT_DIR / "podsumowanie_region.csv")
wg_segmentu.to_csv(OUTPUT_DIR / "podsumowanie_segment.csv")
top10_produktow.to_csv(OUTPUT_DIR / "top10_produktow.csv")
df.to_csv(OUTPUT_DIR / "dane_przetworzone.csv", index=False)

print("Zapisano pliki wynikowe w folderze output/.")
