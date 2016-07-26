#Freeberg
Freeberg is a webapp that serves to provide users with live stock information at the tip of their fingers. The webapp aims to provide neat graphical comparisons between traded stocks on the stock market and allow the user to track stocks they have in their portfolio.


#Project Ideation 

##User stories
As business students, we want to be able to analyze live data and produce relevant analytics for the many finance projects that we do, and especially - for free.

##Definition of the Problem
While the financial industry has many applications which do financial analytics (e.g. Bloomberg), they are extremely costly and unaffordable for students such as us. The problem occurs when stocks have to be compared between one another and shown in a graphical format. Extracting data from Yahoo Finance individually and across multiple stocks becomes a tedious process as one has to manually extract the data for each stock . 

With these problems in mind, Freeberg aims to resolve these issues by allowing the user to extract this data efficiently and use for the relevant analysis of publicly traded stocks.

##Proposed Features for Minimum Viable Product
* Live Stock Tracker that is able to extract Live data from the relevant websites and parse historical prices into graphical formats - easy access to financial information for user
* Comparison of historical data in graphical format, providing visuals to allow users to understand compare companies immediately

#Proposed Level of Achievement
We are currently aiming for the `Project: Gemini` achievement. We plan to fulfill the following requirements in order meet this achievement:

* Log in at least 130 hours each
* Use Django framework for our webapp
* Extract Live Data through API
* Application-specific feature extensions - Exporting Graphical Data
* Enable downloading of data. 

Optional Features:
* User saved stock list

#Project Achievement/ Deliverables
As business students with relatively less exposure to frameworks and coding, we spent a lot of time learning about relevant modules and their implementation processes. We used python 3.5.1 and Django 1.9 to build our webapp, Freeberg. We have finished the stocktracker and comparison function which allow users to retrieve and compare up-to-date financial information for countries on the Straits Times Index.

##4 additional extension milestones completed 
1.	Application specific: Used Django framework to create webapp 
2.	Application specifc: Used Graphing tools to visualise data
3.	Live Stock updates: Used of ystockquote to pull up-to-date information from Yahoo Finance page
4.	Downloading: Enabled downloading of graphs and company information 

##Future Release 
In the future, we seek to implement a personalisation page for the user to keep track of their own stocks. It is regretfully not done in this project due to the lack of time. 

#User Experience 
1. Index  to introduce our services to people with links to the different webapp.
2. Search function on the navigation bar to allow users to quickly search for the stocks
3. Webpage that have all the stocks divided into different industries to allow users to view the stocks via industries
4. Graphical tools that enable users to download and use the information
5. Graphical tools to visualise comparison of the companies financial information to the users

##Cognitive walkthrough
We focused on how easy it is for new users to accomplish tasks with the system.
New users who want to access the individual stock information can: 
1. Click on the stocktracker page
2. Choose their choice of stock to view
3. Enjoy the analytical features of Freeberg

New Users who want to compare different companies' stock information  can:  
1. Click on comparison page 
2. Select 1st stock 
3. Select 2nd stock
4. Enjoy the analytical features of Freeberg

#Appendix
To view the webapp, please install packages: 
Python v3.5.1/ django v1.9 / Jinja2 / MarkupSafe / PyYAML / bokeh v 0.11.1 / django / djangorestframework / numpy / pandas / pip / python-dateutil / pytz / requests / setuptools /  six / tornado / ystockquote 
