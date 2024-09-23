import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.title("Lebanon's External Debt Visualizations")
st.write(
    "Explore Lebanon's external debt trends across the years (1960 - 2022) with interactive visualizations."
)

# Load the data
data = pd.read_csv('https://linked.aub.edu.lb/pkgcube/data/ec4c40221073bbdf6f75b6c6127249c3_20240905_173222.csv')

# Display a brief data overview
with st.expander("View Data Sample"):
    st.write(data.head())  # Show the first few rows of the data

# Line chart visualization: External debt over the years
with st.container():
    st.subheader("Line Chart: External Debt Over the Years")
    
    # Create the slider for the line chart
    year_slider_line = st.slider(
        'Select year range for line chart:',
        min_value=int(data['refPeriod'].min()),
        max_value=int(data['refPeriod'].max()),
        value=(int(data['refPeriod'].min()), int(data['refPeriod'].max()))  # Default to full range
    )
    
    # Filter the data for the line chart
    filtered_df_line = data[(data['refPeriod'] >= year_slider_line[0]) & (data['refPeriod'] <= year_slider_line[1])]
    
    # Create the line chart using filtered data
    fig_line = px.line(filtered_df_line, x='refPeriod', y='Value', title="External Debt Trend (Filtered by Year Range)")
    st.plotly_chart(fig_line, use_container_width=True)

# Scatter plot visualization: Debt distribution over the years
with st.container():
    st.subheader("Scatter Plot: External Debt Distribution")
    st.write("This scatter plot provides a more detailed view of Lebanon's external debt at individual points across the selected time range.")
    
    # Create the slider for the scatter plot
    year_slider_scatter = st.slider(
        'Select year range for scatter plot:',
        min_value=int(data['refPeriod'].min()),
        max_value=int(data['refPeriod'].max()),
        value=(int(data['refPeriod'].min()), int(data['refPeriod'].max()))  # Default to full range
    )
    
    # Filter the data for the scatter plot
    filtered_df_scatter = data[(data['refPeriod'] >= year_slider_scatter[0]) & (data['refPeriod'] <= year_slider_scatter[1])]
    
    # Create a scatter plot using the filtered data
    fig_scatter = px.scatter(filtered_df_scatter, x="refPeriod", y="Value", title="External Debt Distribution (Filtered by Year Range)")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Interpretation and insights below both visualizations
st.write("""
#### Line Chart:
- The **line chart** visualizes the overall trend in Lebanon’s external debt. It helps to observe whether the debt was increasing, stabilizing, or decreasing over the selected periods.
- For example, Lebanon's external debt increased substantially from **2008** to **2010**, rising from around **$44 billion** to over **$80 billion**. This period may reflect significant economic changes or borrowing patterns during that time leading to the 2019 economic crisis.
- By focusing on particular ranges using the slider, you can see how specific periods of financial history, such as economic crises or recoveries, affected the debt. This visualization highlights long-term patterns, which are useful for tracking economic changes.

#### Scatter Plot:
- The **scatter plot** complements the line chart by focusing on individual debt values at specific points in time. This chart can help identify outliers or patterns that are not as visible in the line chart.
- Between **2000** and **2013**, the scatter plot shows consistently high debt values, fluctuating between **$20 billion** and **$62 billion**, reflecting Lebanon's increasing reliance on external debt during that decade.
- By adjusting the slider, you can zoom in on particular years to better understand how Lebanon’s debt was distributed over the years. Unusual spikes or dips in the scatter plot may indicate specific events, such as financial crises or changes in government policies, affecting the country’s debt.

#### Combining Both Charts:
- Both visualizations together provide a comprehensive view of Lebanon’s external debt. While the line chart gives a broad overview of the trend, the scatter plot offers a more granular look at individual data points. 
- Using the sliders, you can explore different time ranges and understand how the debt evolved during critical moments in Lebanon's financial history. For instance, the charts reveal a significant rise in debt between **2000** and **2010**, followed by a more stable but high level of debt in the subsequent years.

In conclusion, these visualizations allow for an in-depth analysis of Lebanon’s external debt by exploring both trends and granular data points. The ability to interactively adjust the time range makes it easier to understand how Lebanon’s debt evolved during various periods.
""")
