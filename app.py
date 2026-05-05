import streamlit as st

st.set_page_config(layout="wide")

# ---------------- CSS ---------------- #
st.markdown("""
<style>

body {
    background-color: #0b0b0d;
}

.hero-shell {
    padding: 3rem;
    background:
        radial-gradient(circle at 0% 0%, rgba(229, 57, 53, 0.18), transparent 30%),
        linear-gradient(135deg, #050505 0%, #0b0b0d 48%, #111111 100%);
    border-radius: 20px;
}

.hero-grid {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}

.hero-copy {
    width: 55%;
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    color: white;
    line-height: 1.1;
}

.highlight-red {
    color: #ff3b30;
}

.hero-subline {
    margin-top: 20px;
    color: #bdbdbd;
    font-size: 16px;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    margin-right: 8px;
    margin-top: 15px;
    border-radius: 20px;
    border: 1px solid #444;
    color: #ddd;
    font-size: 12px;
}

.badge-red {
    border-color: #ff3b30;
    color: #ff3b30;
}

.hero-profile {
    width: 320px;
    position: relative;
}

.hero-profile::before {
    content: "";
    position: absolute;
    inset: -20px;
    background: radial-gradient(circle, rgba(255,59,48,0.25), transparent);
    filter: blur(20px);
}

.hero-profile img {
    width: 100%;
    position: relative;
    z-index: 2;
    filter: drop-shadow(0 25px 40px rgba(0,0,0,0.8));
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ---------------- #
def render_home():
    hero_html = """
    <div class="hero-shell">
        <div class="hero-grid">

            <div class="hero-copy">
                <div class="hero-title">
                    I drive <span class="highlight-red">business growth</span><br>
                    through execution and data.
                </div>

                <div class="hero-subline">
                    Experience across startup operations, analytics, customer engagement,
                    and commercial execution in high-performance environments.
                </div>

                <div>
                    <span class="badge badge-red">Revenue Growth</span>
                    <span class="badge badge-red">Execution</span>
                    <span class="badge">Analytics</span>
                    <span class="badge">Partnerships</span>
                </div>
            </div>

            <div class="hero-profile">
                <img src="assets/shalini-profile.png">
            </div>

        </div>
    </div>
    """

    st.markdown(hero_html, unsafe_allow_html=True)

# ---------------- RUN ---------------- #
render_home()
