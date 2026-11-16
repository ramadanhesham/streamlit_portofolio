import streamlit as st
from PIL import Image

# 1. إعدادات الصفحة (يجب أن تكون أول سطر)
st.set_page_config(page_title="Ramadan Hesham | Portfolio", page_icon="👨‍💻", layout="wide", initial_sidebar_state="expanded")

# 2. إضافة لمسة تصميم مخصصة (Custom CSS)
st.markdown("""
<style>
    .main-header { font-size: 2.8rem; font-weight: 800; color: #1E3A8A; margin-bottom: 0px; }
    .sub-header { font-size: 1.4rem; font-weight: 500; color: #3B82F6; margin-top: 0px; }
    .bio-text { font-size: 1.1rem; line-height: 1.7; color: #4B5563; }
    div[data-testid="stExpander"] { border-radius: 10px; border: 1px solid #E5E7EB; }
</style>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.header("طرق التواصل 📬")
    st.markdown("[🔗 **LinkedIn Profile**](https://linkedin.com/in/ramadanhesham)")
    st.markdown("[🌳 **Linktree (Cookizz)**](https://linktr.ee/Cookizzz)")
    st.markdown("📧 **ramadanh1690@gmail.com**")
    st.markdown("📍 **Alexandria, Egypt**")
    
    st.divider()
    
    # تفعيل زر تحميل الـ CV الحقيقي
    st.info("💡 يمكنك تحميل سيرتي الذاتية من هنا")
    try:
        with open("Ramadan_Hesham_CV.pdf", "rb") as file:
            st.download_button(
                label="📄 تحميل السيرة الذاتية (CV)",
                data=file,
                file_name="Ramadan_Hesham_CV.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("ملف السيرة الذاتية غير موجود. تأكد من رفعه باسم Ramadan_Hesham_CV.pdf")

# 4. القسم الرئيسي (Hero Section)
col_text, col_img = st.columns([2.5, 1], gap="large")

with col_text:
    st.markdown('<p class="main-header">Ramadan Hesham</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Data Science Student | Microsoft Data Engineer Trainee | Content Creator</p>', unsafe_allow_html=True)
    st.markdown('<p class="bio-text">أجمع بين التفكير التحليلي في هندسة البيانات وعلومها، وبين مهارات التواصل وصناعة المحتوى التقني. أهدف إلى تحويل البيانات المعقدة إلى حلول مؤتمتة وقرارات ذكية لدعم الأعمال وصناعة تأثير حقيقي.</p>', unsafe_allow_html=True)

with col_img:
    # تفعيل الصورة الشخصية
    try:
        img = Image.open("profile.jpg")
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.warning("الصورة الشخصية غير موجودة. تأكد من رفعها باسم profile.jpg")

st.divider()

# 5. تنظيم المحتوى باستخدام الـ Tabs (علامات التبويب)
tab1, tab2, tab3 = st.tabs(["💼 الخبرات المهنية", "🛠️ المهارات التقنية", "🎓 التعليم"])

# --- التبويب الأول: الخبرات ---
with tab1:
    st.subheader("مسيرتي المهنية والمشاريع")
    
    with st.expander("🎥 Content Creator @ Ghawy AI (Aug 2026 - Present)", expanded=True):
        st.write("""
        - إعداد وإنتاج محتوى مرئي قصير لتبسيط مفاهيم الذكاء الاصطناعي وتعلم الآلة.
        - التعاون مع فرق التسويق لبناء استراتيجية المحتوى وزيادة تفاعل المجتمع.
        """)
        
    with st.expander("☁️ Microsoft Data Engineering Trainee @ DEPI (Jul 2026 - Present)"):
        st.write("""
        - التدريب المتعمق على هندسة البيانات الحديثة.
        - تطبيق عملي على تقنيات مثل **Azure Data Services، SQL، Data Warehousing، و ETL Processes**.
        """)

    with st.expander("🚀 Co-Founder & Content Creator @ Cookizz (2024 - Present)"):
        st.write("""
        - المشاركة في تأسيس قناة تعليمية لتقديم محتوى تقني ومهاري للشباب المصري.
        - إدارة التخطيط، كتابة السكريبتات، الإنتاج، واستراتيجيات التسويق الرقمي.
        """)

    with st.expander("📢 Vice Head of Media & Marketing @ Project Engine (2025 - 2026)"):
        st.write("""
        - إدارة الحملات الرقمية للفعاليات التقنية الكبرى مثل حدث CTRL A.
        - الإشراف على فرق صناعة المحتوى والتصميم لضمان وصول رسالة تقنية مبسطة للطلاب.
        """)

# --- التبويب الثاني: المهارات ---
with tab2:
    st.subheader("الأدوات والتقنيات")
    
    col_s1, col_s2, col_s3 = st.columns(3)
    
    with col_s1:
        st.success("💻 البرمجة وقواعد البيانات")
        st.write("- Python\n- SQL\n- Java\n- C++\n- R")
        
    with col_s2:
        st.info("☁️ هندسة البيانات (Data Engineering)")
        st.write("- Microsoft Azure\n- AWS (Cloud Foundations)\n- Data Warehousing\n- ETL & Data Pipelines")
        
    with col_s3:
        st.warning("🎬 تحليل البيانات وصناعة المحتوى")
        st.write("- Pandas, NumPy, Scikit-Learn\n- Power BI & Data Viz\n- Video Production & Editing\n- Scriptwriting & Storytelling")

# --- التبويب الثالث: التعليم ---
with tab3:
    st.subheader("الخلفية الأكاديمية")
    
    st.markdown("""
    **🎓 B.Sc. in Data Science** | *Alexandria University (2024 - 2028)*
    - **أبرز المقررات:** Data Structures, Database Systems (SQL), Big Data Analytics, Machine Learning, Advanced Calculus.
    - **الأنشطة:** عضو في ECPC FCDS، GDG On-Campus، و HackerRank.
    
    ---
    
    **🔬 STEM High School Diploma** | *STEM School Kafr El-Sheikh (2021 - 2024)*
    - نظام دراسي مكثف يعتمد على البحث العلمي، التفكير النقدي، وإنجاز مشاريع تخرج (Capstones) متعددة التخصصات.
    """)
