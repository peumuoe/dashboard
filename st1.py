import streamlit as st

# 페이지 설정 (아이콘과 제목 설정)
st.set_page_config(
    page_title="내 소개",
    page_icon="👋",
    layout="wide"
)

# CSS를 사용하여 배경색과 스타일 변경 (도전 과제)
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
    }
    .title {
        color: #1E88E5;
        text-align: center;
    }
    .header {
        color: #0277BD;
    }
    .highlight {
        background-color: #E3F2FD;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 앱 제목 (요구사항 1)
st.markdown("<h1 class='title'>✨ 내 소개 ✨</h1>", unsafe_allow_html=True)

# 프로필 정보를 2개 컬럼으로 표시
col1, col2 = st.columns([1, 2])

with col1:
    # 프로필 이미지 (이모지 사용 - 도전 과제)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("## 🏋️‍♂️")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # 기본 정보 표시 (요구사항 2)
    st.markdown("<h2 class='header'>기본 정보</h2>", unsafe_allow_html=True)
    st.markdown("<div class='highlight'>", unsafe_allow_html=True)
    st.markdown("**이름**: 주기쁨")
    st.markdown("**전공**: HRD (인적자원개발)")
    st.markdown("**거주지**: 인천")
    st.markdown("</div>", unsafe_allow_html=True)

# 취미 섹션 (요구사항 3)
st.markdown("<h2 class='header'>어떤 프로젝트 혹은 도메인에 관심있는지?</h2>", unsafe_allow_html=True)
st.markdown("<div class='highlight'>", unsafe_allow_html=True)
st.markdown("""
* 🏆 스포츠 데이터 분석  
* 📊 경기력 및 훈련 데이터 활용  
* 📈 스포츠 산업에서 데이터 기반 의사결정  
""")
st.markdown("</div>", unsafe_allow_html=True)

# 자기소개 섹션
st.markdown("<h2 class='header'>자기소개</h2>", unsafe_allow_html=True)
st.markdown("<div class='highlight'>", unsafe_allow_html=True)
st.write("""
안녕하세요! 저는 주기쁨이고, 스포츠와 데이터 분석을 접목하는 것에 관심이 많습니다.  
HRD(Human Resource Development) 분야에서 일하고 있지만, 스포츠 데이터 분석을 통해  
선수들의 경기력 향상, 훈련 최적화, 스포츠 산업에서의 데이터 활용 방안을 연구하고 싶습니다.  
데이터 기반의 스포츠 혁신을 목표로 다양한 머신러닝 및 데이터 분석 기법을 배우고 있습니다.  
""")
st.markdown("</div>", unsafe_allow_html=True)

# 방문자 인사말 섹션 (요구사항 4, 5)
st.markdown("<h2 class='header'>방명록</h2>", unsafe_allow_html=True)
greeting = st.text_input("인사말을 남겨주세요 👋")

if greeting:
    st.markdown("<div class='highlight' style='background-color: #E8F5E9;'>", unsafe_allow_html=True)
    st.success(f"감사합니다, {greeting}! 방문해주셔서 기쁩니다. 😊")
    st.markdown("</div>", unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 개인 프로젝트</p>", unsafe_allow_html=True)
