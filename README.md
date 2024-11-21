Management Report Dashboard
A Streamlit application for creating an interactive management report dashboard using a CSV file. This dashboard provides visual insights into various metrics, including Year-over-Year growth, segment-wise sales, top products, and customer preferences.

Features
CSV File Upload: Upload your custom data in CSV format.
Interactive Filters: Filter the data by segment and year for tailored analysis.
Visualizations:
Year-over-Year Growth (Bar Chart): Displays growth percentages by segment.
Segment-Wise Total Sales: View total sales for each segment.
Top Products by Segment: Identify the top-performing products for each segment.
Top Medium Preferences (Pie Chart): Insights into preferred media by sales.
Top Subjects: Discover the most popular subjects by sales.
Summary Metrics: Highlights total net sales for the filtered data.
Installation
Clone this repository or download the source files.

Install the required Python packages using pip:

bash
Copy code
pip install pandas plotly streamlit
Run the application:

bash
Copy code
streamlit run app.py
Usage
Prepare a CSV file containing the following required columns:
segment
book_title
year
class
medium
subject
net_sales
Start the application and upload the CSV file through the sidebar.
Use the filters on the sidebar to refine your analysis.
Explore the interactive visualizations and summary metrics displayed in the dashboard.
Sample CSV File Format
segment	book_title	year	class	medium	subject	net_sales
Segment1	Book A	2023	10	English	Science	5000
Segment2	Book B	2023	9	Hindi	Math	3000
Segment1	Book C	2022	10	English	History	4500
Ensure the column names match the above format.

Requirements
Python 3.7 or higher
Required Python libraries: pandas, plotly, streamlit
Customization
You can extend or modify the application to suit your specific needs by adding:

Additional filters or metrics.
Different chart types or visualizations.
Integration with databases or APIs for dynamic data loading.
License
This project is licensed under the MIT License. Feel free to modify and distribute it.

Let me know if you'd like additional adjustments or details!
