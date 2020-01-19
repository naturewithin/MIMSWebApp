#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is taken from the Dash installation guide for testing purposes:
# https://dash.plot.ly/getting-started


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': 'rgb(26, 118, 255)',
    'text': '#2aa198'
}
app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
                          html.H1(children='MIMS Data', style={
                              'textAlign': 'center', 'color': colors['text']}),

                          html.Div(
                              children='This is a development server. Do not '
                                       'use it in production deployment. '
                                       'Development server credits:'
                                       'https://dash.plot.ly/getting-started',
                              style={
                                  'textAlign': 'center',
                                  'color': '#7FDBFF'
                              }),
                          dcc.Graph(
                              figure=go.Figure(
                                  data=[
                                      go.Scatter(
                                          x=[1995, 1996, 1997, 1998, 1999, 2000,
                                             2001, 2002, 2003,
                                             2004, 2005, 2006, 2007, 2008, 2009,
                                             2010, 2011, 2012],
                                          y=[219, 146, 112, 127, 124, 180, 236,
                                             207, 236, 263,
                                             350, 430, 474, 526, 488, 537, 500,
                                             439],
                                          name='Oxygen',
                                          marker=go.scatter.Marker(
                                              color='rgb(55, 83, 109)'
                                          )
                                      ),
                                      go.Scatter(
                                          x=[1995, 1996, 1997, 1998, 1999, 2000,
                                             2001, 2002, 2003,
                                             2004, 2005, 2006, 2007, 2008, 2009,
                                             2010, 2011, 2012],
                                          y=[16, 13, 10, 11, 28, 37, 43, 55, 56,
                                             88, 105, 156, 270,
                                             299, 340, 403, 549, 499],
                                          name='Argon',
                                          marker=go.scatter.Marker(
                                              color='rgb(26, 118, 255)'
                                          )
                                      )
                                  ],
                                  layout=go.Layout(
                                      showlegend=True,
                                      legend=go.layout.Legend(
                                          x=0,
                                          y=1.0
                                      ),
                                      margin=go.layout.Margin(l=40, r=0, t=40,
                                                              b=30),
                                      plot_bgcolor=colors['background'],
                                      paper_bgcolor=colors['background'],
                                      font={
                                          'color': colors['text']
                                      }
                                  )
                              ),

                          ),
                          dcc.Graph(
                              figure=go.Figure(
                                  data=[
                                      go.Scatter(
                                          x=[1995, 1996, 1997, 1998, 1999, 2000,
                                             2001, 2002, 2003,
                                             2004, 2005, 2006, 2007, 2008, 2009,
                                             2010, 2011, 2012],
                                          y=[219, 146, 112, 127, 124, 180, 236,
                                             207, 236, 263,
                                             350, 430, 474, 526, 488, 537, 500,
                                             439],
                                          name='Oxygen',
                                          marker=go.scatter.Marker(
                                              color='rgb(55, 83, 109)'
                                          )
                                      ),
                                      go.Scatter(
                                          x=[1995, 1996, 1997, 1998, 1999, 2000,
                                             2001, 2002, 2003,
                                             2004, 2005, 2006, 2007, 2008, 2009,
                                             2010, 2011, 2012],
                                          y=[16, 13, 10, 11, 28, 37, 43, 55, 56,
                                             88, 105, 156, 270,
                                             299, 340, 403, 549, 499],
                                          name='Argon',
                                          marker=go.scatter.Marker(
                                              color='rgb(26, 118, 255)'
                                          )
                                      )
                                  ],
                                  layout=go.Layout(
                                      showlegend=True,
                                      legend=go.layout.Legend(
                                          x=0,
                                          y=1.0
                                      ),
                                      margin=go.layout.Margin(l=40, r=0, t=40,
                                                              b=30),
                                      plot_bgcolor=colors['background'],
                                      paper_bgcolor=colors['background'],
                                      font={
                                          'color': colors['text']
                                      }
                                  )
                              ),
                          )
                      ])

if __name__ == '__main__':
    app.run_server(debug=True)
