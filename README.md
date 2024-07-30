Overview
This project performs sentiment analysis on tweets related to the Pfizer vaccine. The data is sourced from Kaggle and analyzed using a pre-trained machine learning model. The application classifies tweets into positive, negative, and neutral categories and provides an interactive web interface for real-time analysis. The application is built with Python and utilizes several libraries for data processing, model training, and visualization.
Additionally, a Jupyter Notebook (SentimentAnalysis.ipynb) showcases data preprocessing, word clouds, and various visualizations such as count plots and pie charts.

Features
- Sentiment classification of tweets about the Pfizer vaccine (positive, negative, neutral)
- Visualization of sentiment distribution
- Interactive web interface for live sentiment analysis
- Comprehensive data analysis including preprocessing, word clouds, and visualizations
- Logistic regression model with hyperparameter tuning for improved performance

Files
- app.py: Main application script to run the Streamlit web interface.
- SentimentAnalysis.ipynb: Jupyter Notebook showcasing data preprocessing, word clouds, and various visualizations, including details on logistic regression and hyperparameter tuning.
- model.pkl: Serialized logistic regression model for sentiment analysis.
- vectorizer.pkl: Serialized CountVectorizer used for feature extraction.
- requirements.txt: List of dependencies required to run the project.
