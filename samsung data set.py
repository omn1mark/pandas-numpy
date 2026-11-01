import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Samsung Dataset.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

print(df.head())
print(df.describe())

print("Highest:", df["High"].max())
print("Lowest:", df["Low"].min())
print("Average:", np.mean(df["Close"]))
print("Median:", np.median(df["Close"]))
print("Standard deviation:", np.std(df["Close"]))

top10 = df.sort_values("Close", ascending=False)
print(top10[["Date", "Close"]].head(10))

df["Profit"] = df["Close"] - df["Open"]

print("Profit days:", len(df[df["Profit"] > 0]))
print("Loss days:", len(df[df["Profit"] < 0]))

df["Daily Change"] = df["Close"].pct_change() * 100

print("Biggest increase:", df["Daily Change"].max())
print("Biggest decrease:", df["Daily Change"].min())

df["Price Range"] = df["High"] - df["Low"]

print(df.sort_values("Price Range", ascending=False).head(5))

df["Year"] = df["Date"].dt.year
yearly = df.groupby("Year")["Close"].mean()

df["Weekday"] = df["Date"].dt.day_name()
weekdays = df.groupby("Weekday")["Daily Change"].mean()

df["Signal"] = np.where(df["Daily Change"] > 2, "Big Increase", "Normal")

print(df["Signal"].value_counts())

df["MA30"] = df["Close"].rolling(30).mean()

investment = 1000000
shares = investment / df["Adj Close"].iloc[0]
final_money = shares * df["Adj Close"].iloc[-1]

print("Investment:", investment)
print("Final value:", round(final_money, 2))
print("Profit:", round(final_money - investment, 2))

plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Close"], label="Price")
plt.plot(df["Date"], df["MA30"], label="30 Day Average")
plt.title("Samsung Stock Price")
plt.legend()
plt.show()

yearly.plot(kind="bar", figsize=(12, 5))
plt.title("Average Price by Year")
plt.show()

weekdays.plot(kind="bar", figsize=(10, 5))
plt.title("Average Return by Weekday")
plt.show()

plt.hist(df["Daily Change"].dropna(), bins=50)
plt.title("Daily Returns Distribution")
plt.show()