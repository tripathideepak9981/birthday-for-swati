import streamlit as st
import os
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="For My Queen | Swati ❤️",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- LUXURY STYLING (EMBEDDED) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Poppins:wght@300;400;600&display=swap');

    /* Global Background */
    .stApp {
        background: radial-gradient(circle at top right, #1a1a2e, #16213e, #0f3460);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }

    /* Hero Section with 3D Depth */
    .hero-box {
        background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0) 100%);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 30px;
        padding: 80px 40px;
        text-align: center;
        margin: 40px 0;
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
        transform: perspective(1000px) rotateX(2deg);
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        background: linear-gradient(to right, #FAD0C4, #ff9a9e, #E63946);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
        font-weight: 700;
    }

    /* 3D Glass Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        text-align: center;
    }

    .glass-card:hover {
        transform: translateY(-15px) scale(1.02);
        background: rgba(255, 255, 255, 0.12);
        box-shadow: 0 20px 40px rgba(230, 57, 70, 0.3);
        border-color: #E63946;
    }

    /* 24 Reasons Styling */
    .reason-container {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 20px;
        padding: 40px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .reason-item {
        padding: 15px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        display: flex;
        align-items: flex-start;
        transition: 0.3s;
    }

    .reason-item:hover {
        background: rgba(230, 57, 70, 0.05);
        padding-left: 25px;
    }

    .reason-num {
        font-family: 'Playfair Display', serif;
        color: #FAD0C4;
        font-weight: 700;
        font-size: 1.2rem;
        margin-right: 20px;
        min-width: 30px;
    }

    .reason-text {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1rem;
        font-weight: 300;
        line-height: 1.4;
    }

    /* Animated Gift Box CSS */
    .gift-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 50px;
    }

    .gift-box {
        width: 100px;
        height: 100px;
        background: #E63946;
        position: relative;
        animation: bounce 1.5s infinite;
        border-radius: 10px;
        cursor: pointer;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }

    .gift-box::before {
        content: '';
        position: absolute;
        width: 20px;
        height: 100%;
        background: #FAD0C4;
        left: 40px;
    }

    .gift-box::after {
        content: '';
        position: absolute;
        height: 20px;
        width: 100%;
        background: #FAD0C4;
        top: 40px;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(5deg); }
    }

    /* Letter Section */
    .letter-paper {
        background: #fff9f0;
        color: #2d3436;
        padding: 50px;
        border-radius: 5px;
        font-family: 'Playfair Display', serif;
        line-height: 2;
        box-shadow: 15px 15px 0px #E63946;
        max-width: 800px;
        margin: auto;
    }

    /* Section Titles */
    .section-header {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        text-align: center;
        margin: 80px 0 40px 0;
        color: #FAD0C4;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #1a1a2e; }
    ::-webkit-scrollbar-thumb { background: #E63946; border-radius: 10px; }

    </style>
""", unsafe_allow_html=True)

# --- CONTENT FUNCTIONS ---
def display_img(image_path_from_app, caption):
    # App.py ki current location nikalna
    base_path = os.path.dirname(__file__)
    
    # Ab yeh sahi path banayega bina double folder ke
    full_path = os.path.join(base_path, image_path_from_app)
    
    if os.path.exists(full_path):
        st.image(full_path, caption=caption, use_container_width=True)
    else:
        # Debugging ke liye: Agar image na mile toh error dikhayega
        st.error(f"File not found at: {full_path}")

# --- 1. HERO ---
st.markdown('''
    <div class="hero-box">
        <p style="letter-spacing: 5px; color: #E63946; font-weight: 600;">CELEBRATING 24 YEARS OF YOU</p>
        <h1 class="hero-title">Happy Birthday, Swati</h1>
        <p style="font-size: 1.4rem; opacity: 0.8; font-weight: 300;">My today, my tomorrow, and my forever.</p>
    </div>
''', unsafe_allow_html=True)

# --- 2. THE STORY (3D CARDS) ---
st.markdown('<h2 class="section-header">Why You Are Special</h2>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('''
        <div class="glass-card">
            <h2 style="color: #E63946;">✨ Peace</h2>
            <p>The way you bring calm to my chaos is a superpower. In your presence, the world finally makes sense.</p>
        </div>
    ''', unsafe_allow_html=True)

with c2:
    st.markdown('''
        <div class="glass-card">
            <h2 style="color: #E63946;">❤️ Love</h2>
            <p>Your love is pure, mature, and grounding. It’s not just a feeling; it’s the foundation of my life.</p>
        </div>
    ''', unsafe_allow_html=True)

with c3:
    st.markdown('''
        <div class="glass-card">
            <h2 style="color: #E63946;">🌟 Growth</h2>
            <p>Because of you, I want to be a better man. You inspire me to reach for heights I never dared to dream of.</p>
        </div>
    ''', unsafe_allow_html=True)

# --- NEW SECTION: 24 REASONS WHY ---
st.markdown('<h2 class="section-header">24 Reasons Why I Love You</h2>', unsafe_allow_html=True)

reasons = [
    "The way your eyes sparkle when you're truly happy.",
    "How you make the most mundane days feel like a celebration.",
    "Your unwavering patience, even when I'm at my most difficult.",
    "The way you carry yourself with so much grace and dignity.",
    "Your kindness, which radiates to everyone you meet.",
    "The profound peace I find just sitting in silence with you.",
    "You are my biggest cheerleader and my safest harbor.",
    "The way you’ve completely changed my perspective on what love is.",
    "Your quiet strength that helps me stay grounded in storms.",
    "How you remember the tiny details I mention in passing.",
    "You make me want to be a better man every single day.",
    "Your laughter is, and will always be, my favorite soundtrack.",
    "How you handle my moods and flaws with so much tenderness.",
    "The way you’ve given my life a true sense of direction.",
    "Your unique sense of humor that only I truly understand.",
    "The confidence you've built in me just by believing in me.",
    "The way you care for your family and the people you love.",
    "Your resilience—you are the strongest woman I know.",
    "How you’ve turned my world from grayscale to vibrant color.",
    "The way you trust me with your heart and your dreams.",
    "Your intelligence and the way you look at the world.",
    "How you’ve turned a house into a home with your presence.",
    "Because you are my best friend first, and my lover second.",
    "Simply because you are Swati—there is no one else like you."
]

r_col1, r_col2 = st.columns(2)
with r_col1:
    st.markdown('<div class="reason-container">', unsafe_allow_html=True)
    for i in range(0, 12):
        st.markdown(f'''
            <div class="reason-item">
                <div class="reason-num">{i+1}</div>
                <div class="reason-text">{reasons[i]}</div>
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with r_col2:
    st.markdown('<div class="reason-container">', unsafe_allow_html=True)
    for i in range(12, 24):
        st.markdown(f'''
            <div class="reason-item">
                <div class="reason-num">{i+1}</div>
                <div class="reason-text">{reasons[i]}</div>
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 3. PHOTO GALLERY ---
st.markdown('<h2 class="section-header">Captured Moments</h2>', unsafe_allow_html=True)
col_a, col_b, col_c = st.columns(3)
with col_a: display_img("assets/images/photo1.jpg", "Your beautiful smile")
with col_b: display_img("assets/images/photo2.jpg", "A moment of grace")
with col_c: display_img("assets/images/photo3.jpg", "The way I see you")

# --- 4. THE GIFT (3D ANIMATED) ---
st.markdown('<h2 class="section-header">A Special Surprise</h2>', unsafe_allow_html=True)
st.markdown('<div class="gift-container"><div class="gift-box"></div></div>', unsafe_allow_html=True)

if st.button("Click to Open Your Gift 🎁", use_container_width=True):
    st.balloons()
    st.markdown('''
        <div style="background: rgba(230,57,70,0.2); padding: 40px; border-radius: 20px; text-align: center; border: 1px solid #E63946;">
            <h2 style="color: #FAD0C4; font-family: 'Playfair Display';">My Lifelong Commitment</h2>
            <p style="font-size: 1.2rem;">Swati, my gift to you is my unwavering support, my deepest respect, and a love that grows stronger with every passing heartbeat. You are my greatest blessing.</p>
        </div>
    ''', unsafe_allow_html=True)

# --- 5. THE LETTER ---
st.markdown('<h2 class="section-header">To My Dearest Swati</h2>', unsafe_allow_html=True)
st.markdown('''
    <div class="letter-paper">
        <p>My Love,</p>
        <p>Watching you turn 24 fills me with so much pride. You carry yourself with a grace that is rare and a strength that is quiet yet powerful. 
        Before you came into my life, I was wandering; after you arrived, I found my home.</p>
        <p>Thank you for the peace you bring to my mind and the joy you bring to my soul. You are my best decision, 
        and I promise to stand by you as you conquer every dream you've ever had. This year is yours, and I am so 
        lucky to have a front-row seat to your greatness.</p>
        <p>Happy Birthday, beautiful.</p>
        <p style="text-align: right; font-weight: bold;">Yours Always,<br>Deepak</p>
    </div>
''', unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown('''
    <div style="text-align: center; margin-top: 100px; padding-bottom: 50px;">
        <p style="letter-spacing: 8px; color: #E63946; font-size: 0.8rem;">ALWAYS YOURS • FOREVER TOGETHER</p>
    </div>
''', unsafe_allow_html=True)