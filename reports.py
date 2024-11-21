import pandas as pd
import plotly.express as px
import streamlit as st

# Streamlit app setup
st.set_page_config(page_title="Management Report Dashboard", layout="wide")

# App title
st.title("Management Report Dashboard")
st.sidebar.header("Upload your CSV file")

# File uploader
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load CSV data
    data = pd.read_csv(uploaded_file)

    # Normalize column names
    data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

    # Ensure required columns exist
    required_columns = {"segment", "book_title", "year", "class", "medium", "subject", "net_sales"}
    if not required_columns.issubset(data.columns):
        st.error(f"Missing required columns. Please ensure the CSV contains the following columns: {', '.join(required_columns)}")
    else:
        # Sidebar filters
        segment_filter = st.sidebar.multiselect("Select Segment", options=data["segment"].unique(), default=data["segment"].unique())
        year_filter = st.sidebar.multiselect("Select Year", options=data["year"].unique(), default=data["year"].unique())

        # Filter data
        filtered_data = data[(data["segment"].isin(segment_filter)) & (data["year"].isin(year_filter))]

        # Year-over-Year Growth Segment-Wise
        st.subheader("Segment-Wise Year-over-Year Growth (Bar Chart)")

        # Calculate YoY growth for each segment
        segment_growth = filtered_data.groupby(["segment", "year"])["net_sales"].sum().reset_index()
        segment_growth["yoy_growth"] = segment_growth.groupby("segment")["net_sales"].pct_change() * 100

        # Add labels for formatting growth percentages
        segment_growth["yoy_growth_label"] = segment_growth["yoy_growth"].apply(lambda x: f"{x:.2f}%" if pd.notnull(x) else "N/A")

        # Create bar chart for YoY growth
        fig = px.bar(
            segment_growth,
            x="year",
            y="yoy_growth",
            color="segment",
            barmode="group",
            title="Segment-Wise Year-over-Year Growth (Grouped Bar Chart)",
            labels={"yoy_growth": "YoY Growth (%)", "year": "Year", "segment": "Segment"},
            text="yoy_growth_label",
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(
            yaxis_tickformat=".2f",
            yaxis_title="YoY Growth (%)",
            xaxis_title="Year",
            legend_title="Segments",
            bargap=0.2  # Space between bars
        )
        st.plotly_chart(fig, use_container_width=True)

        # Other visualizations
        st.subheader("Segment-Wise Total Sales")
        segment_sales = filtered_data.groupby("segment")["net_sales"].sum().reset_index()
        fig1 = px.bar(
            segment_sales,
            x="segment",
            y="net_sales",
            title="Segment-Wise Sales",
            text="net_sales",
            labels={"net_sales": "Net Sales"}
        )
        fig1.update_traces(texttemplate='%{text:.0f}', textposition='outside')
        fig1.update_layout(yaxis_tickformat=".0f")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Top Products by Segment")
        top_products = filtered_data.groupby(["segment", "book_title"])["net_sales"].sum().reset_index()
        top_products = top_products.sort_values(by="net_sales", ascending=False).groupby("segment").head(3)
        fig2 = px.bar(
            top_products,
            x="segment",
            y="net_sales",
            color="book_title",
            title="Top Products by Segment",
            text="net_sales",
            labels={"net_sales": "Net Sales"}
        )
        fig2.update_traces(texttemplate='%{text:.0f}', textposition='outside')
        fig2.update_layout(yaxis_tickformat=".0f")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Top Medium Students Like")
        top_medium = filtered_data.groupby("medium")["net_sales"].sum().reset_index()
        fig3 = px.pie(
            top_medium,
            values="net_sales",
            names="medium",
            title="Top Medium by Net Sales",
            labels={"net_sales": "Net Sales"}
        )
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("Top Subjects Students Like")
        top_subject = filtered_data.groupby("subject")["net_sales"].sum().reset_index()
        fig4 = px.bar(
            top_subject,
            x="subject",
            y="net_sales",
            title="Top Subjects by Net Sales",
            text="net_sales",
            labels={"net_sales": "Net Sales"}
        )
        fig4.update_traces(texttemplate='%{text:.0f}', textposition='outside')
        fig4.update_layout(yaxis_tickformat=".0f")
        st.plotly_chart(fig4, use_container_width=True)

        # Summary Metrics
        st.sidebar.header("Summary Metrics")
        total_sales = filtered_data["net_sales"].sum()
        st.sidebar.metric("Total Net Sales", f"${total_sales:,.2f}")

else:
    st.write("Please upload a CSV file to see the dashboard.")
