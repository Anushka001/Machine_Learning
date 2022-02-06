Problem statement;

Suppose there is a famous mall, and you are a experienced data scientist. The mall wants to get insights about their customer, and the mall has data about their customers like purchasing behaviour and other aspects. As a data scientist, you have to build a system that can cluster the customers into different groups. For example, one group can have all the repeating customers, another one can have customers who do not shop that often from the mall. These culsters will help the mall owner to make better business decisions, and build better marketing strategies.

Work flow:

-First of all we will gather the data, so that we can train our ML model
- Next we will process this data, as we cannot feed this data directly to our model, we will select some features. This will be done in data preprocessing.
- Now we will analyse the data, where we will see what are the features of this data, and which ones are important.
- After that we will choose the optimum number of clusters. We need to tell the ML model the number of clusters, which we will find using a method called "within cluster sum of squares." This WCSS value will tell us the correct no of clusters suitable for the dataset.
- Now we will feed this data to the K Means clustering algorithm, which will group the data depending on their similarities.
-Finally we will visualize these clusters, by putting the predictions into plots.  
