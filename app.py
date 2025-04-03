import streamlit as st
import joblib
clf=joblib.load('loan.joblib')
st.title('LOAN APP RCE')
g=st.nunmber_input('Enter Gender 0:Male 1:Female')
m=st.number_input('Enter Martial status 0:No 1:Yes')
ai=st.number_input('Enter Applicant Income in thousand')
la=st.number_input('Enter Loan amount in thousands')
if st.button('PREDICT'):
    prediction=clf.predict([[g,m,ai,la]])
    if prediction=='Y':
        st.text('Loan is Approved')
    else:
        st.text('Loan is Rejected')
