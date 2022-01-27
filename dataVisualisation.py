import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
reader=pd.read_csv("data.csv")
groupby_data=reader.groupby("level")["attempt"].mean()
print(groupby_data)
fig=go.Figure(go.Bar(x=groupby_data, y=["level1","level2","level3","level4"],orientation='h'))
fig.show()