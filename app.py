import streamlit as st

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