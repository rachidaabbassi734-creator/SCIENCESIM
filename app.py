import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# إعداد الصفحة لتأخذ العرض الكامل
st.set_page_config(page_title="ScienceSim - محاكاة تفاعلية", layout="wide")

st.title("⚡ مختبر الفيزياء الافتراضي: محاكاة قانون أوم والمماثلة الهيدروليكية")
st.write("حرك المؤشرات في القائمة الجانبية لتشاهد كيف تتغير الدائرة الكهربائية والمماثلة المائية بصرياً وحركياً!")

st.markdown("---")

# لوحة التحكم الجانبية
with st.sidebar:
    st.header("⚙️ لوحة التحكم بالتجربة")
    R = st.slider("🚧 المقاومة (R) - تضييق الأنبوب (Ω):", min_value=1.0, max_value=20.0, value=10.0, step=0.5)
    I = st.slider("🌊 شدة التيار (I) - تدفق الماء (A):", min_value=0.5, max_value=5.0, value=2.0, step=0.1)

# حساب التوتر بناءً على قانون أوم
U = R * I

# تقسيم العرض إلى قسمين: الحسابات والمحاكاة المرئية
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 القياسات الرقمية")
    st.metric(label="التوتر الكهربائي المستنتج (U = R × I):", value=f"{U:.2f} V")
    st.markdown(f"""
    - **قيمة المقاومة:** `{R} Ω`
    - **شدة التيار:** `{I} A`
    - **التشبيه المائي:** التوتر الحالي يماثل ضغط ماء بارتفاع `{U:.1f}` متر!
    """)

with col2:
    st.subheader("💧 المحاكاة المرئية للمماثلة الهيدروليكية")
    
    # بناء الرسم البياني التوضيحي المتحرك
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # 1. رسم الأنبوب المائي (يتأثر عرضه بالمقاومة R)
    # كلما زادت المقاومة، يقل عرض الأنبوب في المنتصف (تضييق)
    pipe_thickness = max(0.2, 2.0 - (R / 15.0))
    
    # الجزء الأيسر من الأنبوب (واسع)
    ax.add_patch(patches.Rectangle((0, 1), 3, 2, color='lightblue', alpha=0.5))
    ax.plot([0, 3], [1, 1], color='black', lw=3)
    ax.plot([0, 3], [3, 3], color='black', lw=3)
    
    # منطقة التضييق (المقاومة R)
    ax.add_patch(patches.Rectangle((3, 2 - pipe_thickness/2), 2, pipe_thickness, color='skyblue', alpha=0.8))
    ax.plot([3, 5], [1, 2 - pipe_thickness/2], color='black', lw=3)
    ax.plot([3, 5], [3, 2 + pipe_thickness/2], color='black', lw=3)
    
    # الجزء الأيمن (خروج الماء)
    ax.add_patch(patches.Rectangle((5, 1), 3, 2, color='lightblue', alpha=0.3))
    ax.plot([5, 8], [2 - pipe_thickness/2, 1], color='black', lw=3)
    ax.plot([5, 8], [2 + pipe_thickness/2, 3], color='black', lw=3)
    ax.plot([8, 8], [1, 3], color='black', lw=3, linestyle='--')

    # 2. رسم جزيئات تدفق الماء (تتأثر شدتها وكثافتها بالتيار I)
    num_particles = int(I * 10)
    np.random.seed(42) # للحفاظ على ثبات التوزيع عند التغيير
    x_particles = np.random.uniform(0.5, 7.5, num_particles)
    y_particles = np.random.uniform(1.2, 2.8, num_particles)
    
    # حصر الجزيئات داخل منطقة التضييق لتفادي خروجها بصرياً
    y_particles = np.where((x_particles >= 3) & (x_particles <= 5), 
                           np.random.uniform(2 - pipe_thickness/2 + 0.1, 2 + pipe_thickness/2 - 0.1, num_particles), 
                           y_particles)
    
    # رسم الجزيئات المائية
    ax.scatter(x_particles, y_particles, color='blue', s=50, alpha=0.6, label='تدفق التيار (I)')

    # 3. رسم سهم ضغط الماء (يمثل التوتر U)
    # طول السهم يتناسب مع قيمة التوتر U
    arrow_length = min(3, U / 20)
    ax.arrow(0.5, 2, arrow_length, 0, head_width=0.2, head_length=0.2, fc='red', ec='red', lw=4, la
