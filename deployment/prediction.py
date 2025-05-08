import streamlit as st
import pandas as pd
import joblib

# Model Loading
model = joblib.load("best_rfc_model.pkl")

def run():
    st.title('Prediksi Pelanggan Churn atau Tidak')
    st.header('Form Pengisian Data' )
    with st.form('form_data'):
        gender = st.selectbox('Gender: ', ('Male', 'Female'), index=0)
        senior = st.selectbox('Senior Citizen: ', (0, 1), index=0, help='0 menandakan bukan Senior Citizen, 1 menandakan Senior Citizen')
        partner = st.selectbox('Partner: ', ('No', 'Yes'), index=0)
        dependent = st.selectbox('Dependents: ', ('No', 'Yes'), index=0)
        tenure = st.number_input('Lama tenure: ', min_value=0, value=0)
        phoneservice = st.selectbox('Phone Service: ', ('No', 'Yes'), index=1)
        multiline = st.selectbox('Multiple Lines: ', ('No', 'No phone service', 'Yes'), index=0)
        inetserv = st.selectbox('Internet Service: ', ('DSL', 'Fiber optic', 'No'), index=2)
        onlinesecurity = st.selectbox('Online Security: ', ('No', 'No internet service', 'Yes'), index=0)
        onlinebackup = st.selectbox('Online Backup: ', ('No', 'No internet service', 'Yes'), index=0)
        deviceprotection = st.selectbox('Device Protection: ', ('No', 'No internet service', 'Yes'), index=0)
        techsupp = st.selectbox('Tech Support: ', ('No', 'No internet service', 'Yes'), index=0)
        streamtv = st.selectbox('Streaming TV: ', ('No', 'No internet service', 'Yes'), index=0)
        streammov = st.selectbox('Streaming Movie: ', ('No', 'No internet service', 'Yes'), index=0)
        contract = st.selectbox('Contract: ', ('Month-to-month', 'One year', 'Two year'), index=0)
        paperbill = st.selectbox('Paperless Billing: ', ('No', 'Yes'), index=0)
        paymethod = st.selectbox('Payment Method: ', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)',
       'Credit card (automatic)'), index=0)
        monthlycharges = st.number_input('Monthly Charges: ', min_value=18.25)
        totalcharges = tenure * monthlycharges
        totalcharges_display = st.text_input('Total Charges:', value=totalcharges, disabled=True)

        submit = st.form_submit_button('Predict!')
    st.write('---')
    st.subheader('Data yang Telah Dimasukkan')
    df = pd.DataFrame([
        {
            "gender": gender,
            "SeniorCitizen": senior,
            "Partner": partner,
            "Dependents": dependent,
            "tenure": tenure,
            "PhoneService": phoneservice,
            "MultipleLines": multiline,
            "InternetService": inetserv,
            "OnlineSecurity": onlinesecurity,
            "OnlineBackup": onlinebackup,
            "DeviceProtection": deviceprotection,
            "TechSupport": techsupp,
            "StreamingTV": streamtv,
            "StreamingMovies": streammov,
            "Contract": contract,
            "PaperlessBilling": paperbill,
            "PaymentMethod": paymethod,
            "MonthlyCharges": monthlycharges,
            "TotalCharges": totalcharges
        }
    ])

    st.dataframe(df)

    if submit:
        predictions = model.predict(df)
        if predictions == 1:
            st.error("⚠️ Customer akan **CHURN**!")
        else:
            st.success("✅ Customer **TIDAK** akan churn.")

if __name__== '__main__':
    run()