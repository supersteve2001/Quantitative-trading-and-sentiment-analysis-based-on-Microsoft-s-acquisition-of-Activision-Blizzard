# Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard

## 1.Introduction
On January 18, 2022, Microsoft announced its intention to acquire Activision Blizzard for $68.7 billion. The deal was finalized on October 13, 2023. Under the terms of the agreement, Microsoft will bring Activision Blizzard into its Microsoft Games business as a sibling unit of Xbox Game Studios and ZeniMax Media. With the acquisition, Microsoft gained access to multiple franchises owned by Activision, Blizzard Entertainment,
and King, including Call of Duty, Crash Bandicoot, Spyro, Warcraft, StarCraft, Diablo, Overwatch, and Candy Crush. As of 2023, the acquisition is the largest video game acquisition in history by transaction value.

Following shareholder approval of the acquisition, the merger was reviewed by multiple national antitrust authorities and received early approvals from the European Commission and China’s State Administration for Market Regulation (SAMR), among others. The US Federal Trade Commission (FTC) and the UK Competition and Markets Authority (CMA) have formally questioned the acquisition. SONY also criticized the merger, fearing that Microsoft would make the lucrative Call of Duty franchise exclusive to the Xbox
platform, despite Microsoft’s pledge to remain non-exclusive until 2033. After the court found that their antitrust case did not convincingly block the merger, the FTC withdrew its request, while Microsoft offered to offload its ten-year cloud gaming support for Activision Blizzard games to Ubisoft to appease the CMA.

In this report, we will achieve visual analysis and comparison of 50 technology stocks such as Microsoft and Blizzard, analyze their performance in five years and compare their returns, and use Matplotlib to visualize the price trend chart of each company. In addition, we conduct simulated trading based on Blizzard’s price trend through the method of double moving average and LSTM, and do sentiment analysis of social comments on various acquisition news via crawler.

## 2. Methodology
### 2.1 Select Stocks and Get Stock Price Data
yfinance is a popular open-source library for accessing available financial data on Yahoo Finance using the Yahoo Public API. We can easily use Python to import yfinance package to download historical stock price information.

Microsoft and Activision Blizzard are well-known technology companies. To explore whether external factors affect stock price information, we selected 50 well-known companies in the technology industry, that have competition and cooperation relationships with them, and divided them into five sectors, software, games, cloud computing, semiconductors, and e-commerce, with ten stocks for each sector.

### 2.2  Analyze Industry Performance
Simple return is an intuitive measure that is especially useful for short-term investments or for an initial understanding of asset price fluctuations. On this basis, indexes such as cumulative return and annualize return can be derived, and the calculation formula is as follows

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/22f9c4c0-6982-4ece-927b-88e88205986b)

The bar chart is a good way to show the ranking relationship between companies, we calculate the annualized returns, come up with the best companies in each industry, and use the bar chart to visualize.

### 2.3 Trend and Correlation Analysis
We use the moving average method to process time series data to eliminate short-term volatility and thus identify long-term trends. Exponential Moving Average (EMA) is a method for calculating the average of time series data. Unlike simple moving average (SMA), EMA assigns a higher weight to the latest observation, making it more sensitive to price movements.

We also want to find the stocks that are correlated with the target stock, so we calculate the correlation coefficient between the two stock time series and select the stocks with the largest correlation coefficient. Commonly used correlation coefficients include the Pearson correlation coefficient. It applies to the case of linear dependence.

### 2.4 The Double Moving Average Crossover
The double-moving average crossover is a popular trading strategy that uses two moving averages (MAs) to buy or sell stocks. The strategy is not difficult to implement: when the faster MA crosses above the slower MA, it’s a buy signal, and when the faster MA crosses below the slower MA, it’s a sell signal.

The double-moving average crossover is a trend-following strategy, so it works best in markets that are trending. It can also work in choppy or range-bound markets, but the signals will be less reliable. The double moving average crossover is a technical indicator that is used to signal buy and sell signals for traders. The indicator is created by taking two moving averages of different lengths and then plotting them
on a chart. When the shorter moving average crosses above the longer moving average, it is considered a buy signal. Conversely, when the shorter moving average crosses below the longer moving average, it is considered a sell signal. The key to using this indicator is to use different lengths for the moving averages to avoid false
signals.

The Formula for the Double Exponential Moving Average Is:

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/9f87c619-d7af-4757-a30a-b22c13a626dd)

### 2.5 LSTM
Long short-term memory (LSTM) network is a recurrent neural network (RNN), aimed to deal with the vanishing gradient problem present in traditional RNNs.
A common LSTM unit is composed of a cell, an input gate, an output gate and a forget gate. The compact forms of the equations for the forward pass of an LSTM cell with a forget gate are:

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/630833cd-c3c5-4dd1-b6a6-2c81aae8d684)

## 3. Experiement
### 3.1 Data Collection
Select 10 well-known companies listed on the Nasdaq in the software, gaming, semiconductor, cloud computing and e-commerce industries, and their ticker symbols are as follows:

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/a3927cbd-0947-4574-93af-ab4f4ea6821e)

We use Python to download the stock price data(including date, open, close, high, low, and volume) from October 18, 2018 to October 18, 2023 through the download function in the yfinance library and stored it in a CSV file. We add every stock’s ticker symbol and industry to the file for subsequent data analysis. Format as follows:

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/ad565629-f63b-4e32-a766-36ce201a72c9)

### 3.2  Calculation of Annualized Returns and Analysis of Industries
We use Python to calculate annualized returns for each company in each industry and store them in a dictionary based on their industry. Sorted annualized returns for companies in each industry:

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/c134e213-a836-41dd-9b29-f1b92c2911b8)

The following figure shows the results of the game and semiconductor industries as an example. We can extract valuable information from the figures :
1. The best companies in each industry are NOW (cloud computing), PDD (e-commerce), SE (gaming), NVDA (semiconductor), and MDB (software).
2. The earnings of the semiconductor sector are significantly higher than other sectors.

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/5a960aed-4526-4970-a53c-00540352a433)

### 4.3 Analysis of Stock Price Trends and Correlations
First, take the closing price as the data and draw the trend chart of the stock price of each company in each industry for three years to have an intuitive impression of the data.

The following figure takes the Software industry and the Gaming industry as examples and adds two stocks ATVI and MSFT to the figure. We can find that the stock price data within the industry have the same trend, while there are obvious differences between the stock prices of the industries.

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/ee96ac23-f213-40ec-8d04-42b0b0a33cca)

We’ll display these stocks side by side, which will allow us to better analyze correlations and trends. The result are shown in the figure below

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/82bb6ca6-94bc-4d4b-9f7d-7b6ac8bcaad5)

We find that these companies show the same or opposite trends in the same period, and in fact, these companies are in competition or partnership with our target companies. In the next subsection, SONY and ATVI are used as examples for comparative analysis.

### 4.4 Trade through double moving average crossover
Using pandas, numpy, datetime, matplotlib, and other libraries, calculate price changes, average increases, and decreases. In particular, two moving averages with a short period of 7 and a long period of 3 are drawn. We simulate trading when two lines intersect.

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/cbff328e-ee52-473a-b25e-80d44ef531bf)

Let’s say the initial funding is $100,000 and you buy 1,000 ATVI shares per operation. Given that we knew in advance that Microsoft would announce the acquisition on January 18, 2022 (which caused the stock to surge), we calculated the Relative Strength Index (RSI) of all data before that date daily.

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/3e5dc7bc-3e28-4720-b6d0-10243dd18732)

The transaction results are as follows:

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/8d005257-334b-48d7-b7b1-6affe0713cac)

Here is a slice of the record for all transactions:

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/f18962d0-071e-418e-b4f8-d2dafcf2b178)

### 4.5 Trade through LSTM
Considering that machine learning is used for quantitative analysis and is one of the mainstream directions of quantitative research at present, we take the LSTM model as an example for stock price prediction and simulated trading. We let the model make predictions based on the last 3 days of data and repeat the experiment 10 times to find the best prediction. The predictions are as follows:

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/5d74f86f-a6e9-4590-880c-714c2075b8a8)

The average accuracy of the predicted results under this model reached 97.2623, which seems to be a very good result, but to judge the quality of the quantitative trading model, it is necessary to compare the return rate in the end. The trading process uses an evolutionary strategy agent, and only 1 unit can be bought or sold per transaction. Its simulated trading process is as follows:

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/b3fcc3b7-255e-4cb4-af6f-5e3166cd81e5)

### 4.6 Social platform comment crawling and its emotion analysis
Based on the stock price rise and fall of Blizzard Company (ATVI) from January 2022 to October 2023, five time points with the largest rise and fall were selected: 220118, 230207, 230324, 230426, 230711.

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/c9f2d3ee-a04e-473c-9d53-ea520b95cd9a)

Interestingly, each of these five dates saw an event that had a significant impact on the acquisition process.

On January 18, 2022, Microsoft suddenly announced that it would acquire Activision Blizzard for $68.7 billion, the largest one in the history of video games. Intuitively, this is good for the acquisition process.

On February 8, 2023, the UK’s Competition and Markets Authority, the CMA, published its preliminary findings into the Microsoft and Activision deal, finding that it ”could result in UK gamers facing higher prices, less choice or less innovation.” This is not good for the acquisition process.

On March 24, 2023, the UK Competition and Markets Authority (CMA) announced that it was no longer concerned about Call of Duty. It came to this conclusion after revising its financial model. This is good for the acquisition process.

On April 26, 2023, the UK Competition and Markets Authority (CMA) officially rejected Microsoft’s acquisition of Activision Blizzard. This is not good for the acquisition process.

On July 11, 2023, Judge Corley denied the FTC’s request for a preliminary injunction and shortened the duration of the temporary restraining order. This is good for the acquisition process. The announcement of the acquisition on January 18, 2022, and the approval of the acquisition in the United States on July 11, 2023, obviously had the most talking points, with far more negative and positive comments than other news.

According to the above dates, news about Microsoft’s acquisition of Blizzard is the hottest under these five dates. Vader sentiment analysis was carried out for each news article, and the number of positive comments and negative comments were counted.

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/f11e109a-92cf-4d7e-ad23-7f4135a41091)

By generating the comment heat map with worldly characteristics, we can intuitively judge that the number of positive comments was very high in the events of February, 22 and July, 23. In contrast, there were fewer comments on the various emotions of other events.

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/8476ad28-cdb0-44ad-953d-d50a54162051)

Collect statistics on the most popular words in social comments, and generate a unique wordcloud map for each report through wordcloud

![image](https://github.com/supersteve2001/Quantitative-trading-and-sentiment-analysis-based-on-Microsoft-s-acquisition-of-Activision-Blizzard/assets/69947525/08d9a6c3-80e9-4caa-be29-6dde737d153a)

## 5. Conclusion
The implementation process of the trading strategy under the double moving average is easier to realize than the machine learning trading strategy taking LSTM as an example, but has better profit results.

This is because machine learning often sacrifices model representation to implement calculations. An existing machine learning model is also difficult to predict and trade correctly for a stock market that is heavily influenced by real events.

At the same time, the reason for our excellent return on trading under the double-moving average method is that we have optimized the model according to the stock situation and prior information. Under the normal inversion method, the return rate is only 50%, which is equal to 111% of the return rate under the long-term holding of stocks and 45% of the current method.

However, it is not surprising that machine learning is not applicable in quantitative trading, we can improve the model, replace the double-moving average with a moving average and a forecast stock trend after machine learning training, and replace the short-period moving average with the forecast data, so as to make the shortperiod indicator more consistent with the real situation and eliminate the lag of the moving average method.





