import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Chargement des données
dataset_file = r'C:\Users\y_mc\PycharmProjects\YokAi\Dataset\historical_automobile_sales.csv'
data = pd.read_csv(dataset_file)




app = dash.Dash(__name__)
app.title = "Automobile Statistics Dashboard"

app.layout = html.Div([
    html.H1("Automobile Statistics Dashboard"),
    dcc.Dropdown(
        id='dropdown-statistics',
        options=[
            {'label': 'Yearly Statistics', 'value': 'Yearly'},
            {'label': 'Recession Period Statistics', 'value': 'Recession'}
        ],
        value='Yearly'  # Valeur par défaut
    ),
    dcc.Dropdown(
        id='select-year',
        options=[{'label': i, 'value': i} for i in range(1980, 2024)],
        value=2020  # Valeur par défaut
    ),
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex'})
])

@app.callback(
    Output('output-container', 'children'),
    [Input('dropdown-statistics', 'value'), Input('select-year', 'value')]
)
def update_output_container(selected_stat, selected_year):
    if selected_stat == 'Recession Period Statistics':
        recession_data = data[data['Recession'] == 1]


        mo_1 = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.bar(mo_1, x='Year', y='Automobile_Sales', title="Fluctuation moyenne des ventes d'automobiles pendant les périodes de récession")
        )

        mo_2 = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(mo_2, x='Vehicle_Type', y='Automobile_Sales', title="Ventes moyennes par type de véhicule pendant les récessions")
        )

        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec, values='Advertising_Expenditure', names='Vehicle_Type', title="Dépenses publicitaires par type de véhicule pendant les récessions")
        )

        emp_rate = recession_data.groupby('unemployment_rate')['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(emp_rate, x='unemployment_rate', y='Automobile_Sales', title="Impact du taux de chômage sur les ventes d'automobiles")
        )

        return [
            html.Div(className='chart-item', children=[R_chart1, R_chart2], style={'display': 'flex'}),
            html.Div(className='chart-item', children=[R_chart3, R_chart4], style={'display': 'flex'})
        ]

    elif selected_stat == 'Yearly Statistics' and selected_year:
        yearly_data = data[data['Year'] == int(selected_year)]

        Y_chart1 = dcc.Graph(
            figure=px.line(yearly_data, x='Month', y='Automobile_Sales', title=f"Ventes mensuelles d'automobiles pour {selected_year}")
        )

        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(avr_vdata, x='Vehicle_Type', y='Automobile_Sales', title=f"Ventes moyennes de véhicules par type en {selected_year}")
        )

        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data, values='Advertising_Expenditure', names='Vehicle_Type', title=f"Dépenses publicitaires par type de véhicule en {selected_year}")
        )

        return [
            html.Div(className='chart-item', children=[Y_chart1, Y_chart3], style={'display': 'flex'}),
            html.Div(className='chart-item', children=[Y_chart4], style={'display': 'flex'})
        ]

    else:
        return html.Div()

if __name__ == '__main__':
    app.run_server(debug=True)
