import Data as d
import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
import chart_studio
import plotly.io as pio
from outliers import smirnov_grubbs as grubbs

chart_studio.tools.set_credentials_file(username='retirotigre', api_key='1CRlTIJ3MQwnaossRixV')

data_var = d.Data()

trace1 = go.Scatter(
    x=data_var.get_julian_date(),
    y=grubbs.test(data_var.get_DMS_62(), alpha=0.99),
    xaxis='x1',
    yaxis='y1',
    marker=go.scatter.Marker(
        color='rgb(26, 118, 255)'
    )
)

data = [trace1]

layout = go.Layout(
    plot_bgcolor='#cbd0d6',
    paper_bgcolor='#cbd0d6',
    title=go.layout.Title(
        text=data_var.DMS_62,
        xref='paper',
        font=dict(
            family='Open Sans, sans-serif',
            size=22,
            color='#000000'
        )
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text='Julian Date',
            font=dict(
                family='Open Sans, sans-serif',
                size=18,
                color='#000000'
            )
        )
    ),
    yaxis=go.layout.YAxis(
        showexponent='all',
        exponentformat='e',
        title=go.layout.yaxis.Title(
            text='DMS 62',
            font=dict(
                family='Open Sans, sans-serif',
                size=18,
                color='#000000'
            )
        )
    )
)
fig = go.Figure(data=data, layout=layout)
pio.write_html(fig, file='DMS-62.html', auto_open=True)