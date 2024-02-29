import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from dbConn import main
import time

#set_pageconfig should be the first element of the page
st.set_page_config(page_title='Survey Results')
st.header('Item Status')
data4 = main.dbConn()

columns = ['order_id','ship_mode']
df1 = pd.DataFrame(data4, columns=columns)


combined_df = pd.concat([df1])
with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

    #button inside side bar
    if st.button('Displaying charts inside side bar '):
        # Call functions to display dashboards
        #line chart - type 1
        st.line_chart(combined_df.set_index('order_id'))


# Display the data in Streamlit
st.write("Data from the database:")
st.write(df1)
# to display all dashboards
if st.button('Show Dashboards'):
    # Call functions to display dashboards
    # line chart type 2
    st.line_chart(combined_df,x='order_id', y='ship_mode')

#display the graph in the main page
show_graph=st.sidebar.button('display in main screen')
if show_graph:
    #display syntax 1
    st.area_chart(combined_df)
    
st.write("\ndisplaying chart based on the selection")
# --- STREAMLIT SELECTION
order_id = combined_df['order_id'].unique().tolist()
ship_mode = combined_df['ship_mode'].unique().tolist()

#------------------------------multi select options-------------------------------
    # Multiselect for selecting status - dropdown
# selected_status = st.multiselect('Select Status', Status)
    # Multiselect for selecting status - display
selected_ship_mode = st.multiselect('ship_mode:',
                                    ship_mode,
                                    default=ship_mode)
#-------------------------------
# Filter the data based on the selected status
filtered_df = combined_df[combined_df['ship_mode'].isin(selected_ship_mode)]
#to display the quantity
number_of_result = filtered_df.shape[0]
st.markdown(f'*order_id count: {number_of_result}*')
# Create a bar chart based on the selected status
# The shape tuple contains two elements: the number of rows and the number of columns. Therefore, filtered_df.shape[0] accesses the first element of the tuple, which represents the number of rows in the DataFrame filtered_df.
if filtered_df.shape[0] > 0:
    st.bar_chart(filtered_df.groupby('ship_mode').size())
else:
    st.write("No data available for the selected ship_mode.")























# status_counts = df['status'].value_counts().reset_index()
# status_counts.columns = ['Status', 'Count']

# # Plot the bar chart using Plotly Express
# fig = px.bar(status_counts, x='Status', y='Count', title='Count of Status')
# st.plotly_chart(fig)

# # Plot the pie chart using Plotly Express
# fig = px.pie(status_counts, values='Count', names='Status', title='Status Distribution')
# st.plotly_chart(fig)