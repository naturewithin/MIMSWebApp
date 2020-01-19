import Data as d
import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
import chart_studio

chart_studio.tools.set_credentials_file(username='retirotigre', api_key='1CRlTIJ3MQwnaossRixV')

data_var = d.Data()

trace1 = go.Scatter(
    x=data_var.get_julian_date(),
    y=data_var.get_isoprene_53(),
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
        text=data_var.Isoprene_53,
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
        title=
        go.layout.yaxis.Title(
            text='Isoprene 53',
            font=dict(
                family='Open Sans, sans-serif',
                size=18,
                color='#000000'
            )
        )
    )
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='Isoprene_53')
