import yfinance as yf
import finplot as fplt

tickers = {
    "AAPL": yf.Ticker('AAPL'),
    #"MSFT": yf.Ticker('MSFT'),
    #"SPY": yf.Ticker('SPY')
}

def get_articles(news_data):
    # Print news attributes in a structured format
    for article in news_data:  
        print(article)
        print("\n")  
        print("Title: " + article['title'])
        print("Related Tickers: " + ', '.join(article['relatedTickers']))    
        print("Publisher: " + article['publisher'])
        try:
            print("Description: " + article['summary'])
        except:
            print("Description: None")

for ticker in tickers.values():
    get_articles(ticker.news)
    #df = ticker.history(interval='1d',period='1y')
    #fplt.candlestick_ochl(df[['Open','Close','High','Low']])
    #fplt.show()