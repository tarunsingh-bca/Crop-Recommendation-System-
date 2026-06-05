# Crop Recommendation System

Welcome to the Crop Recommendation System repository. This project is dedicated to helping agricultural experts, researchers, and farmers make data-driven decisions about the best crops to grow based on various environmental and soil conditions.

## Project Overview

Agriculture involves many variables, and choosing the right crop can significantly impact yield and profitability. This system utilizes data analysis and machine learning techniques to recommend the most suitable crop, ensuring optimal resource utilization and minimizing risks associated with crop failure.

## Technologies and Libraries Used

This project is built using a combination of powerful tools and libraries:

- **Python**: Powers the data processing, analysis, and the core recommendation logic.
- **Pandas**: Used for data manipulation, preprocessing, and cleaning the CSV datasets.
- **Scikit-learn**: Powers the machine learning models that generate the accurate crop recommendations.
- **HTML5**: Used for structuring the web-based user interface.
- **CSS3**: Applied for styling and designing an intuitive, responsive user interface.

## Dataset Information

In this repository, we have included several CSV files that serve as the backbone for the analysis and recommendation logic:

- **clean_crop_advisory.csv**: Contains tailored advisory information and best practices for different crop types.
- **clean_data_core.csv**: Holds the primary environmental and historical data used for model training and core predictions.
- **clean_market_prices.csv**: Stores historical market pricing data to help evaluate the economic viability of recommended crops.
- **clean_soil_fertilizer.csv**: Provides critical details regarding soil composition and appropriate fertilizer requirements.

## How to Set Up and Run

To get this project running on your local machine, please follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/tarunsingh-bca/Crop-Recommendation-System-.git](https://github.com/tarunsingh-bca/Crop-Recommendation-System-.git)
   Install Dependencies:
Ensure you have Python installed, and install the required libraries listed in the requirements.txt file by opening your terminal and running:

Bash
pip install -r requirements.txt
Run the Application:

Bash
python app.py
Access the System:
Open your preferred web browser and navigate to http://127.0.0.1:5000 to begin interacting with the system.

How to Use the System
Once the application is running, you can input specific soil composition and environmental parameters through the web interface. The system will cross-reference these inputs with the uploaded CSV data to provide accurate crop recommendations and financial advisory.

Contributing
We welcome contributions to improve this crop recommendation system! If you have suggestions for new features, bug fixes, or dataset enhancements, feel free to fork this repository and submit a pull request.
