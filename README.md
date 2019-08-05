# TwitterSentimentAnalysisTool (TSAT)
 A highly adaptable tool for analyzing twitter data. 
 Auto scrapes Tweets based on user keyword from the previous week and applies a naive bayes classifier to analyze sentiment. Comes prebuilt with a docker postgres server managed by pgadmin
 Includes graphical visuals to analyze and categorize data. 
 
Usage:
1. Clone the project 
2. Install docker and docker-compose (not listed in requirements.txt)
3. Install requirements.txt
4. In terminal navigate to the project and cd to Docker
5. sudo docker-compose up
6. Check localhost:5555 and sign in to postgres using 'user' and 'password' as email and password respectively
7. create a server with the login 'user' and 'password' and the network 172.18.0.1
8. Go to .env file and set environment variables (Assumes you created a twitter app)
9. Run main.py, classify tweets and view projections

**Important References:**
* https://arxiv.org/pdf/1811.07522.pdf
* https://jakevdp.github.io/PythonDataScienceHandbook/05.05-naive-bayes.html
* https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed
* https://www.sciencedirect.com/science/article/pii/S1877050919302789
* https://www.sciencedirect.com/science/article/pii/S2405844018332067
* https://arxiv.org/pdf/1509.02971.pdf
