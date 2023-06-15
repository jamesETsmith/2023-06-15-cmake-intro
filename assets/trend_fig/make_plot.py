import plotly.express as px
import pandas as pd

import plotly.graph_objects as go
import plotly.io as pio


axis_settings = dict(
    ticks="outside",
    mirror=True,
    showline=True,
    linewidth=2,
    zeroline=False,
    showgrid=False,
)
pio.templates["jets_talk"] = go.layout.Template(
    layout=dict(
        font=dict(size=24),
        font_family="DejaVu Sans",
        xaxis=axis_settings,
        yaxis=axis_settings,
        colorway=[
            "#1f77b4",
            "#ff7f0e",
            "#2ca02c",
            "#d62728",
            "#9467bd",
            "#8c564b",
            "#e377c2",
            "#7f7f7f",
            "#bcbd22",
            "#17becf",
        ],
        # margin=dict(l=10, r=10, t=30, b=10),
    )
)
pio.templates.default = "jets_talk"

df = pd.read_csv("data.csv")
df = pd.melt(df, id_vars=["Month"], var_name="Build System", value_name="Search Metric")
print(df.head())
fig = px.line(df, x="Month", y="Search Metric", color="Build System")
fig.update_traces(line=dict(width=5))
fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
fig.write_html("build_system_trends.html")
