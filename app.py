import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

# 1. إعدادات الصفحة العامة والهوية البصرية للموقع
st.set_page_config(
    page_title="ScienceSim - منصة المختبرات الرقمية المربحة",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تصميم مخصص باستخدام CSS لإعطاء مظهر احترافي للموقع
st.markdown("""
<style>
    .main-title { font-size: 40px !important; color: #2C3E50; text-align: center; font-weight: bold; margin-bottom: 20px; }
    .hero-text { font-size: 20px; text-align: center; color: #7F8C8D; margin-bottom: 40px; }
    .premium-box { background-color: #FFF3CD; border-left: 5px solid #FFC107; padding: 20px; border-radius: 5px; }
    .footer-text { text-align: center; padding: 20px; color: #BDC3C7; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# 2. القائمة الجانبية (Sidebar) - للتنقل بين أقسام الموقع
st.sidebar.title("🧭 تصفح المنصة")
page = st.sidebar.radio("انتقل إلى:", ["🏠 الصفحة الرئيسية", "🧪 المختبر الافتراضي (قانون أوم)", "📚 مقالات ودروس (SEO)", "💎 الاشتراك المميز (VIP)"])

# إضافة مساحة إعلانية تجريبية في القائمة الجانبية لمحاكاة الأرباح
st.sidebar.markdown("---")
st.sidebar.caption("📢 مساحة إعلانية (Google AdSense)")
st.sidebar.image("https://via.placeholder.com/250x250.png?text=Ad+Space+Available", use_container_width=True)


# ==================== القسم 1: الصفحة الرئيسية ====================
if page == "🏠 الصفحة الرئيسية":
    st.markdown('<div class="main-title">⚡ مرحباً بك في منصة ScienceSim التعليمية</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-text">المنصة الأولى لتبسيط العلوم والفيزياء عبر مختبرات ومحاكاة تفاعلية ومجانية بالكامل.</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("🎯 محاكاة تفاعلية")
        st.write("مختبرات افتراضية تساعد الطلاب على فهم أصعب تجارب الفيزياء والكيمياء بلمسة زر.")
    with col2:
        st.info("📚 دروس ومخلصات")
        st.write("جذاذات وملخصات دروس جاهزة للتحميل متوافقة مع المناهج التعليمية الحديثة للأساتذة.")
    with col3:
        st.warning("💰 استثمار رقمي")
        st.write("موقع مهيأ بالكامل لدمج إعلانات أدسينس وبوابات الدفع لتحقيق دخل مادي مستدام.")

    st.markdown("---")
    st.subheader("🔥 المحاكاة الأكثر شعبية هذا الأسبوع")
    st.info("💡 اضغط على 'المختبر الافتراضي' في القائمة الجانبية لتجربة محاكاة قانون أوم تفاعلياً!")


# ==================== القسم 2: المختبر الافتراضي ====================
elif page == "🧪 المختبر الافتراضي (قانون أوم)":
    st.title("⚡ مختبر الفيزياء: محاكاة تفاعلية لقانون أوم")
    st.write("حرك المؤشرات في الجانب الأيمن لمشاهدة تغير التوتر والتيار والمقاومة بشكل حي ومباشر.")
    
    st.markdown("---")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🎛️ لوحة التحكم")
        # مؤشرات التحكم التفاعلية
        R = st.slider("المقاومة (R) بالأوم Ω:", min_value=1, max_value=100, value=20)
        I = st.slider("شدة التيار (I) بالأمبير A:", min_value=0.1, max_value=5.0, value=1.5, step=0.1)
        
        # حساب التوتر الرياضي
        U = R * I