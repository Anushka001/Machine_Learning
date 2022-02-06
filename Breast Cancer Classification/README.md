Breast Cancer Classification:

There are two types of tumors: 
1. Benign tumor: These tumors do not metastasize. These are non-cancerous, non-invasive and slow growing tumors which are capsulated.

2. Malignant tumor: These tumors metastasize to other parts of the body. These are cancerous, non-capsulated and fast growing tumors.

If Malignant tumor are not cured, they cause breast cancer.  

If the tumor is Benign, there is nothing to worry. But if the tumor is Malignant, the patient needs to be given urgent treatment, like chemotherapy, radiation etc so as to remove the tumor.

So here our problem statement is to build a Machine Learning model which can predict if the tumor is Benign or Malignant.

The dataset we are using is prepared by Fine Needle aspiration.

Fine Needle aspiration is a type of biopsy procedure. In Fine Needle aspiration, a thin needle is inserted into an area of abnormal-appearing tissue or body fluid. As with other types of biopsies, the sample collected during fine needle aspiration can help make a diagnosis or rule out conditions such as cancer.

In the dataset, we are given information about the properties of cells like radius, symmetry, area, smoothness etc, and we have to determine if the tumor is malignant or benign.

Work flow:
- Data collection
- Data preprocessing
- Splitting the data into train test set
- Training the model using Logistic Regression (best for binary classification)
- Evaluating the trained model using test dataset
- Feeding new data to predict if the tumor is benign or malignant
