#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        Income = request.form.get("Income")
        Age = request.form.get("Age")
        Loan = request.form.get("Loan")
        print(Income, Age, Loan)
        Income = (float(Income) - 45133.79)/ 14426.48
        Age = (float(Age) - 34.86)/ 12.65
        Loan = (float(Loan) - 5591.68)/ 3174.97
        model = joblib.load("Default")
        pred = model.predict([[float(Income), float(Age), float(Loan)]])
        if pred[0] == 0:
            default = " (No default)"
        elif pred[0] == 1:
            default = " (Will default)"
        s = "The predicted default score is " + str(pred[0]) + str(default)
        return(render_template("index.html", result="The predicted default score is "))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




