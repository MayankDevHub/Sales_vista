import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Sales Vista")

# File uploader
uploaded_file = st.file_uploader("Upload your sales CSV file to get the prediction for next six months", type=['csv'])

if uploaded_file is not None:
    try:
        # Load the uploaded data
        data = pd.read_csv(uploaded_file)
        
        st.success("File uploaded successfully!")
        st.subheader("Data Preview")
        st.dataframe(data.head(10))
        
        # Show data info
        st.write(f"Total rows: {len(data)}")
        st.write(f"Columns: {', '.join(data.columns.tolist())}")
        
        # Let user select columns
        st.subheader("Select Columns")
        date_column = st.selectbox("Select Date/Month Column", data.columns.tolist())
        sales_column = st.selectbox("Select Sales Column", data.columns.tolist())
        
        if st.button("Analyze & Predict"):
            # Create a copy to avoid modifying original
            df = data.copy()
            
            # Process the data
            df[date_column] = pd.to_datetime(df[date_column])
            df = df.sort_values(date_column)
            df.set_index(date_column, inplace=True)
            
            # Training the model
            df['Month_Num'] = np.arange(len(df))
            X = df[['Month_Num']]
            y = df[sales_column]
            model = LinearRegression()
            model.fit(X, y)
            
            # Display model performance
            score = model.score(X, y)
            st.info(f"Model R² Score: {score:.4f} ({score*100:.2f}% accuracy)")
            
            # Forecasting next 6 months
            future_months = np.arange(len(df), len(df)+6).reshape(-1, 1)
            forecast = model.predict(future_months)
            
            # Displaying historical sales
            st.subheader("Historical Sales")
            st.line_chart(df[sales_column])
            
            # Displaying the forecast
            forecast_index = pd.date_range(start=df.index[-1] + pd.DateOffset(months=1), periods=6, freq='M')
            forecast_df = pd.DataFrame({
                'Forecasted Sales': forecast
            }, index=forecast_index)
            
            st.subheader("Forecasted Sales for Next 6 Months")
            st.line_chart(forecast_df)
            
            # Show forecast values in a table
            st.subheader("Forecast Details")
            forecast_table = pd.DataFrame({
                'Month': forecast_index.strftime('%B %Y'),
                'Predicted Sales': forecast.round(2)
            })
            st.dataframe(forecast_table)
            
            # Download forecast
            csv = forecast_table.to_csv(index=False)
            st.download_button(
                label="Download Forecast as CSV",
                data=csv,
                file_name="sales_forecast.csv",
                mime="text/csv"
            )
            
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        st.info("Please make sure your CSV file has proper date and sales columns")

else:
    st.info("👆 Please upload a CSV file to begin analysis")
    
    # Show example format
    st.subheader("Expected CSV Format Example")
    example_df = pd.DataFrame({
        'Date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
        'Sales': [15000, 18000, 17500, 19000]
    })
    st.dataframe(example_df)
    
    st.info("Your CSV should have:\n- A date/month column (e.g., 'Date', 'Month')\n- A sales column with numeric values (e.g., 'Sales', 'Revenue')")