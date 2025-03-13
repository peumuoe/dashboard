import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(
    page_title="판매 데이터 시각화",
    page_icon="📊",
    layout="wide"
)

# 앱 제목
st.title("📊 월별 판매 데이터 시각화")
st.markdown("다양한 차트를 통해 판매 데이터를 시각화하는 앱입니다.")

# 1. 데이터프레임 생성 (요구사항 1)
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

# 데이터 생성
sales_df = generate_sales_data()

# 사이드바 - 필터링 및 옵션
st.sidebar.header("데이터 필터 및 옵션")

# 제품 선택
selected_products = st.sidebar.multiselect(
    "시각화할 제품 선택",
    ["상품A", "상품B", "상품C"],
    default=["상품A", "상품B", "상품C"]
)

# 월 범위 선택
months_range = st.sidebar.slider(
    "월 범위 선택",
    1, 12, (1, 12),
    step=1
)

# 선택된 월 범위에 따라 데이터 필터링
filtered_df = sales_df.iloc[(months_range[0]-1):months_range[1]]

# 선택된 제품만 포함하는 데이터프레임 생성
filtered_products_df = filtered_df[['월'] + selected_products]

# 데이터 탭과 시각화 탭 생성
tab1, tab2 = st.tabs(["📋 데이터", "📊 시각화"])

with tab1:
    st.header("판매 데이터")
    st.dataframe(filtered_products_df, use_container_width=True)
    
    # 데이터 요약 정보
    st.subheader("데이터 요약")
    
    # 총 판매량 계산
    total_sales = {product: filtered_df[product].sum() for product in selected_products}

    # 총 판매량 표시
    col1, col2, col3 = st.columns(3)
    
    for i, (product, sales) in enumerate(total_sales.items()):
        if i == 0:
            col1.metric(f"{product} 총 판매량", f"{sales:,}개")
        elif i == 1:
            col2.metric(f"{product} 총 판매량", f"{sales:,}개")
        else:
            col3.metric(f"{product} 총 판매량", f"{sales:,}개")  # ✅ 실행할 코드 추가하여 오류 해결