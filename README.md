# TeleICU-System

Innovative Monitoring System for TeleICU Patients using Video Processing and Deep Learning


This project is built during Intel Unnati Industrial Internship 2024. The system aims to monitor the ICU patients in real time remotely.
A] Data Preparation- Data is being processed and labelled. The image file is converted into xml file inorder to get the information of the objects in the images.
 B] Image Agument- Images are agumented ,resize, recolored , reshape for improving data quality.

3] Model Building and Training: In the folder yolo_training the images which were processed are trained and optimized model has been built. Data visualization helps to visualize the patterns of the object in the images.	The bounding box created can be visualized and compared to the original image. The performance measure considered here are precision, recall, AUC curve, ROC curve, Confusion matrix. Initially the epochs considered for the model was 50 and till the end we had considered the epochs to be 100 and hence we reached to the optimal accuracy.

4] Optimization of Model
In this file we check the confidence rate and after a specific treshold is crossed. The value is passed for prediction.

5]The frontend file consists of an interactive page where we can on/off the webcam and monitor the patients
