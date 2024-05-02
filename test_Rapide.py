import pandas as pd
import io
#
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import pandas as pd
# import plotly.express as px


# Chargement des données
#
# file_url = r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
# file_path = Path(r'C:\Users\y_mc\PycharmProjects\YokAi\Dataset\historical_automobile_sales.csv')

# def download_csv(path):
#     csv_data = path
#     response = requests.get(csv_data)
#
#     print("envoi de la requete....attente de reponse")
#
#     if response.status_code == 200:
#         print("requete accepte...\n debut du telechargement")
#         with open('historical_automobile_sales.csv', 'wb') as file:
#             file.write(response.content)
#         print("Fichier telecharger avec succes")
#     else:
#         print("Erreur de telechargement..........")
#
#     return "Operation Termine "
#
# download_csv(file_url)
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Restaurant tips by day of week'),
    dcc.Dropdown(
        id="dropdown",
        options=["Fri", "Sat", "Sun"],
        value="Fri",
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"))
def update_bar_chart(day):
    df = px.data.tips() # replace with your own data source
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill",
                 color="smoker", barmode="group")
    return fig


app.run_server(debug=True)








#
# Dataset = 'C:\Users\y_mc\PycharmProjects\YokAi\Dataset\historical_automobile_sales.csv'
# data = pd.read_csv(Dataset)
"""
print(data.columns)

figure = px.bar(data, x='Year', y='Automobile_Sales',
                title="Fluctuation moyenne des ventes d'automobiles pendant les périodes de récession")
figure.show()

#
#
mo_chart = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
# # R_chart1 = dcc.Graph(figure=px.bar(yearly_rec, x='Year', y='Automobile_Sales',title="Fluctuation moyenne des ventes d'automobiles pendant les périodes de récession"))
fig = px.line(mo_chart, x="Year", y="Automobile_Sales", title='fluctuation ')
fig.show()

exp_rec = data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()

mo_chart_2 = px.pie(exp_rec, values='Advertising_Expenditure', names='Vehicle_Type', title="Dépenses publicitaires par type de véhicule pendant les récessions")

mo_chart_2.show()


emp_rate = data.groupby('unemployment_rate')['Automobile_Sales'].mean().reset_index()
R_chart4 =px.bar(emp_rate, x='unemployment_rate', y='Automobile_Sales', title="Impact du taux de chômage sur les ventes d'automobiles")
R_chart4.show()





# with open('Dataset/historical_automobile_sales.csv','r') as file:
#     dataset = file.read()
#
# dataset_file = io.StringIO(dataset)
# data_ = pd.read_csv(dataset_file)
# print(data_.head())




"""