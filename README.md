# NPRG045

- Pokračování s rss kanály yahoo, nutné získat related tickers
## APIs
- [https://www.linkedin.com/pulse/10-alternatives-newsapi-newsdata-bing-news-yahoo-more-vikash/]
- MBOUM
- yfinance (non official Yahoo!)
    - Nemezený počet dotazů
    - `news()`
    - Proč nepoužívat yfinance pro analýzu sentimentu [https://analyzingalpha.com/yfinance-python]
    - Is there an alternative to Yahoo Finance? Being an unofficial library, it is not uncommon for yfinance to suddenly stop working. Thus, having another free alternative is essential.
    
    - Although less popular, YahooQuery is another open-source Python library that fetches data from Yahoo Finance. You can install it simply by typing “pip install yahooquery” on your terminal. The library is also actively maintained and decently documented (Github / Documentation).
    - ```
        {'uuid': '50b7811e-82a0-31ff-8916-781fa5678d5a', 
         'title': 'Earnings, Fed Decision, Jobs Data Are Key This Week. One Thing’s More Important.', 
         'publisher': 'Barrons.com', 
         'link': 'https://finance.yahoo.com/m/50b7811e-82a0-31ff-8916-781fa5678d5a/earnings%2C-fed-decision%2C-jobs.html', 
         'providerPublishTime': 1698662160, 
         'type': 'STORY', 
         'thumbnail': {'resolutions': [{'url': 'https://s.yimg.com/uu/api/res/1.2/iXgzsWpiRgKbrTNXnh6jqw--~B/aD02NDA7dz0xMjc5O2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/Barrons.com/fa92d09e55c95de75a80bed7faaa9e0b', 'width': 1279, 'height': 640, 'tag': 'original'}, {'url': 'https://s.yimg.com/uu/api/res/1.2/VmOvcAxXCZLy6y92AMv56Q--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/Barrons.com/fa92d09e55c95de75a80bed7faaa9e0b', 'width': 140, 'height': 140, 'tag': '140x140'}]}, 
         'relatedTickers': ['AAPL', 'AMD', '^GSPC', 'STLAM.MI', 'F']}
        ```
- Finnhub

## Proč není API  tomto případě ideální?
API funguje na principu dotazování, to znamená že bychom se museli neustále dotazovat. Websockety by byly lepším řešení, pokud se bavíme o vytvoření API, jenž by bylo možné poskytovat vnějším systémům pro obchodování. Pokud by se jednalo pouze o vizuální webovou aplikaci pro uživatele postačilo by nám API, které by se dotázalo pokaždé po otevření stránky s detailem daného symbolu.

## RSS, WebSub, Atom

## Implementační návrhy
- Zachytávání ceny v čase zveřejnění článku. Pro analýzu/vizualizaci možného dopadu. Dobré také jako mini featura v detailu.

## News filter 
- Filtrování na základě klíčových slov (https://scanz.com/smart-ways-to-create-keyword-based-news-scans/)

### Poznámky
Jakmile se kvantita stane hlavním důrazem, kvalita nevyhnutelně trpí. 