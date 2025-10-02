#for å laste ned aksjekurs filer:
#info fra denne nettsiden: https://pypi.org/project/yfinance/
#pip install yfinance
#det gir tilgang til yahoo finance
#dataen vi får har kolonner som ser slik ut: Date,Open,High,Low,Close,Adj Close,Volume
#jeg velger en av kolonnene å printe

import yfinance as yf

#henter data for Apple
data = yf.download("AAPL", start="2023-01-01", end="2024-01-01")

with open("apple_sin_aksjekurs.txt", "w") as f:
    for pris in data["Close"]: #dataen fra yahoo finance har masse kolonner (for prisen da den var lav, høy osv. per dag), vi kan velge den kolonnen vi vil ha
        f.write(str(pris) + "\n")
