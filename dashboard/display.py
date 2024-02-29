import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from dbConn import main
import time

#set_pageconfig should be the first element of the page
st.set_page_config(page_title='Survey Results')
st.header('Item Status')
data1, data2,data3 = main.dbConn()

columns = ['item','status']
df1 = pd.DataFrame(data1, columns=columns)
df2 = pd.DataFrame(data2, columns=columns)
df3 = pd.DataFrame(data3, columns=columns)

combined_df = pd.concat([df1, df2, df3])
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
        st.line_chart(combined_df.set_index('item'))


# Display the data in Streamlit
st.write("Data from the database:")
st.write(df1)
# to display all dashboards
if st.button('Show Dashboards'):
    # Call functions to display dashboards
    # line chart type 2
    st.line_chart(combined_df,x='item', y='status')

#display the graph in the main page
show_graph=st.sidebar.button('display in main screen')
if show_graph:
    #display syntax 1
    st.area_chart(combined_df)
    
st.write("\ndisplaying chart based on the selection")
# --- STREAMLIT SELECTION
Item = combined_df['item'].unique().tolist()
Status = combined_df['status'].unique().tolist()

#------------------------------multi select options-------------------------------
    # Multiselect for selecting status - dropdown
# selected_status = st.multiselect('Select Status', Status)
    # Multiselect for selecting status - display
selected_status = st.multiselect('Status:',
                                    Status,
                                    default=Status)
#-------------------------------
# Filter the data based on the selected status
filtered_df = combined_df[combined_df['status'].isin(selected_status)]
#to display the quantity
number_of_result = filtered_df.shape[0]
st.markdown(f'*Item count: {number_of_result}*')
# Create a bar chart based on the selected status
# The shape tuple contains two elements: the number of rows and the number of columns. Therefore, filtered_df.shape[0] accesses the first element of the tuple, which represents the number of rows in the DataFrame filtered_df.
if filtered_df.shape[0] > 0:
    st.bar_chart(filtered_df.groupby('status').size())
else:
    st.write("No data available for the selected status.")























# status_counts = df['status'].value_counts().reset_index()
# status_counts.columns = ['Status', 'Count']

# # Plot the bar chart using Plotly Express
# fig = px.bar(status_counts, x='Status', y='Count', title='Count of Status')
# st.plotly_chart(fig)

# # Plot the pie chart using Plotly Express
# fig = px.pie(status_counts, values='Count', names='Status', title='Status Distribution')
# st.plotly_chart(fig)
