# sentimentAnalysisTool
 Tool for analyzing twitter data. Includes an auto build neural net classifier and the 
 ability to create one's own classifier based on preclassified input data.
 Auto scrapes Tweets and auto gathers users. Comes prebuilt with a docker postgres server managed by pgadmin
 Includes graphical code to analyze and categorize data
 
 **Instructions for Use:**
 1. clone project
 2. Run the main.py and follow the directions

**Advanced Usage:**

**Docker:**
Docker-compose file has params for changing any necessary usernames or passwords in the enviornment variables.
The container may be on a different network. Use docker container inspect to find the ipv4 and use that
when creating the connection on pg admin
DB name is chosen by user. Just be consistent if you decide to edit any of the db values in the main.py

**Building a Training Set:**
Currently, the training set is built on the corpus set created by Niek Sanders’ Corpus. Currently website link is broken 
so use this personal repo link:
https://github.com/karanluthra/twitter-sentiment-training

This will build a set with about 5000 multi lingual classified tweets

*If you want to use a custom set:*
Place classified data in a csv with the same indexing as corpus. If the text is given just add that as a column 
and see the customized method in training_set.py. This should build a training set with 
the custom values, but its imperative if you don't have any id values to leave the 3rd column blank and put 
text in the fourth column


 