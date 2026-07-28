# Analiza sprzedaży sieci Superstore (2015–2018)

Projekt analityczny w Pythonie (pandas, matplotlib) na podstawie publicznego
zbioru danych **Sample Superstore** - ok. 10 000 zamówień amerykańskiej sieci
sklepów sprzedającej meble, artykuły biurowe i elektronikę.

## Cel projektu

Odpowiedzieć na pytania biznesowe:
- Które kategorie produktów generują największą sprzedaż, a które największy zysk?
- Czy są kategorie, które **tracą** pieniądze mimo wysokiej sprzedaży?
- Jak sprzedaż rozkłada się na regiony USA i segmenty klientów?
- Jak zmieniała się sprzedaż rok do roku i miesiąc do miesiąca?

## Kluczowe wnioski

- **Furniture (meble)** generuje prawie tyle samo sprzedaży co Technology, ale
  ma marżę zaledwie **2,49%** wobec ~17% w pozostałych kategoriach.
- Podkategoria **Tables** przynosi realną stratę: **-17 725 USD** łącznego zysku
  mimo wysokiej sprzedaży - prawdopodobnie efekt zbyt wysokich rabatów.
- Region **West** generuje najwyższą sprzedaż i zysk, **South** - najniższą sprzedaż.
- Sprzedaż rosła konsekwentnie każdego roku: z 484 tys. USD (2015) do 733 tys. USD (2018).

## Struktura projektu

```
superstore-sales-analysis/
├── data/
│   └── superstore.csv          # surowe dane źródłowe
├── src/
│   └── analiza_sprzedazy.py    # główny skrypt analityczny
├── output/                     # wygenerowane wykresy i pliki CSV z wynikami
├── requirements.txt
└── README.md
```

## Jak uruchomić

```bash
git clone https://github.com/dkirsz/superstore-analiza-sprzedazy.git
cd superstore-sales-analysis
pip install -r requirements.txt
python src/analiza_sprzedazy.py
```

Wyniki (wykresy PNG i podsumowania CSV) pojawią się w folderze `output/`.

## Użyte technologie

- **pandas** - wczytywanie, czyszczenie i agregacja danych
- **matplotlib** - wizualizacja wyników
- **Python 3.10+**

## Źródło danych

Publiczny zbiór danych "Sample Superstore", powszechnie używany do nauki
analizy danych 

## Możliwe rozszerzenia

- Prognoza sprzedaży na kolejny kwartał (np. regresja liniowa / Prophet)
- Analiza wpływu rabatów (`Discount`) na rentowność
- Interaktywny dashboard (Streamlit / Plotly Dash)
