import streamlit as st

# 페이지 설정
st.set_page_config(page_title="기술 시간 아이디어 노트", layout="wide")

st.title("💡 기술 수업: 발명 아이디어 구상 노트")
st.info("생활 속의 불편함을 찾고, 이를 해결할 멋진 아이디어를 기록해보세요!")

# 사이드바: 학생 정보 입력
st.sidebar.header("학생 정보")
student_id = st.sidebar.text_input("학번 (예: 10101)")
student_name = st.sidebar.text_input("이름")

# 메인 화면: 아이디어 입력 레이아웃
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. 문제 발견")
    problem = st.text_area("일상생활에서 불편했던 점은 무엇인가요?", placeholder="예: 우산에서 떨어지는 빗물 때문에 바닥이 미끄러워요.")

    st.subheader("2. 기존 해결책")
    existing = st.text_area("지금은 이 문제를 어떻게 해결하고 있나요?", placeholder="예: 입구에 비닐 커버를 씌우거나 극세사 매트를 깔아요.")

with col2:
    st.subheader("3. 나의 아이디어")
    idea = st.text_area("당신만의 새로운 해결 방법은?", placeholder="예: 원심력을 이용해 1초 만에 물기를 털어주는 회전형 우산 털이개")
    
    improvement = st.select_slider(
        "기존 제품보다 얼마나 개선되었나요?",
        options=["조금 편리해짐", "보통", "매우 혁신적임"]
    )

# 결과 요약 및 저장
st.divider()

if st.button("내 아이디어 최종 확인"):
    if not student_id or not student_name:
        st.warning("사이드바에 학번과 이름을 입력해주세요!")
    else:
        summary = f"""
        ### [제출용 요약]
        - **작성자**: {student_id} {student_name}
        - **불편한 점**: {problem}
        - **아이디어**: {idea}
        - **혁신성**: {improvement}
        """
        st.markdown(summary)
        
        # 파일로 다운로드 기능
        report_text = f"학번: {student_id}\n이름: {student_name}\n문제: {problem}\n아이디어: {idea}\n개선도: {improvement}"
        st.download_button(
            label="텍스트 파일로 저장하기",
            data=report_text,
            file_name=f"{student_id}_{student_name}_아이디어.txt",
            mime="text/plain"
        )
