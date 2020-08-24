# Automatic-Answer-Grading

Given an answer to a question from selected set of questions, our aim is to evaluate it and give a qualitative score.
The subjective nature of an answer makes it difficult to grade it uniformly across many human graders. In addition, human graders tend to unknowingly grade an answer with their own biases towards the subject matter presented.
Manual grading has another major drawback, the time required to grade essays can be significantly high.

# Dataset

The dataset used is the Kaggle’s Automatic Essay Scoring dataset,can be downloaded from https://www.kaggle.com/c/asap-aes/data

# Testing

cd website

python manage.py migrate

python manage.py runserver

# Observations and Results 

The models were tested using kappa statistic which is intending to compare labelling by different human annotators, not a classifier versus a ground truth. The kappa score is a number between -1 and 1. Scores above .8 are generally considered good agreement,zero or lower means no agreement
For this project we have used an Algorithm in which we Combine all the topics into a single model and predicted the score using bi-directional LSTM.		
kappa score obtained is 0.74

# Future Work

An assumption has been made regarding that essays are not similar to each other but there should be a plagiarism check before passing it to the model for score.

# References

Mahana, Johns and Apte “Automatic Essay Grading with Machine Learning”
http://cs229.stanford.edu/proj2012/MahanaJohnsApte-AutomatedEssayGradingUsingMachineLearning.pdf
Attali, Yigal, and Jill Burstein. “Automated essay scoring with e-rater V. 2.” The Journal of Technology, Learning and Assessment 4.3 (2006). 
https://www.ets.org/Media/Research/pdf/RR-04-45.pdf


