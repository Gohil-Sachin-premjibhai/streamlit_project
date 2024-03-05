import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


st.title("ml project")
st.header("diamond price prediction")
st.subheader("implementation of random forest algoritham")
st.text("random forest bagging technique") 

st.markdown("# hi")         # markdown
st.markdown("## hi")
st.markdown("### hi")
st.markdown("#### hi")
st.markdown("##### hi")
st.markdown("hi")

st.success("success!")
st.info("information!")
st.warning("warning!")
st.error("error!")

# exp = ZeroDivisionError("division not possible with 0")
st.exception(ZeroDivisionError("division not possible with 0"))
st.help(ZeroDivisionError)

st.write("range(1,10)")
st.write(range(1,10))                                               # write
st.write("1+2+3")
st.write(1+2+3)

st.code('x=10 \n'
        'for i in range(x): \n'                                # code
        '\tprint(i)')


st.checkbox("Male")
st.checkbox("Female")        # checkbox


if(st.checkbox("Adult")):
    st.write("you're an adult!")             # checkbox with validation


radioButton=st.radio("select: ", ("male","female","other"))


if(radioButton=="male"):
    st.write("you're male")
elif(radioButton=="female"):                  # redio button
    st.write("you're female")
elif(radioButton=="other"):
    st.write("you're other person")



st.subheader("select box")                                  # selectbox
selectBox=st.selectbox("Data Science: ",["Data Analsis","web Scraping","Machine Learning","Deep Learning",
                               "Natural Language processing", "Computer vision", "image Processing"])

st.write("you've selected: ",selectBox)


st.subheader("mutliselect Box")       # multiselectbox
multiselectbox=st.multiselect("Data Science: ",["Data Analsis","web Scraping","Machine Learning","Deep Learning",
                               "Natural Language processing", "Computer vision", "image Processing"])
st.write("you've selected: ",len(multiselectbox),multiselectbox)


st.subheader("Button")  
# st.button("click me")                      # Button
if (st.button("click me")):
    st.write("thank for click me")

st.subheader("slider")                                # slider
level=st.slider("select the level",1,100,step=1)
st.write("level:",level)


st.subheader("Text Input")
user_name=st.text_input("user_name:")
user_password=st.text_input("user_password:", type ="password")




st.subheader("Text Area")
textArea=st.text_area("write something interesting about yourself in 500 words", height=200)

st.subheader("input number")
st.number_input("select your age",18,100)

st.subheader("input Date")
st.date_input("Date")

st.subheader("input Time")
st.time_input("Time")




st.subheader("Loading files")

upload_file =st.file_uploader("upload the csv file: ", type=['csv','xlsx'])
if upload_file:
    st.subheader("loading the csv file")
    df=pd.read_csv(upload_file.name)
    # st.table(df.head(10))
    st.dataframe(df.head(10))

# st.table(df.head())

# if df is not None:
#     st.dataframe(df)
    

st.subheader("Dealing with images")
upload_image=st.file_uploader("upload image file", type=['png','jpeg','jpg'])
if upload_image:
    st.image(upload_image)


st.subheader("Dealing with videos")
video_file=st.file_uploader("upload the video file : " , type = ['mkv', 'mp4'])
if video_file:
    st.video(video_file,start_time= 0)


st.subheader("Dealing with Audio")
audio_file=st.file_uploader("upload the audio file : " , type = ['mp3', 'wav'])
if audio_file:
    st.audio(audio_file.read())



df = sns.load_dataset('tips')

# Alter Scatter Plot
st.header("1. Altair Scatter Plot")
chart_data = pd.DataFrame(np.random.randn(500,5),columns= ["a","b","c","d","e"])
chart = alt.Chart(chart_data).mark_circle().encode(x="a",y="b", size="c",tooltip=["a","b","c","d","e"])
st.altair_chart(chart)

st.header("2. Interactive Charts")

st.subheader("2.1 Line Chart")
df = pd.read_csv("lang_data.csv")
lang_list = df.columns.to_list()
lang_choices = st.multiselect("Choose Your Language",lang_list)
new_df = df[lang_choices]
st.line_chart(new_df)

st.subheader("2.2 Area Chart")
st.area_chart(new_df)


st.header("3. Data Visualization with Plotly")
st.subheader("3.1 Displaying the dataset")
df = sns.load_dataset("tips")
st.dataframe(df.head(10))

st.subheader("3.2 Pie Chart")
fig = px.pie(df,values="total_bill", names="day",color_discrete_sequence=px.colors.sequential.Aggrnyl)
st.plotly_chart(fig)

st.subheader("3.3 Pie Chart with Multiple Parameters")
fig = px.pie(df,values="total_bill", names="day",opacity=.7,color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.subheader("3.4 Histogram")
x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)

hist_data = [x1,x2,x3]
group_labels = ["Group-1","Group-2","Group-3"]
fig = ff.create_distplot(hist_data,group_labels,bin_size=[.1,.25,.5])
st.plotly_chart(fig)




df = sns.load_dataset("iris")

st.header("1. Charts with Random Numbers")

chart_data = pd.DataFrame(np.random.randn(20,3),columns=["Col-1","Col-2","Col-3"])
st.subheader("1.1 Line Chart")
st.line_chart(chart_data)

area_chart = pd.DataFrame(np.random.randn(20,3),columns=["Col-1","Col-2","Col-3"])
st.subheader("1.2 Area Chart")
st.area_chart(area_chart)

bar_chart = pd.DataFrame(np.random.randn(20,3),columns=["Col-1","Col-2","Col-3"])
st.subheader("1.3 Bar Chart")
st.bar_chart(bar_chart)

st.header("2. Data Visualization with Matplotlib and Seaborn")

st.subheader("2.1 Loading the dataframe")
st.dataframe(df)

st.subheader("2.2 Bar Plot with Matplotlib")
fig = plt.figure(figsize=(15,8))
df["species"].value_counts().plot(kind='bar')
st.pyplot(fig)

# st.bar_chart(df["species"].value_counts())

st.subheader("2.2 Distribution Plot with Seaborn")
fig = plt.figure(figsize=(15,8))
sns.distplot(df["sepal_length"])
st.pyplot(fig)

st.header("3. Multiple Graphs")

# st.subheader("3.1 Distribution Plot with Seaborn")
col1,col2 = st.columns(2)
with col1:
    col1.header = "KDE = False"
    col1.write("KDE = False")
    fig1 = plt.figure(figsize=(8,8))
    sns.distplot(df["sepal_length"], kde=False)
    st.pyplot(fig1)
with col2:
    col2.header = "HIST = False"
    col2.write("HIST = False")
    fig2 = plt.figure(figsize=(8,8))
    sns.distplot(df["sepal_length"], hist=False)
    st.pyplot(fig2)

st.header("4. Changing the Style")
col1,col2 = st.columns(2)
with col1:
    fig1 = plt.figure(figsize=(8,8))
    sns.set_style("darkgrid")
    sns.set_context("notebook")
    sns.distplot(df["sepal_length"], hist=False)
    st.pyplot(fig1)
with col2:
    fig2 = plt.figure(figsize=(8,8))
    sns.set_theme(context="poster",style="darkgrid")
    sns.distplot(df["sepal_length"], hist=False)
    st.pyplot(fig2)

st.header("5. Exploring Different Graphs")

st.subheader("5.1 Scatter-Plot")
fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader("5.2 Count-Plot")
fig,ax = plt.subplots(figsize=(15,8))
sns.countplot(data=df,x="species")
st.pyplot(fig)

st.subheader("5.3 Box-Plot")
fig,ax = plt.subplots(figsize=(15,8))
sns.boxplot(data=df,x="species",y="sepal_length")
st.pyplot(fig)

st.subheader("5.4 Violin Plot")
fig,ax = plt.subplots(figsize=(15,8))
sns.violinplot(data=df,x="species",y="sepal_length")
st.pyplot(fig)
