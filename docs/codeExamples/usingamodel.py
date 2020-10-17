from sklearn.feature_extraction import stop_words
import string

from sklearn.externals import joblib

stopwords = stop_words.ENGLISH_STOP_WORDS
def clean(doc): #doc is a string of text
    doc = doc.replace("</br>", " ") #This text contains a lot of <br/> tags.
    doc = "".join([char for char in doc if char not in string.punctuation and not char.isdigit()])
    doc = " ".join([token for token in doc.split() if token not in stopwords])
    #remove punctuation and numbers
    return doc


model_file = "mymodel.pkl"
pipeline = joblib.load(model_file)

print(pipeline["logisticregression"].classes_) 
#Remember: we originally setup relevant as 1 and non-relevant as 0.

mystring = "Every facet of Canadian life has been changed by the current pandemic, from how and where we live, to how we shop, eat and work. While not all changes have been for the better, COVID-19 could bring about some positive changes to Canada's economy."
print(pipeline.predict([mystring])) #prints only the prediction
print(pipeline.predict_proba([mystring])) #prints predictions with probabilities in the order: [not relevant, relevant]


