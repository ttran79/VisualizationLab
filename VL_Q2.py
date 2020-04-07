import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')
# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)



# Sorting values and select 20 first value
new_df = df.sort_values('Total', ascending = False ).head(20).reset_index()

# Preparing data
trace1 = go.Bar(x=new_df['NOC'], y=new_df['Total'], name='total',
                marker={'color': '#CD7F32'})

data = [trace1]
# Preparing layout
layout = go.Layout(title='Q2 total medals of olympic 2016 of first top 20', xaxis_title="Country",
                   yaxis_title="total medals", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='VL_Q2.html')
