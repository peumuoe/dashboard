import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="카페 주문 시스템",
    page_icon="☕",
    layout="centered"
)

# 앱 제목 (요구사항 1)
st.title("☕ 카페 주문 시스템")
st.markdown("원하시는 음료를 선택하고 주문해주세요.")

# 주문자 정보 섹션
st.subheader("주문자 정보")

# 주문자 이름 입력 (요구사항 2)
customer_name = st.text_input("이름을 입력해주세요")

# 음료 선택 섹션
st.subheader("음료 선택")

# 음료 가격 정보 (도전 과제)
drink_prices = {
    "아메리카노": 4500,
    "카페라떼": 5000,
    "카푸치노": 5500,
    "녹차": 4000,
    "바닐라 라떼": 5800,
    "카라멜 마키아또": 6000
}

# 음료 선택 (요구사항 3)
drink = st.selectbox(
    "음료를 선택해주세요",
    list(drink_prices.keys())
)

# 음료 크기 선택 (요구사항 4)
size = st.radio(
    "크기를 선택해주세요",
    ["Small", "Medium", "Large"],
    horizontal=True
)

# 크기별 추가 가격 (도전 과제)
size_prices = {
    "Small": 0,
    "Medium": 500,
    "Large": 1000
}

# 옵션 선택 섹션
st.subheader("옵션 선택")

# 옵션 체크박스 (요구사항 5)
col1, col2 = st.columns(2)

with col1:
    extra_shot = st.checkbox("샷 추가 (+500원)")
    whipped_cream = st.checkbox("휘핑크림 추가 (+500원)")

with col2:
    ice = st.checkbox("얼음 추가 (무료)")
    takeout = st.checkbox("테이크아웃")

# 수량 선택 (요구사항 6) - ✅ 슬라이더 값 설정
st.subheader("수량 선택")
quantity = st.slider("수량을 선택해주세요", min_value=1, max_value=10, value=1)  # ✅ 최소 1, 최대 10

# 주문 버튼 (요구사항 7)
st.markdown("---")
if st.button("주문하기"):
    # 주문 정보가 있는지 확인
    if not customer_name:
        st.error("이름을 입력해주세요!")
    else:
        # 총 가격 계산 (도전 과제)
        base_price = drink_prices[drink]
        size_extra = size_prices[size]
        option_price = 0
        
        if extra_shot:
            option_price += 500
        if whipped_cream:
            option_price += 500
            
        unit_price = base_price + size_extra + option_price
        total_price = unit_price * quantity
        
        # 주문 정보 표시
        st.success("주문이 완료되었습니다!")
        
        # 주문 내역 요약 표시
        st.subheader("📝 주문 내역")
        
        # 주문 정보 테이블 생성
        order_info = {
            "항목": ["주문자", "음료", "크기", "옵션", "수량", "단가", "총 금액"],
            "내용": [
                customer_name,
                drink,
                size,
                ", ".join([opt for opt, selected in {
                    "샷 추가": extra_shot,
                    "휘핑크림 추가": whipped_cream,
                    "얼음 추가": ice,
                    "테이크아웃": takeout
                }.items() if selected]) or "없음",
                quantity,
                f"{unit_price:,}원",
                f"{total_price:,}원"
            ]
        }
        
        # 테이블 표시
        st.table(order_info)
