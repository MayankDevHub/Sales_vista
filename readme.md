# SalesVista 📊

**SalesVista** is an interactive machine learning web application for sales forecasting and trend analysis. Upload your historical sales data and predict future sales for the next 6 months with ease!

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Features

- **📁 CSV Upload**: Upload your own sales data in CSV format
- **📈 Data Visualization**: Interactive charts showing historical sales trends
- **🤖 ML Predictions**: Linear Regression model for accurate sales forecasting
- **📊 6-Month Forecast**: Predict sales for the upcoming 6 months
- **💾 Export Results**: Download predictions as CSV for further analysis
- **🎯 Model Accuracy**: View R² score to evaluate prediction reliability
- **🔧 Flexible Column Selection**: Choose your date and sales columns dynamically

## 🚀 Demo

![SalesVista Demo](https://via.placeholder.com/800x400?text=SalesVista+Demo+Screenshot)

*Upload your sales data → Analyze trends → Get predictions → Download results*

## 🛠️ Tech Stack

- **Python** - Core programming language
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **scikit-learn** - Machine learning model (Linear Regression)

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher installed
- pip (Python package manager)

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/salesvista.git
cd salesvista
```

2. **Create a virtual environment** (recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

pip install -r requirements.txt


## 🎯 Usage

1. **Run the application**

streamlit run app.py


2. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to the URL shown in the terminal

3. **Upload your CSV file**
   - Click on "Browse files" or drag & drop your CSV
   - Your CSV should have at least two columns: one for dates and one for sales values

4. **Select columns**
   - Choose which column contains your dates
   - Choose which column contains your sales data

5. **Analyze & Predict**
   - Click "Analyze & Predict" button
   - View historical trends, forecasts, and download results

## 📁 Project Structure

```
## 📁 Project Structure
```
salesvista/
│
├── app.py                  # Main Streamlit application
├── model.py                # Machine learning model implementation
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── data/                  # Sample data folder (optional)
    └── sales_data.csv     # Example CSV file
```
```

## 📊 CSV Format

Your CSV file should follow this format:

| Date       | Sales |
|------------|-------|
| 2023-01-01 | 15000 |
| 2023-02-01 | 18000 |
| 2023-03-01 | 17500 |
| 2023-04-01 | 19000 |

**Requirements:**
- At least one date/time column
- At least one numeric column for sales
- Minimum 6-10 data points for better predictions
- Dates in standard format (YYYY-MM-DD, MM/DD/YYYY, etc.)

## 🧪 Sample Data

You can create a sample CSV file with this data for testing:

```csv
Date,Sales
2023-01-01,15000
2023-02-01,18000
2023-03-01,17500
2023-04-01,19000
2023-05-01,21000
2023-06-01,20500
2023-07-01,22000
2023-08-01,23500
2023-09-01,24000
2023-10-01,25500
2023-11-01,27000
2023-12-01,28500
```

## 🔮 How It Works

1. **Data Upload**: User uploads CSV file with historical sales data
2. **Data Processing**: Pandas processes and validates the data
3. **Feature Engineering**: Creates time-based features for the model
4. **Model Training**: Linear Regression model learns from historical patterns
5. **Prediction**: Model forecasts sales for next 6 months
6. **Visualization**: Streamlit displays interactive charts and results

## 📈 Model Information

- **Algorithm**: Linear Regression
- **Features**: Time-based numerical encoding
- **Training**: Trained on user-uploaded historical data
- **Output**: 6-month sales forecast with R² accuracy score

## 🚧 Future Enhancements

- [ ] Add multiple ML models (ARIMA, Prophet, Random Forest)
- [ ] Implement seasonal decomposition
- [ ] Add confidence intervals for predictions
- [ ] Support for multiple file formats (Excel, JSON)
- [ ] User authentication and data storage
- [ ] Advanced visualizations (Plotly, interactive filters)
- [ ] Export reports in PDF format
- [ ] Compare multiple forecasting models

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [MayankDevHub](https://github.com/MayankDevHub)

- LinkedIn: https://www.linkedin.com/in/mayank-kumar-3a69932a8?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

- Email: mayankkumar5962@gmail.com

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Machine learning powered by [scikit-learn](https://scikit-learn.org/)
- Data processing with [Pandas](https://pandas.pydata.org/)

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub.

---

⭐ **If you find this project useful, please consider giving it a star!** ⭐