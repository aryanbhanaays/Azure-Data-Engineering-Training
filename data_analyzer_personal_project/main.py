# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO

gradient_text_css = """
    <style>
    .gradient-text {
        font-weight: bold;
        background: -webkit-linear-gradient(left, #007BFF, #887c7a);
        background: linear-gradient(to right, #007BFF, #887c7a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
        font-size: 3em;
        position: relative;
        overflow: hidden;
    }
    .gradient-text:hover::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 200%;
        height: 100%;
        background: linear-gradient(to right, rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0));
        animation: shine 0.5s forwards linear;
    }

    @keyframes shine {
        to {
            left: 100%;
        }
    }
    </style>
"""

st.markdown(gradient_text_css, unsafe_allow_html=True)
st.markdown('<div class="gradient-text" data-content="CodeBuddy.io">Sales Analysis</div>', unsafe_allow_html=True)

with open("ui/sidebar.md", "r") as sidebar_file:
    sidebar_content = sidebar_file.read()

with open("ui/styles.md", "r") as styles_file:
    styles_content = styles_file.read()


st.sidebar.markdown(sidebar_content)
href = f'<a href="https://github.com/aryanbhanaays" style="text-decoration: none;color: white;">Visit Website</a>'    

styled_button_html2 = f"<div style='text-align: center;padding: 5px 10px; font-size: 12px'><button class='button-62' role='button'><span class='text'>{href}</span></button></div>"
st.sidebar.markdown(styled_button_html2, unsafe_allow_html=True)

st.write(styles_content, unsafe_allow_html=True)
def calculate_average_costs(items_df, sales_df):
    """
    Calculate the average cost of items sold within their valid date ranges
    
    Args:
    items_df (DataFrame): DataFrame containing item data.
    sales_df (DataFrame): DataFrame containing sales data.
    
    The items_df should have columns: ItemId, StartDate, EndDate, Price.
    The sales_df should have columns: SalesId, ItemId, NumSales, SalesDate.
    
    Returns:
    DataFrame: DataFrame with ItemId and AvgCost columns.
    """
    
    merged_df = pd.merge(sales_df, items_df, on='ItemId')
    merged_df['SalesDate'] = pd.to_datetime(merged_df['SalesDate'])
    merged_df['StartDate'] = pd.to_datetime(merged_df['StartDate'])
    merged_df['EndDate'] = pd.to_datetime(merged_df['EndDate'])

    filtered_df = merged_df[(merged_df['SalesDate'] >= merged_df['StartDate']) & 
                            (merged_df['SalesDate'] <= merged_df['EndDate'])].copy()
    filtered_df.loc[:, 'TotalSalesValue'] = filtered_df['NumSales'] * filtered_df['Price']  

    avg_cost_df = (filtered_df.groupby('ItemId')['TotalSalesValue'].sum() /
                   filtered_df.groupby('ItemId')['NumSales'].sum()).reset_index()
    avg_cost_df.columns = ['ItemId', 'AvgCost']
    return avg_cost_df, filtered_df

def main():

    st.write("""
    ### Upload Your CSV Files
    Upload the Items and Sales CSV files to calculate the average cost of items sold. 
    If you don't have files, you can use the demo data provided.
    """)

    items_file = st.file_uploader("Upload Items CSV", type=["csv"])
    sales_file = st.file_uploader("Upload Sales CSV", type=["csv"])

    use_demo_data = st.checkbox("Use demo data")

    if (items_file and sales_file) or use_demo_data:
        if use_demo_data:
            items_csv = """ItemId,StartDate,EndDate,Price
                            1,2022-01-01,2022-12-31,10
                            2,2022-01-01,2022-12-31,20
                            3,2022-06-01,2022-12-31,30
                            4,2022-01-01,2022-12-31,25
                            5,2022-03-01,2022-11-30,15
                            6,2022-05-01,2022-12-31,35
                        """
            sales_csv = """SalesId,ItemId,NumSales,SalesDate
                            1,1,10,2022-01-15
                            2,2,5,2022-07-15
                            3,3,2,2022-06-15
                            4,3,3,2023-01-01
                            5,4,7,2022-02-01
                            6,5,8,2022-04-15
                            7,6,6,2022-06-10
                            8,1,9,2022-07-20
                            9,2,4,2022-08-05
                            10,5,7,2022-09-12
                            11,6,3,2022-11-22
                        """
            items_df = pd.read_csv(StringIO(items_csv))
            sales_df = pd.read_csv(StringIO(sales_csv))
        else:
            items_df = pd.read_csv(items_file)
            sales_df = pd.read_csv(sales_file)

        item_data, sales_data = st.columns(2)
        with item_data:
            st.write("### Items Data")
            st.write(items_df)
        with sales_data:
            st.write("### Sales Data")
            st.write(sales_df)
        
        if st.button("Calculate Average Cost"):
            avg_cost_df, filtered_df = calculate_average_costs(items_df, sales_df)
            st.write("### Average Cost of Items Sold")
            st.write(avg_cost_df)
            csv = avg_cost_df.to_csv(index=False)
            st.download_button(
                label="Download Average Costs CSV",
                data=csv,
                file_name='avg_costs.csv',
                mime='text/csv',
            )
            st.write("## Analysis and Visualization")
            st.write("### Total Sales per Item")
            sales_per_item = filtered_df.groupby('ItemId')['NumSales'].sum().reset_index()
            fig = px.bar(sales_per_item, x='ItemId', y='NumSales', title='Total Sales per Item', color='NumSales')
            st.plotly_chart(fig)
            st.write("### Average Cost per Item")
            fig = px.bar(avg_cost_df, x='ItemId', y='AvgCost', title='Average Cost per Item', color='AvgCost')
            st.plotly_chart(fig)
            st.write("### Total Sales Value per Item")
            total_sales_value = filtered_df.groupby('ItemId')['TotalSalesValue'].sum().reset_index()
            fig = px.pie(total_sales_value, names='ItemId', values='TotalSalesValue', title='Total Sales Value Distribution')
            st.plotly_chart(fig)
            st.markdown("""
                            <style>
                            .footer {
                                position: fixed;
                                left: 0;
                                bottom: 0;
                                width: 100%;
                                background-color: white;
                                color: black;
                                text-align: center;
                                padding: 10px;
                                font-size: 12px;
                            }
                            </style>
                            <div class="footer">
                            Made with ❤️ by Aryan Bhan
                            </div>
                            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
