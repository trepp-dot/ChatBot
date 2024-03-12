import datetime

date = datetime.datetime.now().strftime("%Y-%m-%d")

initial_message = [{
  "role": "system",
  "content": "You are a chatbot on behalf of Eran Trepp personal website."
             "You should be polite and helpful, always ask further questions, and create a nice conversation."
             "write short answers up to 50 tokens, and use proper grammar unless asked you to do something else, "
             f"today's date is {date}"
             "To set up a meeting with Eran, please use email or phone or website."
             "Use the provided articles delimited by triple quotes to answer questions. "
             "If the answer cannot be found in the articles, write \"I am only authorized to answer questions related to Eran.\""
  },
  {
    "role": "user",
    "content": "\"\"\"\nname: Eran last name: Trepp Born and living in Israel phone number: +972-52-889-1884  \nemail:  trepp49@gmail.com \nliving in: Tel-Aviv \nYOB: 1986\n\n website: https://www.eran-trepp.com/\n\n\"\"\""
               "I’m a creative, agile data scientist with a unique business understanding and orientation. Offering experience in designing and deploying end-to-end data-driven solutions incorporating state-of-the-art models. "
               "Working with Python, PySpark, SQL, Deep & machine learning. I am looking for a data scientist position."
               "\n\nEXPERIENCE\n\n"
               "2022 - today:    DATA SCIENTIST at BEES Tel-Aviv.:\n•\tDeveloped algorithmic pipelines at a large scale in production\n•\tResearched and developed explainable RecSys for an e-commerce store\n•\tDefining, designing, and executing algorithmic solutions in time series forecasting, anomaly detection, and clustering models\n\n"
               "2015 - today:     INDEPENDENT BUSINESS CONSULTANT:\n•\tBuilding and validating models in different fields – Gathering data from various sources, preparing & validating it for analysis, and building complex models for pulling meaningful insights leading to acumen business decisions.  \n•\tConstructed business plans and manufactured market reviews for small businesses.\n\n\n"
               "2021 - 2022:     DATA SCIENTIST at AVO SHOPPING:\n•\tDeployed to production a recommendation engine, a customer retention system, and a route optimization technique using machine learning algorithms such as Regression, SVM, Random forest, Xgboost, KNN, and K-means.\n•\tLed data science analysis projects using ML - customer segmentation, sales forecast, market basket analysis, and more, providing oversight and actionable insights for all organization departments.\n\n\n"
               "2020 - 2021:     DATA SCIENTIST, Credit Dept. at MIMUN YASHIR.:\n•\tDeveloping models incorporating machine learning algorithms such as SVM, Xgboost, and more for predicting loan defaults.\n•\tLed the development of machine learning infrastructure, including designing a DB, creating ETL, and monitoring data quality.\n•\tDeployed machine learning models into production.\n\n\n"
               "2017 - 2020:     SENIOR FINANCIAL DATA ANALYST at MIMUN YASHIR:\n•\tProviding crucial business insights through developing data-driven models\n•\tDeveloping models for structured bonds and other types of securities\n\n\n2015 - 2017:     CO-FOUNDER & CTO at LOCALFRIEND:\n•\tFounded a TravelTech B2B startup providing a virtual concierge platform.\n•\tLeading the company's core technology and product development.\n•\tFundraising and financial planning"
               "\n\nEDUCATION\n\n"
               "2017 - 2019: MSc in Mathematical Finance, at Bar Ilan Universit\n"
               "2008 - 2011: BA in Economics and Business Management, at Tel Aviv University\nC"
               "ourses: Python for DS, G-stat | GCP Specialization, Coursera | Deep Learning, NYU\n\n"
               "SKILLS & MORE\n\nLanguages:  English – Fluent    |   Hebrew – native\n"
               "Models: both supervised and unsupervised for example Regression | SVM | Random forest | Xgboost | KNN | K-means | ARIMA | Exponential Smoothing (ETS) | DeepAR - DNN for time series forecasting | TFT - DNN for time series forecasting | XDeepFM - DNN for recommendation system and more\n"
               "Technology:  Python | PySpark | Hive | SQL | AWS | Azure | GCP |  Airflow  | and more\n"
               "Python DS Libraries:  Pandas | Numpy | Scikit-learn | Scipy | TensorFlow and more\n"
               "Military service:   3 years as a combat soldier and commander in the Egoz elite unit\n\"\"\""
  }
]

