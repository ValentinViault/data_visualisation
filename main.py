# Lignes d'import / Import lines
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go

# Ouverture du fichier et lecture via panda / Opening the file and reading using pandas
file = 'C:\\Users\\User\\Desktop\\Portfolio_Python\\projet_data_visualisation\\data\\Superstore.csv'
df = pd.read_csv(file)

# Voir comment le CSV est articulé et ses en-tête / Looking at the CSV and its headers
print(df.head())
print(df.info())

# Montrer les 10 premiers résultats / Showing the 10 first results
print(df["Order Date"].head(10))

# Changer le format de date, et utiliser coerce pour éviter la casse / Change the datetime format and use coerce to prevent breaking
df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')

print(df.info())
print(df["Order Date"].isna().sum())

# Grouper les données par catégorie / Group the data by category
category_result = df.groupby("Category")["Profit"].sum()
print(category_result)

year_result = df.groupby(df["Order Date"].dt.year)["Profit"].sum().sort_index()
print(year_result)

monthly_result = df.groupby(df["Order Date"].dt.to_period("M"))["Profit"].sum().reset_index()
monthly_result["Order Date"] = monthly_result["Order Date"].dt.to_timestamp()

# Chaque mois de chaque année / Every months of each year
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# reset_index() pour passer d'un MultiIndex à un axe x / Switching from a MultiIndex to a x axis using reset_index()
monthly = df.groupby(["Year", "Month"])["Profit"].sum().reset_index()

# Recréer une vraie date / Recreate a proper date
monthly["Date"] = pd.to_datetime(monthly[["Year", "Month"]].assign(DAY='1'))

# Afficher les résultats dans un graphique / Showing the results with a graph
fig = px.line(monthly, x="Date", y="Profit", title="Évolution du profit mensuel", markers=True)
fig.show()

# Enquête sur mars 2013 / Investigating on March 2013
march_2013 = df[(df["Year"] == 2013) & (df["Month"] == 3)]
result_march_2013 = march_2013.groupby("Category")["Profit"].sum()
print(result_march_2013)

# Enquête sur mai 2014 / Investigating on May 2014
may_2014 = df[(df["Year"] == 2014) & (df["Month"] == 5)]
result_may_2014 = may_2014.groupby("Category")["Profit"].sum()
print(result_may_2014)

# Profit par catégorie / Profit per category
category_result = df.groupby("Category")["Profit"].sum().reset_index()

# Graphiques et DashBoard / Graphs and DashBoard
fig = make_subplots(
    rows=2,
    cols=1,
    subplot_titles=('Profit par catégorie','Profit mensuel')
    )

fig.add_trace(
    go.Bar(
        x=category_result["Category"],
        y=category_result["Profit"],
        name="Profit catégorie"
    ),
    row=1,
    col=1,
)

fig.add_trace(
    go.Scatter(
        x=monthly_result["Order Date"],
        y=monthly_result["Profit"],
        mode="lines+markers",
        name="Profit mensuel",
    ),
    row=2,
    col=1,
)
fig.update_layout(
    title="Mini-Dashboard - Analyse des Profits",
    height=700,
    showlegend=True,
    template="plotly_white",
)
fig.write_image("images\dashboard.png")

fig.show()
