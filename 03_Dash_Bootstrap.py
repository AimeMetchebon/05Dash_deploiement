#Utilisez Plotly Express pour créer un graphique en barres des 10 premiers livres, en 
#affichant le nombre de pages par titre
from dash import Dash, html, dash_table,dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv', on_bad_lines = 'skip')
df = df.head(10)


# Création de l'application Dash
#app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout



app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("Choisissez un auteur"),
                dcc.Dropdown(
                    id='dropdown-exemple',
                    options=[{'label': i, 'value': i} for i in df['authors'].unique()],
                    value=df['authors'][0]
                ),
            ]
        ),
        
        html.Div(
            [
                dbc.Label("Choix du nombre Max de pages"),
                dbc.Input(id='input-exemple', type="number", value=500),
            ]
        ),
    ],
    body=True,
)

app.layout = dbc.Container(
    [
        html.H1("Ma première visualisation Dash-Bootstrap"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(dcc.Graph(id="mon-graphique")),
            ],
            align="center",
        ),
    ],
    fluid=True,
)


# La fonction de rappel
@app.callback(
    Output('mon-graphique', 'figure'),
    [Input('dropdown-exemple', 'value'),
     Input('input-exemple', 'value')]
    

)
def update_graph1(dropdown_exemple,input_exemple):
    # Filtrer les données pour consider l'auteur choisie'
  
    if input_exemple == 'Nombre maximal de page':
        data_filtered = df[df['authors'] == dropdown_exemple]
    else:
        data_filtered = df[df['authors'] == dropdown_exemple][df['  num_pages'] <= input_exemple]

    # Créer le graphique
    fig = px.histogram(data_filtered, x= 'title', y= '  num_pages' , histfunc='avg')
    fig.update_layout(title='Livre(s) par Auteur', xaxis_title='Titre', yaxis_title='Nombre de pages')

    return fig






# Exécution de l'application
if __name__ == '__main__':
    app.run_server(debug=True)
