import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Political Matrix", layout="wide")

# Title + subtitle
st.title("Smartmap für die Winterthurer Erneuerungswahlen des Stadtparlaments 2026")

st.markdown(
    """
    Diese Visualisierung wird euch präsentiert von der wohl **lösungsorientiertesten Partei der Schweiz** – der GLP 🟢🔵😉  
    Politik, aber mit Daten statt Parolen.
    """
)

# Fun GIF
st.image(
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGpjNnQ3d3oxNDk2NjNrcWJwejBwaHZ2NnM5NDk3MHNyOHBmd2VqYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5z0cCCGooBQUtejM4v/giphy.gif",
    width=300,
    caption="Keine Smartmap? keine Angst die GLP Winti macht euch eine"
)

df = pd.read_csv('data/processed/candidates_answers_processed.csv')

# Normalize to [-1, 1]
def normalize(series):
    min_val = series.min()
    max_val = series.max()
    return 2 * (series - min_val) / (max_val - min_val) - 1

df["x"] = normalize(df["Links_Rechts"])
df["y"] = -normalize(df["Liberal_Konservativ"])

# Party colors
party_colors = {
    "EDU": "#FFFFFF",
    "AL": "#000000",
    "EVP": "#FFD700",
    "Mitte": "#FFA500",
    "GLP": "#90EE90",
    "Grüne": "#228B22",
    "FDP": "#ADD8E6",
    "SVP": "#4CAF50",
    "SP": "#E53935",
}

party_border = {
    "EDU": "#999999",
    "AL": "#555555",
}

fig = go.Figure()

for party, group in df.groupby("Party"):
    color = party_colors.get(party, "#AAAAAA")
    border = party_border.get(party, color)

    fig.add_trace(go.Scatter(
        x=group["x"],
        y=group["y"],
        mode="markers",
        name=party,
        marker=dict(
            color=color,
            size=12,
            line=dict(color=border if party in party_border else "#333333", width=1.5),
        ),
        text=group["Name"] + "<br>Partei: " + group["Party"],
        hoverinfo="text",
    ))

fig.update_layout(
    xaxis=dict(
        title="← Links | Rechts →",
        range=[-1.1, 1.1],
        zeroline=True,
        zerolinecolor="gray",
        zerolinewidth=1,
        showgrid=True,
        gridcolor="#333333",
        scaleanchor="y",
        scaleratio=1,
    ),
    yaxis=dict(
        title="Konservativ ↓| ↑ Liberal ",
        range=[-1.1, 1.1],
        zeroline=True,
        zerolinecolor="gray",
        zerolinewidth=1,
        showgrid=True,
        gridcolor="#333333",
    ),
    plot_bgcolor="#1a1a2e",
    paper_bgcolor="#0f0f1a",
    font=dict(color="white"),
    legend=dict(
        bgcolor="#1a1a2e",
        bordercolor="#444",
        borderwidth=1,
    ),
    width=1000,
    height=1000,
)

st.plotly_chart(fig, use_container_width=False)

st.caption("X-axis: Links (left) ← → Rechts (right) | Y-axis: Liberal (top) ↓ Konservativ (bottom)")