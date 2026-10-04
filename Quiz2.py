import streamlit as st
st.write("x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x")
st.write("Welcome to Quiz2")
st.write("x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x")
st.sidebar('Rest the Quiz')
st.write("Q1. Who is the President of India?/n/n Options: A. Rahul Gandhi, B. Sonia Gandhi, C. Dropadi Murmu, D. Arvind Kejriwal")
Ans1 = st.text_input("Enter your choice for Q1")
st.write("Q2. Which is the Capital of India?/n/n Options: A. Lucknow, B. Gujrat, C. Himachal, D. New Delhi")
Ans2 = st.text_input("Enter your choice for Q2")
st.write("Q3. Name of the currency of India?/n/n Options: A. Rubel, B. Rupee, C. Dollar, D. Euro")
Ans3 = st.text_input("Enter your choice for Q3")
st.write("Q4. Which is the capital of the Haryana?/n/n Options: A. Faridabad, B. Jhajhar, C. Rohtak, D. Chandigarh")
Ans4 = st.text_input("Enter your choice for Q4")

score = 0

if not Ans1 or not Ans2 or not Ans3 or not Ans4:
    st.warning("Please answer all questions before submitting!")
else:
  if Ans1 == "c" or Ans1 == "C":
      st.snow()
      score+=5
  else:
      score-=2
      st.write("incorrect answer")
      st.balloons()
  if Ans2 == "d" or Ans2 == "D":
      st.snow()
      score+=5
  else:
      score-=2
      st.write("incorrect answer")
      st.balloons()
  if Ans3 == "b" or Ans3 == "B":
      st.snow()
      score+=5
  else:
      score-=2
      st.write("incorrect answer")
      st.balloons()
  if Ans4 == "d" or Ans4 == "D":
      st.snow()
      score+=5
  else:
      score-=2
      st.write("incorrect answer")
      st.balloons()
  
  st.write("Total score is", score)
if score>=10:
  st.write('Very Poor')
elif score>=20:
  st.write('Okay okay')
elif score>=30:
  st.write('Good')
else:
  st.write('Excellent')
  
    

