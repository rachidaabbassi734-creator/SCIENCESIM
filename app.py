import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# إعداد الصفحة لتكون مريحة وتأخذ العرض الكامل
st.set_page_config(page_title="ScienceSim - قانون أوم", layout="wide")

# عنوان المحاكاة
st.title("⚡ مختبر الفيزياء: محاكاة تفاعلية لقانون أوم")
st.write("قم بتغيير قيم المقاومة وشدة التيار من لوحة التحكم الجانبية لمشاهدة تغير التوتر والمماثلة الهيدروليكية.")

st.markdown("---")

# إنشاء لوحة التحكم في القائمة الجانبية (Sidebar)
with st.sidebar:
    st.header("⚙️ لوحة التحكم")
    R = st.slider("المقاومة (R) بالأوم Ω:", min_value=1.0, max_value=100.0, value=10.0, step=0.5)
    I = st.slider("شدة التيار (I) بالأمبير A:", min_value=0.1, max_value=5.0, value=1.5, step=0.1)

# حساب التوتر بناءً على قانون أوم U = R * I
U = R * I

# تقسيم الصفحة إلى عمودين كبيرين متناسقين
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 النتيجة الحسابية والمبيان")
    # عرض النتيجة بوضوح
    st.metric(label="التوتر الكهربائي المحسوب (U):", value=f"{U:.2f} V")
    
    # رسم مبيان تفاعلي بسيط بقيم متغيرة
    fig, ax = plt.subplots(figsize=(5, 3.5))
    current_range = np.linspace(0, 5, 100)
    voltage_range = R * current_range
    
    ax.plot(current_range, voltage_range, color='blue', label=f'U = {R} * I')
    ax.scatter(I, U, color='red', s=100, zorder=5, label=f'النقطة الحالية ({I}A, {U:.1f}V)')
    
    ax.set_xlabel("شدة التيار (I) بالأمبير")
    ax.set_ylabel("التوتر (U) بالفولت")
    ax.set_title("منحنى تغيرات التوتر بدلالة التيار")
    ax.grid(True, linestyle='--')
    ax.legend()
    
    st.pyplot(fig)

with col2:
    st.subheader("💧 المماثلة الهيدروليكية (Hydraulic Analogy)")
    st.write("لفهم التجريد الفيزيائي، تخيل الدائرة الكهربائية كمضخة أنابيب مياه:")
    
    # رسم توضيحي بسيط للمماثلة الهيدروليكية باستخدام Matplotlib
    fig2, ax2 = plt.subplots(figsize=(5, 3.5))
    
    # رسم تشبيهي للمضخة والتضييق
    ax2.text(0.5, 0.8, f"💧 ضغط الماء (التوتر U) = {U:.2f} متر", fontsize=11, ha='center', color='blue', weight='bold')
    ax2.text(0.5, 0.5, f"🚧 تضييق الأنبوب (المقاومة R) = {R} أوم", fontsize=11, ha='center', color='red', weight='bold')
    ax2.text(0.5, 0.2, f"🌊 تدفق الماء (التيار I) = {I} أمبير", fontsize=11, ha='center', color='green', weight='bold')
    
    # إخفاء المحاور لتبدو كبطاقة توضيحية جمالية
    ax2.axis('off')
    ax2.set_facecolor('#f0f2f6')
    st.pyplot(fig2)
