import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy as np
import pickle
from PIL import Image
import altair as alt

pickled_model = pickle.load(open('modelfinal1.pkl', 'rb'))

st.title(':red[PCOS]')

st.subheader(':green[Age VS Share of Respondents]')

df = pd.DataFrame({
    'Age group': ['<19', '20-29', '30-44', '45-59', '60>'],
    'Percentage': [3.8, 16.81, 11.58, 1.44, 0.55]
})

chart = alt.Chart(df).mark_bar(color='#FFA07D').encode(
    x=alt.X('Age group', title='Age group'),
    y=alt.Y('Percentage', title='Percentage'),
    text=alt.Text('Percentage', format='.1f'),
    color=alt.Color('Age group',)
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
)

chart = chart.properties(
    width=alt.Step(40)  # adjust the width of the bars
)

st.header('')

st.altair_chart(chart, use_container_width=True)
st.title(":blue[Start your diagnosis]")
# Getting input data from user



fields = ['Age (yrs)', 'Weight (Kg)', 'BMI', 'Pulse rate(bpm)', 'Hb(g/dl)',
       'Cycle(R/I)', 'Cycle length(days)', 'Marraige Status (Yrs)',
       'Hip(inch)', 'Waist(inch)', 'AMH(ng/mL)', 'Vit D3 (ng/mL)',
       'Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)',
       'Hair loss(Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)', 'Follicle No. (L)',
       'Follicle No. (R)', 'Avg. F size (L) (mm)', 'Avg. F size (R) (mm)',
       'Endometrium (mm)']


# create an empty list to store input values
inputs = []

# take input for each field and append it to the inputs list
for field in fields:
    input_val = st.number_input(label=field)
    inputs.append(input_val)

# convert the inputs list to a 2D numpy array
inputs_arr = np.array(inputs).reshape(1, -1)

# display the inputs and the shape of the inputs array
a = st.button("Submit")
text = " "
if a:
    value = pickled_model.predict(inputs_arr)
    if value == 1:
        text = "you have probability of Polycystic Ovary Syndrome"
    else:
        text = "Your are not prone to Polycystic Ovary Syndrome"
    st.success("Diagnosis completed ✅")
    st.success(text)
    



