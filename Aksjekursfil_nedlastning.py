#for å laste ned aksjekurs filer:
#info fra denne nettsiden: https://pypi.org/project/yfinance/
#pip install yfinance
#det gir tilgang til yahoo finance
#dataen vi får har kolonner som ser slik ut: Date,Open,High,Low,Close,Adj Close,Volume
#jeg velger en av kolonnene å printe

import yfinance as yf

data = ["AAPL", "TSLA", "MSFT", "NVDA", "SNAP"] #noen eksempler på aksjer

for d in data:

    download = yf.download(d, start="2023-01-01", end="2024-01-01")

    with open(f"{d}.txt", "w") as f:
        for pris in download["Close"].values:  #Close er values gjør at det bare blir tallene som printes
            f.write(f"{pris}\n")
