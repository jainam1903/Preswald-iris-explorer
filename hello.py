from preswald import text, plotly, connect, get_df, table, slider
import plotly.express as px
import plotly.graph_objects as go

# Title
text("# 🌸 Iris Species Explorer")
text("Explore Sepal and Petal sizes across different Iris species.")

# Load the dataset
connect()
df = get_df('iris')  

# Scatter Plot: PetalLength vs PetalWidth
fig = px.scatter(
    df,
    x='PetalLengthCm',
    y='PetalWidthCm',
    color='Species',
    title='Petal Length vs Width by Species',
    labels={'PetalLengthCm': 'Petal Length (cm)', 'PetalWidthCm': 'Petal Width (cm)'}
)

fig.update_traces(marker=dict(size=10))
fig.update_layout(template='plotly_white')
plotly(fig)

# Full table
table(df, title="📊 Full Iris Dataset")

# Slider for filtering
threshold = slider("Min Sepal Length (cm)", min_val=4.0, max_val=8.0, default=5.0)
filtered_df = df[df["SEPALLENGTHCM"] >= threshold]
table(filtered_df, title="Filtered Data (Sepal Length ≥ Threshold)")