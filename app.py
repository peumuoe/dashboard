import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="판매 데이터 시각화",
    page_icon="📊",
    layout="wide"
)

# 앱 제목
st.title("📊 판매 데이터 시각화")
st.markdown("Streamlit을 사용하여 판매 데이터를 시각화하는 대시보드입니다.")

# 데이터 생성 함수
@st.cache_data
def generate_sales_data():
    np.random.seed(42)
    months = [f"{i}월" for i in range(1, 13)]
    product_a = np.random.randint(50, 201, size=12)
    product_b = np.random.randint(50, 201, size=12)
    product_c = np.random.randint(50, 201, size=12)
    
    df = pd.DataFrame({
        '월': months,
        '상품A': product_a,
        '상품B': product_b,
        '상품C': product_c
    })
    
    return df

# 데이터 로드
sales_df = generate_sales_data()

# 데이터 표시
st.subheader("📋 판매 데이터")
st.dataframe(sales_df)

# 시각화
st.subheader("📊 판매량 그래프")
fig = px.line(sales_df, x="월", y=["상품A", "상품B", "상품C"], markers=True, title="월별 판매량 변화")
st.plotly_chart(fig)
