from math import pi
import pandas as pd
from pandas_datareader import data, wb
import datetime
from bokeh.plotting import figure, show, output_file

symbol = 'AAPL'

web = data
start = datetime.datetime(2016, 8, 5)
end = datetime.datetime(2017, 8, 4)

df = web.DataReader(symbol, 'google', start, end)
df

df.columns
df.index

inc = df.Close > df.Open
dec = df.Open > df.Close
w = 12*60*60*1000 #half day in milliseconds

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title="AAPL Candlestick")
p.xaxis.major_label_orientation = pi / 4
p.grid.grid_line_alpha=0.3

p.segment(df.index, df.High, df.index, df.Low, color="black")
p.vbar(df.index[inc], w, df.Open[inc], df.Close[inc], color="#32CD32", line_color="green")
p.vbar(df.index[dec], w, df.Open[dec], df.Close[dec], color="#FF4500", line_color="red")

output_file("candlestick_AAPL.html", title="candlestick_AAPL.py example")

show(p) # open a browser

