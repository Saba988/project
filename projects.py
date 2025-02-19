# # import streamlit as st
# # import pandas as pd
# # import os
# # from io import BytesIO

# # st.set_page_config(page_title="Data Sweeper",layout="wide")

# # #custom css
# # st.markdown(
# #     """
# #     <style>
# #     .stApp{
# #         background-color:white;
# #         color:black;   
# #     }
# #     </style>
# # """
# #     ,
# #     unsafe_allow_html=True
# # )

# # #title and description
# # st.title("Datasweeper Sterling Integrator by Saba Junaid")
# # st.write("Transfrom your files between CSV and Excel format with built-in data cleaning and visualization Creating the project for PITP")


# # #file uploader
# # uploaded_files=st.file_uploader("upload your file (accept CSV or Excel):",type=["csv","xlsx"],accept_multiple_files=True)

# # if uploaded_files:
# #     for file in uploaded_files:
# #         file_ext= os.path.splitext(file.name)[-1].lower

# #         if file_ext == ".csv":
# #             df=pd.read_csv(file)
# #         elif file_ext == ".xlsx":
# #             df=pd.read_excel(file)
# #         else:
# #             st.error(f"Unsupported file type:{file_ext}") 
# #             continue

# #         #file details
# #         st.write("🔍 Preview the head of Dataframe")
# #         st.dataframe(df.head())


# #         #data cleaning options
# #         st.subheader("🛠 Data Cleaning Option")
# #         if st.checkbox(f"Clean data for {file.name}"):
# #             col1, col2 = st.columns(2)

# #             with col1:
# #                 if st.button(f"Remove duplicates from the files:{file.name}"):
# #                     df.drop_duplicates(inplace=True)
# #                     st.write("✅ Duplicates removed!")
# #             with col2:
# #                 if st.button(f"Fill missing values for {file.name}"):
# #                     numeric_cols=df.select_dtypes(include=["number"]).columns
# #                     df[numeric_cols]= df[numeric_cols].fillna(df[numeric_cols].mean())
# #                     st.write("✅ Missing values have been filled!")
# #         st.subheader("🎯 Select Columns to Keep")
# #         columns= st.multiselect (f"Choose columns for {file.name}", df.columns, default=df.columns)    
# #         df= df[columns]



# #         #Data Visualization   
# #         st.subheader("📊 Data Visualization") 
# #         if st.checkbox(f"Show Visualization for {file.name}"):
# #             st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])


# #         #Conversion Option
# #         st.subheader("🔄 Conversion Options")
# #         conversion_type=st.radio(f"Convert {file.name} to:",["CSV","Excel"],key=file.name)    
# #         if st.button(f"Covert {file.name}"):
# #             buffer=BytesIO
# #             if conversion_type == "CSV":
# #                 df.to_csv(buffer, index=False)
# #                 file_name= file.name.replace(file_ext, ".csv")
# #                 mime_type= "text/csv"
# #             elif conversion_type == "Excel":
# #                 df.to_excel(buffer, index=False)
# #                 file_name= file.name.replace(file_ext, ".xlsx")
# #                 mime_type="application/vnd.openxmlformats-officedocumentspreadsheetml.sheet"
# #             buffer.seek(0)  
# #             st.download_button(
# #                 label=f"Download {file.name} as {conversion_type}",
# #                 data=buffer,
# #                 file_name=file_name,
# #                 mime=mime_type
# # )

# # st.success("🎉 All files processed successfully!")              




# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# # Page Configuration
# st.set_page_config(page_title="Data Sweeper", layout="wide")

# # Custom CSS
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: black;
#         color: white;   
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Title and Description
# st.title("Datasweeper Sterling Integrator by Saba Junaid")
# st.write("Transform your files between CSV and Excel format with built-in data cleaning and visualization. Project for PITP.")

# # File Uploader
# uploaded_files = st.file_uploader(
#     "Upload your file (accepts CSV or Excel):", 
#     type=["csv", "xlsx"], 
#     accept_multiple_files=True
# )

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         # File Processing
#         try:
#             if file_ext == ".csv":
#                 df = pd.read_csv(file)
#             elif file_ext == ".xlsx":
#                 df = pd.read_excel(file, engine="openpyxl")
#             else:
#                 st.error(f"❌ Unsupported file type: {file_ext}") 
#                 continue
#         except Exception as e:
#             st.error(f"⚠️ Error loading file {file.name}: {e}")
#             continue

#         # File Preview
#         st.write(f"### 📌 Preview: {file.name}")
#         st.dataframe(df.head())

#         # Data Cleaning Options
#         st.subheader("🛠 Data Cleaning Options")
#         if st.checkbox(f"Clean data for {file.name}"):
#             col1, col2 = st.columns(2)

#             with col1:
#                 if st.button(f"Remove Duplicates ({file.name})"):
#                     df.drop_duplicates(inplace=True)
#                     st.success("✅ Duplicates removed!")

#             with col2:
#                 if st.button(f"Fill Missing Values ({file.name})"):
#                     numeric_cols = df.select_dtypes(include=["number"]).columns
#                     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                     st.success("✅ Missing values filled!")

#         # Column Selection
#         st.subheader("🎯 Select Columns to Keep")
#         selected_columns = st.multiselect(
#             f"Choose columns for {file.name}", 
#             df.columns, 
#             default=df.columns
#         )
#         df = df[selected_columns]

#         # Data Visualization
#         st.subheader("📊 Data Visualization")
#         if st.checkbox(f"Show Visualization for {file.name}"):
#             st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

#         # File Conversion
#         st.subheader("🔄 Convert File")
#         conversion_type = st.radio(
#             f"Convert {file.name} to:", 
#             ["CSV", "Excel"], 
#             key=file.name
#         )

#         if st.button(f"Convert {file.name}"):
#             buffer = BytesIO()
#             if conversion_type == "CSV":
#                 df.to_csv(buffer, index=False)
#                 file_name = file.name.replace(file_ext, ".csv")
#                 mime_type = "text/csv"
#             elif conversion_type == "Excel":
#                 df.to_excel(buffer, index=False, engine="openpyxl")
#                 file_name = file.name.replace(file_ext, ".xlsx")
#                 mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

#             buffer.seek(0)

#             st.download_button(
#                 label=f"⬇️ Download {file_name}",
#                 data=buffer,
#                 file_name=file_name,
#                 mime=mime_type
#             )

# st.success("🎉 All files processed successfully!")   
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout="wide")

# Custom CSS for Better UI
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;
        color: white;
    }
    .css-1aumxhk {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.title("Datasweeper Sterling Integrator by Saba Junaid")
st.write("Transform files between CSV and Excel format with data cleaning & visualization.")

# File Uploader
uploaded_files = st.file_uploader(
    "Upload your file (CSV or Excel):", 
    type=["csv", "xlsx"], 
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # File Processing
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file, engine="openpyxl")
            else:
                st.error(f"❌ Unsupported file type: {file_ext}") 
                continue
        except Exception as e:
            st.error(f"⚠️ Error loading file {file.name}: {e}")
            continue

        # File Preview
        st.write(f"### 📌 Preview: {file.name}")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("🛠 Data Cleaning Options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates ({file.name})"):
                    df.drop_duplicates(inplace=True)
                    st.success("✅ Duplicates removed!")

            with col2:
                if st.button(f"Fill Missing Values ({file.name})"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("✅ Missing values filled!")

        # Column Selection
        st.subheader("🎯 Select Columns to Keep")
        selected_columns = st.multiselect(
            f"Choose columns for {file.name}", 
            df.columns, 
            default=df.columns
        )
        df = df[selected_columns]

        # Data Visualization using Seaborn
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            numeric_columns = df.select_dtypes(include="number").columns

            if len(numeric_columns) >= 2:
                st.write("### 📈 Line Plot for Numeric Columns")

                # Seaborn Style
                sns.set_style("darkgrid")
                plt.figure(figsize=(10, 5))
                
                # Limit to first 300 rows for clarity
                sns.lineplot(data=df.iloc[:300], x=df.index[:300], y=numeric_columns[0], label=numeric_columns[0], color="red")
                sns.lineplot(data=df.iloc[:300], x=df.index[:300], y=numeric_columns[1], label=numeric_columns[1], color="blue")

                plt.xlabel("Index")
                plt.ylabel("Values")
                plt.title("Data Trends")
                plt.legend()
                
                st.pyplot(plt)  # Display the plot in Streamlit
            else:
                st.warning("⚠️ Not enough numeric columns for visualization.")

        # File Conversion
        st.subheader("🔄 Convert File")
        conversion_type = st.radio(
            f"Convert {file.name} to:", 
            ["CSV", "Excel"], 
            key=file.name
        )

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False, engine="openpyxl")
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            st.download_button(
                label=f"⬇️ Download {file_name}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("🎉 All files processed successfully!")   
