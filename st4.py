import streamlit as st
import pandas as pd
import json

# 페이지 설정
st.set_page_config(
    page_title="학생 성적 관리 대시보드",
    page_icon="📚",
    layout="wide"
)

# 앱 제목
st.title("📚 학생 성적 관리 대시보드")
st.markdown("학생들의 성적을 관리하고 분석하는 대시보드입니다.")

# 학생 데이터프레임 생성 (요구사항 1)
@st.cache_data
def create_student_data():
    data = {
        '학생 이름': ['김민준', '이서연', '박지호', '최수아', '정도윤', '한예은', '황현우', '송지은'],
        '학년': [1, 2, 3, 1, 2, 3, 2, 1],
        '국어': [85, 92, 78, 96, 88, 77, 82, 94],
        '영어': [92, 88, 76, 94, 85, 75, 79, 91],
        '수학': [78, 95, 65, 92, 90, 68, 85, 79],
        '과학': [90, 84, 72, 88, 95, 70, 78, 86]
    }
    
    # 데이터프레임 생성
    df = pd.DataFrame(data)
    
    # 총점과 평균 점수 계산 (요구사항 3)
    df['총점'] = df[['국어', '영어', '수학', '과학']].sum(axis=1)
    df['평균'] = df[['국어', '영어', '수학', '과학']].mean(axis=1)
    
    return df

# 데이터프레임 로드
df = create_student_data()

# 사이드바 - 검색 및 필터링 옵션 (도전 과제)
st.sidebar.header("🔍 검색 및 필터링")

# 학생 검색 기능 (도전 과제)
search_name = st.sidebar.text_input("🔎 학생 이름 검색")

# 과목 필터링 (도전 과제)
st.sidebar.subheader("📌 과목별 필터링")
selected_subject = st.sidebar.selectbox("과목 선택", ['국어', '영어', '수학', '과학'])

# 평균 기준 필터링 (도전 과제)
filter_option = st.sidebar.radio(
    "📊 필터링 기준",
    ["전체 학생", f"{selected_subject} 평균 이상", f"{selected_subject} 평균 이하"]
)

# 학년 필터링
selected_grade = st.sidebar.multiselect("🎓 학년 선택", [1, 2, 3], default=[1, 2, 3])

# 데이터 필터링 적용
filtered_df = df.copy()

# 학년 필터 적용
filtered_df = filtered_df[filtered_df['학년'].isin(selected_grade)]

# 이름 검색 필터 적용
if search_name:
    filtered_df = filtered_df[filtered_df['학생 이름'].str.contains(search_name, case=False)]

# 과목 평균 필터 적용
if filter_option != "전체 학생":
    subject_avg = df[selected_subject].mean()
    if "이상" in filter_option:
        filtered_df = filtered_df[filtered_df[selected_subject] >= subject_avg]
    else:
        filtered_df = filtered_df[filtered_df[selected_subject] < subject_avg]

# 메인 컨텐츠 탭 나누기 (요구사항 추가)
tab1, tab2 = st.tabs(["📋 학생 성적", "📊 데이터 분석"])

with tab1:
    # 기본 데이터프레임 표시 (요구사항 2)
    st.subheader("📋 학생 성적 데이터")
    
    # 정렬 옵션
    sort_options = st.radio(
        "🔽 정렬 기준",
        ["정렬 없음", "평균 높은 순", "평균 낮은 순"],
        horizontal=True
    )
    
    # 데이터 정렬 (요구사항 4)
    display_df = filtered_df.copy()
    if sort_options == "평균 높은 순":
        display_df = display_df.sort_values(by='평균', ascending=False)
    elif sort_options == "평균 낮은 순":
        display_df = display_df.sort_values(by='평균', ascending=True)
    
    # 데이터프레임 표시
    st.dataframe(display_df, use_container_width=True)

with tab2:
    # 메트릭 표시 (요구사항 5)
    st.subheader("📊 성적 분석")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📌 전체 평균 점수", f"{df['평균'].mean():.2f}점")
    
    with col2:
        st.metric("🏆 최고 평균 점수", f"{df['평균'].max():.2f}점")
    
    with col3:
        st.metric("🔻 최저 평균 점수", f"{df['평균'].min():.2f}점")
    
    # JSON 데이터 표시 (요구사항 6)
    st.subheader("📜 학생별 총점 데이터 (JSON 형식)")
    
    json_data = df[['학생 이름', '총점']].set_index("학생 이름").to_json(indent=4, force_ascii=False)
    st.code(json_data, language="json")
