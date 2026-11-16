import streamlit as st
from PIL import Image

# إعدادات الصفحة
st.set_page_config(page_title="Ramadan Hesham | Portfolio", page_icon="👨‍💻", layout="wide")

# القائمة الجانبية (Sidebar)
st.sidebar.title("طرق التواصل 📬")
st.sidebar.write("[LinkedIn](https://linkedin.com/in/ramadanhesham)")
st.sidebar.write("[Linktree (Cookizz)](https://linktr.ee/Cookizzz)")
st.sidebar.write("📧 ramadanh1690@gmail.com")
st.sidebar.write("📍 Alexandria, Egypt")

# القسم الرئيسي (Header)
st.title("Ramadan Hesham")
st.subheader("Data Science Student | Microsoft Data Engineer Trainee (DEPI) | Content Creator")
st.write("""
أجمع بين التفكير التحليلي في هندسة البيانات وعلومها، وبين مهارات التواصل وصناعة المحتوى التقني. 
أهدف إلى تحويل البيانات المعقدة إلى حلول مؤتمتة وقرارات ذكية لدعم الأعمال.
""")

st.divider()

# قسم الخبرات (Experience)
st.header("الخبرات المهنية 💼")
col1, col2 = st.columns(2)

with col1:
    st.write("### Content Creator @ Ghawy AI")
    st.write("إعداد وإنتاج محتوى مرئي قصير لتبسيط مفاهيم الذكاء الاصطناعي وتعلم الآلة.")
    
    st.write("### Microsoft Data Engineering Trainee @ DEPI")
    st.write("التدريب على هندسة البيانات الحديثة باستخدام تقنيات مثل Azure، وSQL، وData Pipelines.")

with col2:
    st.write("### Co-Founder & Content Creator @ Cookizz")
    st.write("إدارة التخطيط وكتابة السكريبتات وإنتاج الفيديوهات التقنية للشباب.")
    
    st.write("### Vice Head of Media & Marketing @ Project Engine")
    st.write("إدارة الحملات الرقمية للفعاليات التقنية الكبرى مثل حدث CTRL A.")

st.divider()

# قسم المهارات (Skills)
st.header("المهارات التقنية 🛠️")
st.write("- **Programming & DBs:** Python, SQL, Java, C++")
st.write("- **Data Engineering & Cloud:** Microsoft Azure, AWS, Data Warehousing, ETL, Data Modeling")
st.write("- **Tools:** Pandas, NumPy, Scikit-Learn, Streamlit")
st.write("- **Media:** Video Production, Digital Marketing, Scriptwriting")

st.divider()

# قسم التعليم (Education)
st.header("التعليم المتواصل 🎓")
st.write("**B.Sc. in Data Science** - Alexandria University (2024 - 2028)")
st.write("**STEM High School Diploma** - Kafr El-Sheikh (2021 - 2024)")