import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Political Matrix", layout="wide")

# Title + subtitle
st.title("Smartmap für die Winterthurer Erneuerungswahlen des Stadtparlaments 2026")
st.markdown(
    """
    Diese Visualisierung wird euch präsentiert von der GLP 🟢🔵😉  
    Daher Werbung:
    """
)

# Image instead of GIF
st.image("data/logo.png")

df = pd.read_csv('data/processed/candidates_answers_processed.csv')

filter_option = st.radio(
    "Filter:",
    ["All", "Elected", "Not Elected"],
    horizontal=True
)

show_centers = st.toggle("Show Party Centers", value=False)

if filter_option == "Elected":
    df = df[df["Elected"] == 1]
elif filter_option == "Not Elected":
    df = df[df["Elected"] == 0]

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

if show_centers:
    # Compute per-party averages and show only those
    centers = df.groupby("Party")[["x", "y"]].mean().reset_index()

    for _, row in centers.iterrows():
        party = row["Party"]
        color = party_colors.get(party, "#AAAAAA")
        border = party_border.get(party, color)

        fig.add_trace(go.Scatter(
            x=[row["x"]],
            y=[row["y"]],
            mode="markers+text",
            name=party,
            marker=dict(
                color=color,
                size=22,
                line=dict(color=border if party in party_border else "#333333", width=2),
                symbol="circle",
            ),
            text=[party],
            textposition="top center",
            textfont=dict(color="white", size=12),
            hovertext=f"{party}<br>Ø x: {row['x']:.3f}<br>Ø y: {row['y']:.3f}",
            hoverinfo="text",
        ))
else:
    # Show all individual candidates
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
    ),
    yaxis=dict(
        title="← Konservativ | Liberal →",
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