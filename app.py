import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

# 1. إعداد النافذة البيانية والمحاور
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
plt.subplots_adjust(bottom=0.25)

# المتغيرات الفيزيائية الابتدائية
tension_h = 3.0
circuit_actif = True

# إعداد النقط المتحركة (الماء والإلكترونات)
gouttes_x = np.random.uniform(2.0, 2.2, 20)
gouttes_y = np.random.uniform(0, tension_h, 20)
pos_electrons = np.linspace(0, 16, 25)

def dessiner_decor_fixe():
    # المحور الأول: النموذج الهيدروليكي (الشلال)
    ax1.set_xlim(0, 6)
    ax1.set_ylim(-0.5, 6)
    ax1.axis('off')
    
    falaise_x = [0, 2, 2, 6]
    falaise_y = [tension_h, tension_h, 0, 0]
    ax1.fill_between(falaise_x, falaise_y, color='#8B5A2B', alpha=0.7) 
    ax1.plot([0, 2, 2, 6], [tension_h, tension_h, 0, 0], color='#4A2E1B', lw=4)
    ax1.axhspan(-0.5, 0, color='#228B22', alpha=0.3) 
    ax1.text(0.5, 5.5, "🏔️ SYSTÈME HYDRAULIQUE", fontsize=11, fontweight='bold')

    # المحور الثاني: الدارة الكهربائية المعيارية (3APIC)
    ax2.set_xlim(0, 6)
    ax2.set_ylim(-0.5, 6)
    ax2.axis('off')
    ax2.text(0.5, 5.5, "⚡ CIRCUIT ÉLECTRIQUE", fontsize=11, fontweight='bold')
    
    # أسلاك التوصيل
    ax2.plot([1, 5, 5, 1, 1], [1, 1, 5, 5, 1], color='black', lw=2, zorder=1)
    
    # المولد المعياري (عمود كهربائي)
    ax2.vlines(x=3, ymin=4.7, ymax=5.3, color='red', lw=4, zorder=2) 
    ax2.vlines(x=2.8, ymin=4.9, ymax=5.1, color='blue', lw=6, zorder=2) 
    ax2.text(2.6, 5.4, "+", color='red', fontsize=14, fontweight='bold')
    ax2.text(3.2, 5.4, "-", color='blue', fontsize=14, fontweight='bold')

# إنشاء النصوص الديناميكية التي تتغير أثناء المحاكاة
txt_hydrau = ax1.text(2.5, 5, "", fontsize=10, fontweight='bold', bbox=dict(facecolor='white', alpha=0.8))
txt_elec = ax2.text(1.5, 0.3, "", fontsize=10, fontweight='bold', bbox=dict(facecolor='white', alpha=0.8))

def deplacer_electrons(positions, vitesse):
    xs, ys = [], []
    for p in positions:
        p = (p + vitesse) % 16
        if p < 4:
            x, y = 5 - p, 5
        elif p < 8:
            x, y = 1, 5 - (p - 4)
        elif p < 12:
            x, y = 1 + (p - 8), 1
        else:
            x, y = 5, 1 + (p - 12)
        xs.append(x)
        ys.append(y)
    return xs, ys, positions + vitesse

def update(frame):
    global gouttes_y, pos_electrons
    ax1.clear()
    ax2.clear()
    dessiner_decor_fixe()
    
    # السرعة تتناسب طردياً مع الارتفاع/التوتر (السبب والنتيجة)
    vitesse = tension_h * 0.08 
    
    # --- حركة الشلال الهيدروليكي ---
    if circuit_actif:
        gouttes_y -= vitesse
        gouttes_y = np.where(gouttes_y <= 0, tension_h, gouttes_y)
        ax1.plot(gouttes_x, gouttes_y, 'bo', ms=5, color='#4169E1')
        ax1.plot([0, 2], [tension_h+0.1, tension_h+0.1], color='#4169E1', lw=6)
        ax1.plot([2, 6], [0.1, 0.1], color='#4169E1', lw=6)
        txt_hydrau.set_text(f"Hauteur Falaise = {tension_h:.1f} m\n🌊 Courant d'eau : ACTIF")
    else:
        ax1.plot([1.9, 1.9], [tension_h, tension_h+0.6], color='red', lw=5) 
        ax1.text(1.2, tension_h+0.7, "BARRAGE FERMÉ", color='red', fontweight='bold')
        txt_hydrau.set_text(f"Hauteur Falaise = {tension_h:.1f} m\n❌ Débit d'eau = 0")
        
    # السطر 101 المصحح والمغلق بالكامل وبدون أي أخطاء سنتكس
    ax1.text(2.3, tension_h/2, f"↕ Dh = {tension_h:.1f} m", color='red', fontsize=12, fontweight='bold')

    # --- حركة الإلكترونات في الدارة ---
    if circuit_actif:
        ax2.plot([1, 1], [2.7, 3.3], color='black', lw=4) # قاطع التيار مغلق
        x_e, y_e, pos_electrons = deplacer_electrons(pos_electrons, vitesse)
        ax2.plo
