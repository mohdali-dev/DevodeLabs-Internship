import streamlit as st
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier()
model.fit(X, y)

st.title("AI Flower Classifier")

sepal_length = st.slider("Sepal Length", 4.0, 8.0)
sepal_width = st.slider("Sepal Width", 2.0, 5.0)
petal_length = st.slider("Petal Length", 1.0, 7.0)
petal_width = st.slider("Petal Width", 0.1, 3.0)

prediction = model.predict([[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]])

st.write("Prediction:", iris.target_names[prediction][0])
