import pandas as pd
import plotly.graph_objects as go
from wordcloud import WordCloud

# Example DataFrame
data = {'Word': ['apple', 'banana', 'orange', 'apple', 'orange'],
        'Frequency': [5, 3, 4, 2, 1]}

df = pd.DataFrame(data)

# Generate Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(zip(df['Word'], df['Frequency'])))

# Create Plotly figure
fig = go.Figure()

# Add word cloud to figure
fig.add_trace(go.Image(z=wordcloud.to_array(), hoverinfo='text'))

# Add hover text
hover_text = [f"Word: {word}<br>Frequency: {freq}" for word, freq in zip(df['Word'], df['Frequency'])]
fig.data[0].text = hover_text

# Update layout
fig.update_layout(title='Word Cloud', hovermode='closest')

# Show the figure
fig.show()
