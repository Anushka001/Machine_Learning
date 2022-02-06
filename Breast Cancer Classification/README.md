Breast Cancer Classification
There are two types of tumors: 
Benign tumor: these tumors do not metastasize. These are non-cancerous, non-invasive and slow growing tumors which are capsulated.
Malignant tumor: these tumors metastasize to other parts of the body. These are cancerous, non-capsulated and fast growing tumors.

if malignant tumor are not caused, they cause breast cancer.  
If the tumor is benign, there is nothing to worry. But in the latter, the patient needs to be given urgent treatment, like chemotherapy, radiation etc so as to remove the tumor.

So here our problem statement is to identify if the tumor is Benign or Malignant.

the dataset is prepared by fine needle aspiration.
fine needle aspiration is a type of biopsy procedure. In fine needle aspiration, a thin needle is inserted into an area of abnormal-appearing tissue or body fluid. As with other types of biopsies, the sample collected during fine needle aspiration can help make a diagnosis or rule out conditions such as cancer.

In the dataset, we are given info about the properties of cells like radius, symmetry, area, smoothness etc, and we have to determine if the tumor is malignant[0] or benign[1]

Work flow:
data collection
data preprocessing
train test split
train model using logistic regression (best for binary classification)
evaluate trained model using test data
feed new data to predict if the tumor is benign or malignant
