import streamlit as st 

name = st.text_input('이름을 입력하세요')
if name:
    st.write(f'안녕하세요, {name}님!')

number = st.number_input('숫자를 입력하세요', min_value=0, max_value=100, value=50) 

slider_val = st.slider('슬라이더', min_value=0, max_value=100, value=50)

checkbox_val = st.checkbox('동의합니다') 

radio_val = st.radio('옵션을 선택하세요', ['옵션 1', '옵션 2', '옵션 3'])

selectbox_val = st.selectbox('항목을 선택하세요', ['항목 1', '항목 2', '항목 3'])

multiselect_val = st.multiselect('여러 항목을 선택하세요', ['항목 1', '항목 2', '항목 3', '항목 4'])

date_val = st.date_input('날짜를 선택하세요') 

time_val = st.time_input('시간을 선택하세요')
if st.button('클릭하세요'):
    st.write('버튼이 클릭되었습니다!')
uploaded_file = st.file_uploader("파일을 업로드하세요", type=['csv', 'txt', 'xlsx'])
if uploaded_file is not None:
    # 파일 처리 코드
    st.write("파일이 업로드되었습니다!")