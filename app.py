import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from content import (
    metrics,
    portfolio_fit_areas,
    projects,
    analytics_projects,
    experience,
    education,
    leadership_items,
    extra_curricular_items,
    skills,
    skill_notes,
    skills_visuals,
)

st.set_page_config(
    page_title="Shalini Arun Prakash | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 0% 0%, rgba(229, 57, 53, 0.18), transparent 30%),
        radial-gradient(circle at 100% 10%, rgba(255, 107, 107, 0.09), transparent 25%),
        linear-gradient(135deg, #050505 0%, #0b0b0d 48%, #111111 100%);
    color: #ffffff;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 3rem;
    max-width: 1360px;
}

h1, h2, h3, h4 {
    color: #ffffff !important;
    letter-spacing: -0.035em;
}

p, li, span, div {
    color: #e5e5e5;
}

.hero-shell {
    position: relative;
    overflow: hidden;
    min-height: 660px;
    background:
        radial-gradient(circle at 82% 22%, rgba(229, 57, 53, 0.18), transparent 28%),
        radial-gradient(circle at 10% 0%, rgba(255, 107, 107, 0.10), transparent 24%),
        linear-gradient(135deg, #050505 0%, #0b0b0d 48%, #111111 100%);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 35px 100px rgba(0,0,0,0.65);
    margin-bottom: 1.2rem;
}

.hero-shell:after {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(90deg, rgba(0,0,0,0.08), rgba(229,57,53,0.04)),
        radial-gradient(circle at 78% 72%, rgba(255,255,255,0.04), transparent 34%);
    pointer-events: none;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 1240px;
    padding: 4.4rem 4rem 3.2rem 4rem;
}

.hero-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.35fr) minmax(280px, 0.65fr);
    gap: 3rem;
    align-items: end;
}

.hero-copy {
    min-width: 0;
}

.hero-profile-wrap {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    min-height: 500px;
}

.hero-profile-stage {
    position: relative;
    width: min(360px, 100%);
    display: flex;
    justify-content: center;
    align-items: flex-end;
}

.hero-profile-stage:before {
    content: "";
    position: absolute;
    inset: 22px 10px -8px 10px;
    border-radius: 36px;
    background:
        radial-gradient(circle at 50% 24%, rgba(229,57,53,0.34), transparent 54%),
        linear-gradient(180deg, rgba(255,255,255,0.075), rgba(255,255,255,0.018));
    border: 1px solid rgba(255,255,255,0.13);
    box-shadow: 0 32px 90px rgba(0,0,0,0.55);
    z-index: 0;
}

.hero-profile-stage:after {
    content: "";
    position: absolute;
    width: 86%;
    height: 24px;
    bottom: -10px;
    background: rgba(0,0,0,0.55);
    filter: blur(18px);
    border-radius: 999px;
    z-index: 0;
}

.hero-profile-img {
    position: relative;
    z-index: 2;
    width: 92%;
    max-height: 500px;
    object-fit: contain;
    filter:
        drop-shadow(0 28px 42px rgba(0,0,0,0.78))
        brightness(1.02)
        contrast(1.04);
}

.hero-proof-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin-top: 1.5rem;
}

.hero-proof-pill {
    min-width: 130px;
    padding: 0.85rem 1rem;
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.12);
    border-left: 4px solid #E53935;
}

.hero-proof-value {
    font-size: 1.35rem;
    font-weight: 950;
    color: #ffffff;
    line-height: 1;
}

.hero-proof-label {
    color: #a1a1aa;
    font-size: 0.76rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 0.35rem;
}

.name-chip {
    display: inline-flex;
    padding: 0.65rem 1.05rem;
    border-radius: 999px;
    background: #E53935;
    color: #ffffff;
    font-size: 0.82rem;
    font-weight: 950;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1.4rem;
    box-shadow: 0 18px 45px rgba(229,57,53,0.28);
}

.hero-title {
    font-size: clamp(3rem, 5.7vw, 6rem);
    line-height: 0.94;
    font-weight: 950;
    color: #ffffff;
    margin-bottom: 1.35rem;
    max-width: 1180px;
    text-shadow: 0 14px 45px rgba(0,0,0,0.55);
    text-transform: uppercase;
}

.highlight-red {
    color: #E53935;
    background: none;
    -webkit-text-fill-color: #E53935;
    display: inline-block;
}

.hero-subline {
    font-size: 1.08rem;
    line-height: 1.75;
    max-width: 930px;
    color: #d4d4d8;
    margin-bottom: 1.6rem;
}

.hero-mini-card {
    padding: 1rem;
    background: rgba(17,17,19,0.88);
    border: 1px solid rgba(255,255,255,0.10);
    border-left: 4px solid #E53935;
    min-height: 135px;
    margin-bottom: 1rem;
    transition: all 0.22s ease-in-out;
}

.hero-mini-card b {
    color: #ffffff;
    font-size: 0.95rem;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}

.hero-mini-card p {
    color: #a1a1aa;
    font-size: 0.86rem;
    margin: 0.35rem 0 0 0;
    line-height: 1.45;
}

.badge {
    display: inline-flex;
    align-items: center;
    padding: 0.42rem 0.72rem;
    margin: 0.28rem 0.42rem 0.28rem 0;
    border-radius: 999px;
    background: rgba(255,255,255,0.045);
    color: #f5f5f5;
    border: 1px solid rgba(255,255,255,0.12);
    font-size: 0.68rem;
    font-weight: 750;
    text-transform: uppercase;
    letter-spacing: 0.045em;
    line-height: 1.2;
    white-space: nowrap;
}

.badge-red {
    background: rgba(229,57,53,0.10);
    color: #ffffff;
    border: 1px solid rgba(229,57,53,0.32);
}

.badge-light-red {
    background: rgba(255,107,107,0.08);
    color: #ffffff;
    border: 1px solid rgba(255,107,107,0.30);
}

.section-title {
    font-size: 2.35rem;
    font-weight: 950;
    color: #ffffff;
    margin-top: 3.2rem;
    margin-bottom: 0.55rem;
    text-transform: uppercase;
}

.section-title:after {
    content: "";
    display: block;
    width: 72px;
    height: 4px;
    background: #E53935;
    margin-top: 0.65rem;
}

.section-caption {
    color: #a1a1aa;
    font-size: 1rem;
    margin-bottom: 1.35rem;
    line-height: 1.65;
    max-width: 990px;
}

.metric-card {
    position: relative;
    overflow: hidden;
    background: #111113;
    border: 1px solid rgba(255,255,255,0.10);
    padding: 1.35rem;
    min-height: 150px;
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.35);
    margin-bottom: 1rem;
    transition: all 0.22s ease-in-out;
}

.metric-card:before {
    content: "";
    position: absolute;
    width: 6px;
    height: 100%;
    left: 0;
    top: 0;
    background: #E53935;
}

.metric-value {
    font-size: 2.25rem;
    font-weight: 950;
    color: #ffffff;
    margin-bottom: 0.38rem;
}

.metric-label {
    font-size: 0.9rem;
    color: #a1a1aa;
    line-height: 1.42;
    position: relative;
    z-index: 1;
}

.fit-card {
    background: #111113;
    border: 1px solid rgba(255,255,255,0.12);
    border-top: 4px solid #E53935;
    padding: 1.25rem;
    min-height: 210px;
    box-shadow: 0 18px 50px rgba(0,0,0,0.35);
    margin-bottom: 1rem;
    transition: all 0.22s ease-in-out;
}

.fit-card h3 {
    text-transform: uppercase;
    font-size: 1.1rem;
    margin-bottom: 0.65rem;
}

.fit-card p {
    color: #d4d4d8;
    font-size: 0.92rem;
    line-height: 1.55;
}

.visual-card {
    background: #111113;
    border: 1px solid rgba(255,255,255,0.12);
    border-top: 4px solid #E53935;
    padding: 1.2rem;
    box-shadow: 0 18px 50px rgba(0,0,0,0.35);
    margin-bottom: 1rem;
    transition: all 0.22s ease-in-out;
}

.project-card {
    overflow: hidden;
    background: #111113;
    border: 1px solid rgba(255,255,255,0.11);
    padding: 0;
    margin-bottom: 1.25rem;
    box-shadow: 0 20px 62px rgba(0, 0, 0, 0.35);
    transition: all 0.22s ease-in-out;
}

.project-card:hover,
.metric-card:hover,
.fit-card:hover,
.visual-card:hover,
.skill-visual-card:hover,
.hero-mini-card:hover {
    transform: translateY(-3px);
    border-color: rgba(255,107,107,0.42);
    box-shadow: 0 24px 70px rgba(0,0,0,0.48);
}

.project-img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    border-bottom: 4px solid #E53935;
    opacity: 0.90;
    filter: grayscale(12%) contrast(1.08);
}

.experience-img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-bottom: 4px solid #E53935;
    opacity: 0.90;
    filter: grayscale(10%) contrast(1.08);
}

.project-body,
.experience-body {
    padding: 1.35rem 1.45rem 1.5rem 1.45rem;
}

.project-title {
    font-size: 1.35rem;
    line-height: 1.18;
    font-weight: 950;
    color: #ffffff;
    margin-bottom: 0.45rem;
    text-transform: uppercase;
}

.project-meta {
    font-size: 0.82rem;
    color: #FF6B6B;
    font-weight: 850;
    margin-bottom: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}

.project-summary {
    font-size: 0.96rem;
    color: #d4d4d8;
    line-height: 1.6;
    margin-bottom: 0.85rem;
}

.relevance-box {
    background: rgba(229,57,53,0.10);
    border-left: 4px solid #E53935;
    padding: 1rem;
    margin-top: 1rem;
    color: #ffffff;
}

.timeline-title {
    font-size: 1.13rem;
    font-weight: 950;
    color: #ffffff;
    text-transform: uppercase;
}

.timeline-meta {
    color: #FF6B6B;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
    font-weight: 850;
}

.timeline-detail {
    color: #d4d4d8;
    line-height: 1.6;
    margin-bottom: 0.85rem;
}

.achievement-list {
    color: #d4d4d8;
    line-height: 1.7;
    margin-top: 0.6rem;
}

.image-banner-card {
    min-height: 270px;
    background-size: cover;
    background-position: center;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 20px 62px rgba(0,0,0,0.38);
    position: relative;
    overflow: hidden;
    margin-bottom: 1.25rem;
}

.image-banner-overlay {
    background: linear-gradient(90deg, rgba(0,0,0,0.93), rgba(0,0,0,0.68), rgba(0,0,0,0.28));
    min-height: 270px;
    padding: 2rem;
}

.image-banner-title {
    font-size: 2rem;
    font-weight: 950;
    text-transform: uppercase;
    color: #ffffff;
    margin-bottom: 0.7rem;
}

.image-banner-text {
    max-width: 760px;
    color: #d4d4d8;
    line-height: 1.65;
}

.skill-visual-card {
    position: relative;
    min-height: 390px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.12);
    background: #111113;
    box-shadow: 0 20px 62px rgba(0,0,0,0.38);
    margin-bottom: 1.25rem;
    transition: all 0.22s ease-in-out;
}

.skill-visual-img {
    width: 100%;
    height: 175px;
    object-fit: cover;
    opacity: 0.82;
    filter: grayscale(10%) contrast(1.08);
    border-bottom: 4px solid #E53935;
}

.skill-visual-body {
    padding: 1.25rem 1.35rem 1.35rem 1.35rem;
}

.skill-visual-title {
    font-size: 1.1rem;
    font-weight: 950;
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    margin-bottom: 0.75rem;
}

.skill-visual-evidence {
    color: #d4d4d8;
    font-size: 0.9rem;
    line-height: 1.55;
    margin-top: 0.8rem;
}

.skill-visual-methods {
    color: #a1a1aa;
    font-size: 0.85rem;
    line-height: 1.5;
    margin-top: 0.7rem;
    padding-top: 0.7rem;
    border-top: 1px solid rgba(255,255,255,0.10);
}

.skill-item {
    display: inline-block;
    padding: 0.42rem 0.65rem;
    margin: 0.22rem;
    border: 1px solid rgba(255,107,107,0.45);
    background: rgba(255,107,107,0.10);
    color: #ffffff;
    font-size: 0.74rem;
    font-weight: 750;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}

.skill-strip {
    display: flex;
    gap: 0.7rem;
    flex-wrap: wrap;
    margin-top: 1rem;
    margin-bottom: 1.5rem;
}

.skill-strip-item {
    flex: 1;
    min-width: 170px;
    background: rgba(229,57,53,0.10);
    border: 1px solid rgba(229,57,53,0.35);
    padding: 0.9rem;
    text-align: center;
    font-size: 0.82rem;
    font-weight: 850;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #ffffff;
}

.contact-card {
    background: #111113;
    border: 1px solid rgba(255,255,255,0.12);
    padding: 1.6rem;
    box-shadow: 0 22px 60px rgba(0,0,0,0.36);
    min-height: 300px;
    border-top: 5px solid #E53935;
}

div[data-testid="stExpander"] {
    background: #111113;
    border: 1px solid rgba(255,255,255,0.12);
    overflow: hidden;
    margin-bottom: 1rem;
}

div[data-testid="stExpander"] summary {
    color: #ffffff !important;
    font-weight: 900;
    text-transform: uppercase;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: #111113;
    padding: 10px;
    border-radius: 0px;
    border: 1px solid rgba(255,255,255,0.12);
    position: sticky;
    top: 0;
    z-index: 999;
}

.stTabs [data-baseweb="tab"] {
    height: 48px;
    border-radius: 0px;
    padding: 0 18px;
    background: #18181b;
    color: #ffffff;
    font-weight: 850;
    text-transform: uppercase;
}

.stTabs [aria-selected="true"] {
    background: #E53935 !important;
    color: #ffffff !important;
}

.stDataFrame {
    border-radius: 0px;
    overflow: hidden;
}

hr {
    border: none;
    height: 1px;
    background: rgba(255,255,255,0.12);
    margin: 2rem 0;
}

@media (max-width: 900px) {
    .hero-content { padding: 2.2rem; }
    .hero-title { font-size: 3.2rem; }
    .hero-grid { grid-template-columns: 1fr; gap: 1.5rem; }
    .hero-profile-wrap { min-height: auto; margin-top: 1.5rem; }
    .hero-profile-stage { width: min(300px, 100%); }
}
</style>
""",
    unsafe_allow_html=True,
)


def render_badges(items, style="badge"):
    st.markdown("".join([f'<span class="{style}">{item}</span>' for item in items]), unsafe_allow_html=True)


def render_metric_card(value, label):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_fit_card(area, evidence):
    st.markdown(
        f"""
        <div class="fit-card">
            <h3>{area}</h3>
            <p>{evidence}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_image_banner(title, text, image_url):
    st.markdown(
        f"""
        <div class="image-banner-card" style="background-image:url('{image_url}');">
            <div class="image-banner-overlay">
                <div class="image-banner-title">{title}</div>
                <div class="image-banner-text">{text}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_project_card(project):
    st.markdown(
        f"""
        <div class="project-card">
            <img src="{project["image"]}" class="project-img">
            <div class="project-body">
                <div class="project-title">{project["title"]}</div>
                <div class="project-meta">{project["capability"]} · {project["location"]}</div>
                <div class="project-summary">{project["summary"]}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_badges(project["frameworks"][:4], "badge-light-red")

    with st.expander("Explore case study"):
        c1, c2 = st.columns([1, 1])

        with c1:
            st.markdown("#### Context")
            st.write(project["context"])

            st.markdown("#### Problem")
            st.write(project["problem"])

            st.markdown("#### My Role")
            st.write(project["role"])

            st.markdown("#### Approach")
            for item in project["approach"]:
                st.write(f"• {item}")

        with c2:
            st.markdown("#### Key Outputs")
            for item in project["outputs"]:
                st.write(f"• {item}")

            st.markdown("#### Tools")
            render_badges(project["tools"][:4], "badge-red")

            st.markdown("#### Relevance")
            st.markdown(
                f"""
                <div class="relevance-box">
                    {project["strategic_relevance"]}
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_experience_card(item):
    achievement_html = "".join([f"<li>{achievement}</li>" for achievement in item["achievements"]])
    st.markdown(
        f"""
        <div class="project-card">
            <img src="{item["image"]}" class="experience-img">
            <div class="experience-body">
                <div class="timeline-title">{item["title"]}</div>
                <div class="timeline-meta">{item["period"]}</div>
                <div class="timeline-detail">{item["description"]}</div>
                <div class="achievement-list">
                    <b>Achievements:</b>
                    <ul>{achievement_html}</ul>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_simple_visual_card(item):
    chips = "".join([f'<span class="skill-item">{skill}</span>' for skill in item["skills"]])
    st.markdown(
        f"""
        <div class="project-card">
            <img src="{item["image"]}" class="project-img">
            <div class="project-body">
                <div class="project-title">{item["title"]}</div>
                <div class="project-meta">{item.get("category", "Extra-Curricular")} · {item.get("location", "")}</div>
                <div class="project-summary">{item["summary"]}</div>
                <div>{chips}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def make_commercial_proof_bubble_map():
    data = pd.DataFrame({
        "Proof Point": [
            "3× Revenue Growth",
            "2,000+ Live Sessions",
            "150+ Monthly Conversions",
            "$3.5M Proposal",
            "100+ Survey Responses",
            "10+ Expert Interviews",
            "60% Utilisation",
            "14+ Workstreams",
        ],
        "Category": [
            "Commercial Execution",
            "High-Volume Delivery",
            "Conversion Support",
            "Enterprise Transformation",
            "Customer Research",
            "Stakeholder Research",
            "Operations Analytics",
            "Portfolio Breadth",
        ],
        "Impact Area": [
            "Revenue",
            "Execution",
            "Commercial",
            "Transformation",
            "Research",
            "Research",
            "Operations",
            "Breadth",
        ],
        "Scale": [90, 82, 76, 84, 72, 68, 70, 74],
        "x": [1.0, 2.1, 3.0, 4.0, 1.5, 2.7, 3.6, 4.5],
        "y": [3.0, 3.7, 2.6, 3.4, 1.6, 2.0, 1.4, 2.2],
    })

    fig = px.scatter(
        data,
        x="x",
        y="y",
        size="Scale",
        color="Impact Area",
        text="Proof Point",
        hover_name="Category",
        title="Commercial Proof Bubble Map",
        size_max=58,
    )

    fig.update_traces(
        textposition="middle center",
        textfont=dict(size=11, color="white"),
        marker=dict(line=dict(width=1.5, color="rgba(255,255,255,0.25)")),
    )

    fig.update_layout(
        height=520,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#d4d4d8",
        title_font_color="#ffffff",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        showlegend=True,
        legend=dict(orientation="h", y=-0.1),
        margin=dict(l=20, r=20, t=70, b=80),
    )

    return fig


def make_career_momentum_timeline():
    data = pd.DataFrame({
        "Year": [2019, 2021, 2024, 2025, 2026],
        "Stage": [
            "Clinical Operations",
            "EdTech Scale",
            "Startup Ownership",
            "Global Business Projects",
            "Analytics + Commercial Portfolio",
        ],
        "Narrative": [
            "Patient care, documentation and clinic coordination",
            "2,000+ sessions and performance-led delivery",
            "Turfo operations, revenue growth and stakeholder ownership",
            "Consulting projects across healthcare, transformation, AI and strategy",
            "Portfolio connecting analytics, growth, partnerships and execution",
        ],
        "Momentum": [1, 2, 3.2, 4.1, 4.8],
    })

    fig = px.line(
        data,
        x="Year",
        y="Momentum",
        markers=True,
        text="Stage",
        title="Career Momentum Timeline",
        hover_data=["Narrative"],
    )

    fig.update_traces(
        line=dict(color="#E53935", width=4),
        marker=dict(size=14, color="#FF6B6B", line=dict(width=2, color="#ffffff")),
        textposition="top center",
        textfont=dict(color="#ffffff", size=11),
    )

    fig.update_layout(
        height=440,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#d4d4d8",
        title_font_color="#ffffff",
        xaxis=dict(showgrid=False, title=""),
        yaxis=dict(visible=False),
        margin=dict(l=20, r=20, t=70, b=40),
    )

    return fig


def make_analytics_decision_funnel():
    stages = pd.DataFrame({
        "Stage": [
            "Business Question",
            "Data Layer",
            "Analysis / Modelling",
            "Insight",
            "Business Decision",
        ],
        "Value": [100, 86, 72, 58, 44],
        "Evidence": [
            "Pricing, utilisation, customer retention, adoption behaviour",
            "Trackers, survey data, transaction data, performance signals",
            "EDA, segmentation, regression, classification, SmartPLS",
            "Patterns, drivers, segments, risks and opportunities",
            "Pricing, targeting, utilisation, engagement and roadmap decisions",
        ],
    })

    fig = go.Figure(
        go.Funnel(
            y=stages["Stage"],
            x=stages["Value"],
            text=stages["Evidence"],
            textinfo="label+text",
            marker=dict(
                color=["#E53935", "#D83A3A", "#C94A4A", "#B85A5A", "#FF6B6B"],
                line=dict(width=1.5, color="rgba(255,255,255,0.25)"),
            ),
        )
    )

    fig.update_layout(
        title="Analytics Decision Funnel",
        height=520,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#ffffff",
        title_font_color="#ffffff",
        margin=dict(l=20, r=20, t=70, b=40),
    )

    return fig


def make_project_capability_heatmap():
    capability_groups = [
        "Healthcare",
        "Digital Transformation",
        "Commercial Strategy",
        "AI / Product",
        "Market Intelligence",
        "Operations",
    ]

    mapping = {
        "Bunk Station": [0, 0, 9, 0, 7, 8],
        "TrueLayer": [0, 8, 7, 5, 8, 6],
        "FinWise": [0, 6, 7, 9, 5, 6],
        "LM Instruments": [0, 9, 8, 4, 5, 9],
        "DP World": [0, 9, 6, 7, 7, 8],
        "Royal Dutch Clinic": [9, 4, 8, 0, 7, 8],
        "GSK": [9, 2, 9, 0, 9, 4],
        "Smart Hospitals": [9, 9, 6, 8, 7, 9],
        "Clinical Operations": [9, 2, 3, 0, 3, 9],
    }

    y_labels = []
    z = []

    for p in projects:
        short_name = p["title"].split("–")[0].strip()
        y_labels.append(short_name)
        z.append(mapping.get(short_name, [0, 0, 0, 0, 0, 0]))

    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            x=capability_groups,
            y=y_labels,
            colorscale=[[0, "#111113"], [0.3, "#4A0F0F"], [0.6, "#B71C1C"], [1, "#FF6B6B"]],
            colorbar=dict(title="Coverage"),
            zmin=0,
            zmax=9,
        )
    )

    fig.update_layout(
        title="Project-to-Capability Heatmap",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#d4d4d8",
        title_font_color="#ffffff",
        height=560,
        margin=dict(l=20, r=20, t=60, b=80),
    )

    return fig


def render_analytics_decision_engine():
    st.markdown('<div class="section-title">Analytics Decision Engine</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A process view of how I use analytics as a decision system from business question to action.</div>',
        unsafe_allow_html=True,
    )

    engine_steps = [
        {
            "step": "01",
            "title": "Frame the Business Question",
            "body": "Defined decision problems around pricing, utilisation, retention, adoption behaviour, performance improvement and market entry.",
            "proof": "TasteMate · Turfo · BYJU’S · GSK · AI Adoption Research",
        },
        {
            "step": "02",
            "title": "Build the Data Layer",
            "body": "Worked with transaction data, survey responses, dashboard inputs, operational trackers, performance signals and research model data.",
            "proof": "Excel trackers · Streamlit dashboards · SmartPLS outputs · Survey datasets",
        },
        {
            "step": "03",
            "title": "Model the Insight",
            "body": "Applied EDA, segmentation, regression, classification, clustering, association rules and statistical interpretation.",
            "proof": "Customer analytics · Spend modelling · Behavioural segmentation · Trust mediation model",
        },
        {
            "step": "04",
            "title": "Drive the Business Decision",
            "body": "Translated insights into pricing recommendations, utilisation planning, targeting logic, engagement improvement and operating model decisions.",
            "proof": "Revenue growth · Conversion support · Retention recommendations · Strategic roadmap",
        },
    ]

    cols = st.columns(4)
    for i, item in enumerate(engine_steps):
        with cols[i]:
            st.markdown(
                f"""
                <div class="fit-card" style="min-height: 330px;">
                    <div style="font-size:0.8rem; color:#FF6B6B; font-weight:950; letter-spacing:0.08em;">STEP {item["step"]}</div>
                    <h3>{item["title"]}</h3>
                    <p>{item["body"]}</p>
                    <div style="margin-top:1rem; padding-top:0.8rem; border-top:1px solid rgba(255,255,255,0.10); color:#a1a1aa; font-size:0.82rem;">
                        <b style="color:#ffffff;">Proof:</b><br>{item["proof"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_analytics_evidence_table():
    rows = [
        {"Method": "Dashboards", "Where demonstrated": "TasteMate, Turfo trackers, Streamlit portfolio"},
        {"Method": "EDA", "Where demonstrated": "TasteMate and customer/transaction analysis"},
        {"Method": "Regression", "Where demonstrated": "TasteMate average spend modelling"},
        {"Method": "Classification", "Where demonstrated": "TasteMate predictive analysis"},
        {"Method": "Clustering", "Where demonstrated": "TasteMate customer segmentation"},
        {"Method": "Association Rules", "Where demonstrated": "Meal combination insights"},
        {"Method": "KPI Tracking", "Where demonstrated": "Turfo utilisation/revenue, BYJU’S engagement"},
        {"Method": "Financial Modelling", "Where demonstrated": "GSK, LM Instruments, Bunk Station"},
        {"Method": "Research Modelling", "Where demonstrated": "AI Adoption Research using TPB, Trust Mediation and SmartPLS"},
    ]

    st.markdown('<div class="section-title">Analytics Evidence Map</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A grounded view of where each analytics method was applied across projects.</div>',
        unsafe_allow_html=True,
    )
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


def render_leadership_impact_matrix():
    st.markdown('<div class="section-title">Leadership Impact Map</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Leadership evidence mapped by ownership, stakeholder exposure and outcome.</div>',
        unsafe_allow_html=True,
    )

    rows = [
        {
            "Area": "Student Leadership",
            "Evidence": "Global Learning & Student Life Committee",
            "Ownership": "Cross-campus coordination, student engagement and student-faculty-admin communication",
            "Impact": "Strengthened collaboration and event participation across the cohort",
        },
        {
            "Area": "Industry Engagement",
            "Evidence": "Industry Connect Event, Dubai",
            "Ownership": "Supported coordination between students and senior business leaders",
            "Impact": "Improved exposure to real-world leadership and business decision-making",
        },
        {
            "Area": "Event Execution",
            "Evidence": "Business Conclave",
            "Ownership": "Supported presentation coordination, logistics and team communication",
            "Impact": "Enabled smoother delivery of student-led business presentations",
        },
        {
            "Area": "Healthcare Outreach",
            "Evidence": "OMFS Awareness Marathon",
            "Ownership": "Supported public healthcare awareness and registration/event coordination",
            "Impact": "Contributed to community-level awareness and outreach execution",
        },
        {
            "Area": "Public Health",
            "Evidence": "Anti-Tobacco Awareness Human Chain",
            "Ownership": "Participated in preventive health communication initiative",
            "Impact": "Supported public awareness around tobacco-related health risks",
        },
    ]

    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


def render_home():
    st.markdown(
        """
        <div class="hero-shell">
            <div class="hero-content">
                <div class="hero-grid">
                    <div class="hero-copy">
                        <div class="name-chip">Shalini Arun Prakash · Professional Portfolio</div>
                        <div class="hero-title">
                            I drive <span class="highlight-red">business growth</span><br>
                            through execution and data.
                        </div>
                        <div class="hero-subline">
                            Experience across startup operations, EdTech, analytics, customer engagement,
                            commercial execution and structured business problem solving.
                        </div>
                        <span class="badge badge-red">Revenue Growth</span>
                        <span class="badge badge-red">Commercial Execution</span>
                        <span class="badge badge-light-red">Data Analytics</span>
                        <span class="badge">Partnerships</span>
                        <span class="badge">Strategy</span>

                        <div class="hero-proof-strip">
                            <div class="hero-proof-pill">
                                <div class="hero-proof-value">3×</div>
                                <div class="hero-proof-label">Revenue Growth</div>
                            </div>
                            <div class="hero-proof-pill">
                                <div class="hero-proof-value">150+</div>
                                <div class="hero-proof-label">Monthly Conversions</div>
                            </div>
                            <div class="hero-proof-pill">
                                <div class="hero-proof-value">2,000+</div>
                                <div class="hero-proof-label">Live Sessions</div>
                            </div>
                        </div>
                    </div>

                    <div class="hero-profile-wrap">
                        <div class="hero-profile-stage">
                            <img src="assets/shalini-profile.png" class="hero-profile-img">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="hero-mini-card">
                <b>Execution Operator</b>
                <p>Startup operations, EdTech delivery and clinical coordination show ground-level ownership.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="hero-mini-card">
                <b>Business Problem Solver</b>
                <p>Consulting-style projects across healthcare, fintech, transformation and market strategy.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <div class="hero-mini-card">
                <b>Analytics + AI Builder</b>
                <p>Dashboards, modelling, research analytics and AI-enabled product/system thinking.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    cols = st.columns(4)
    for i, (value, label) in enumerate(metrics[:4]):
        with cols[i]:
            render_metric_card(value, label)

    cols = st.columns(4)
    for i, (value, label) in enumerate(metrics[4:]):
        with cols[i]:
            render_metric_card(value, label)

    st.markdown('<div class="section-title">Portfolio Fit</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A structured view of how my experience and project work connect across execution, commercial thinking, analytics, AI and stakeholder management.</div>',
        unsafe_allow_html=True,
    )

    for i in range(0, len(portfolio_fit_areas), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(portfolio_fit_areas):
                with col:
                    item = portfolio_fit_areas[i + j]
                    render_fit_card(item["area"], item["evidence"])

    st.markdown('<div class="section-title">Commercial Proof Map</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A proof-led visual showing measurable outcomes across execution, commercial growth, analytics and transformation.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="visual-card">', unsafe_allow_html=True)
    st.plotly_chart(make_commercial_proof_bubble_map(), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Career Momentum</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A visual progression from clinical operations to EdTech scale, startup ownership, global business projects and analytics-led commercial execution.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="visual-card">', unsafe_allow_html=True)
    st.plotly_chart(make_career_momentum_timeline(), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


def render_experience():
    st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Professional experience with role descriptions, visual context and achievement evidence under each experience.</div>',
        unsafe_allow_html=True,
    )

    for i in range(0, len(experience), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(experience):
                with col:
                    render_experience_card(experience[i + j])


def render_education():
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Reverse-chronology view of academic foundation across global business, medical cosmetology and clinical healthcare.</div>',
        unsafe_allow_html=True,
    )

    for item in education:
        with st.expander(
            f'{item["timeline"]} · {item["title"]}',
            expanded=item["title"].startswith("Global MBA"),
        ):
            c1, c2 = st.columns([0.9, 1.4])

            with c1:
                st.image(item["image"], use_container_width=True)

            with c2:
                st.markdown(f"### {item['title']}")
                st.markdown(f"**{item['period']}**")
                st.write(item["summary"])

                st.markdown("**Key highlights:**")
                for point in item["highlights"]:
                    st.write(f"• {point}")


def render_projects():
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Consulting-style and business project work across fintech, digital transformation, commercial strategy, AI-enabled models, market intelligence and healthcare transformation.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="background:#111113; border:1px solid rgba(255,255,255,0.12); border-top:4px solid #E53935; padding:1.2rem; margin-bottom:1.2rem;">
            <div style="font-size:0.78rem; color:#FF6B6B; font-weight:950; letter-spacing:0.08em; text-transform:uppercase;">
                Project Lens
            </div>
            <div style="margin-top:0.8rem;">
                <span class="badge badge-red">Commercial Strategy</span>
                <span class="badge badge-light-red">Digital Transformation</span>
                <span class="badge badge-red">AI & Analytics</span>
                <span class="badge badge-light-red">Healthcare / Life Sciences</span>
                <span class="badge">Operations</span>
                <span class="badge">Market Intelligence</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    capability_filter = st.selectbox(
        "Filter by capability",
        ["All"] + sorted(set([p["capability"] for p in projects])),
    )

    filtered = projects if capability_filter == "All" else [
        p for p in projects if p["capability"] == capability_filter
    ]

    st.write(f"Showing {len(filtered)} project(s).")

    for i in range(0, len(filtered), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(filtered):
                with col:
                    render_project_card(filtered[i + j])


def render_analytics():
    st.markdown('<div class="section-title">Data Analytics & Business Intelligence</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A dedicated section for dashboarding, KPI ownership, customer analytics, predictive modelling, research analytics and data-driven decision support.</div>',
        unsafe_allow_html=True,
    )

    render_image_banner(
        "Analytics as Decision Support",
        "My analytics work is positioned around business problem framing, dashboard ownership, performance visibility, modelling and recommendations — not just reporting.",
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1800&q=90",
    )

    analytics_cards = [
        {
            "area": "Decision intelligence",
            "evidence": "Framed analytics projects around business choices: pricing, utilisation, spend behaviour, segmentation, retention and operational performance.",
        },
        {
            "area": "Dashboard ownership",
            "evidence": "Built trackers and dashboard structures that made performance visible across bookings, utilisation, revenue, engagement and model outputs.",
        },
        {
            "area": "Customer analytics",
            "evidence": "Used segmentation, behaviour patterns, spend modelling and association rules to move beyond reporting into actionable commercial insight.",
        },
        {
            "area": "Research analytics",
            "evidence": "Designed and interpreted AI adoption analysis using TPB, trust mediation, SmartPLS outputs and evidence-backed reasoning.",
        },
    ]

    for i in range(0, len(analytics_cards), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(analytics_cards):
                item = analytics_cards[i + j]
                with col:
                    render_fit_card(item["area"], item["evidence"])

    st.markdown('<div class="section-title">Analytics Decision Funnel</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A visual funnel showing how analytics moves from business question to actionable decision.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="visual-card">', unsafe_allow_html=True)
    st.plotly_chart(make_analytics_decision_funnel(), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    render_analytics_decision_engine()

    st.markdown('<div class="section-title">Analytics Business Impact</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Business outcomes supported through analytics, dashboarding and modelling work.</div>',
        unsafe_allow_html=True,
    )

    impact_cards = [
        {
            "area": "Revenue & Utilisation Decisions",
            "evidence": "Used Turfo trackers to monitor bookings, utilisation and revenue trends, supporting pricing and slot optimisation decisions.",
        },
        {
            "area": "Customer Segmentation & Targeting",
            "evidence": "Applied segmentation and customer behaviour analysis in TasteMate to support retention, pricing and campaign recommendations.",
        },
        {
            "area": "Performance Improvement",
            "evidence": "Used learner engagement and performance signals at BYJU’S to support improved delivery quality and conversion-oriented outcomes.",
        },
        {
            "area": "Research-Based Decision Support",
            "evidence": "Interpreted AI adoption research outputs using TPB, trust mediation and SmartPLS to connect behavioural drivers with adoption strategy.",
        },
    ]

    for i in range(0, len(impact_cards), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(impact_cards):
                item = impact_cards[i + j]
                with col:
                    render_fit_card(item["area"], item["evidence"])

    render_analytics_evidence_table()

    st.markdown('<div class="section-title">Analytics Project Evidence</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Analytics evidence is separated from the main Projects tab to make dashboarding, modelling and BI ownership visible on its own.</div>',
        unsafe_allow_html=True,
    )

    for i in range(0, len(analytics_projects), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(analytics_projects):
                with col:
                    render_project_card(analytics_projects[i + j])


def render_skills():
    st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A visual capability map showing what I can do, where it was demonstrated, and the tools or methods behind it.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="skill-strip">
            <div class="skill-strip-item">Business Ownership</div>
            <div class="skill-strip-item">Strategy</div>
            <div class="skill-strip-item">Data Analytics</div>
            <div class="skill-strip-item">AI-Enabled Workflows</div>
            <div class="skill-strip-item">Commercial Execution</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    skill_items = list(skills.items())

    for i in range(0, len(skill_items), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(skill_items):
                category, items = skill_items[i + j]
                chips = "".join([f'<span class="skill-item">{item}</span>' for item in items])
                evidence = skill_notes.get(category, {}).get("evidence", "")
                methods = skill_notes.get(category, {}).get("methods", "")
                image = skills_visuals.get(category, {}).get(
                    "image",
                    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1400&q=85",
                )
                headline = skills_visuals.get(category, {}).get("headline", "")

                with col:
                    st.markdown(
                        f"""
                        <div class="skill-visual-card">
                            <img src="{image}" class="skill-visual-img">
                            <div class="skill-visual-body">
                                <div class="skill-visual-title">{category}</div>
                                <div class="project-summary">{headline}</div>
                                <div>{chips}</div>
                                <div class="skill-visual-evidence"><b>Evidence:</b> {evidence}</div>
                                <div class="skill-visual-methods"><b>Methods / Tools:</b> {methods}</div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

    st.markdown('<div class="section-title">Project-to-Capability Map</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A visual map connecting project evidence to capability areas across healthcare, digital transformation, commercial strategy, AI, market intelligence and operations.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="visual-card">', unsafe_allow_html=True)
    st.plotly_chart(make_project_capability_heatmap(), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    mapping_data = []
    for p in projects:
        mapping_data.append(
            {
                "Project": p["title"],
                "Capability": p["capability"],
                "Frameworks": ", ".join(p["frameworks"]),
                "Tools": ", ".join(p["tools"]),
                "Relevance": p["strategic_relevance"],
            }
        )

    st.dataframe(pd.DataFrame(mapping_data), use_container_width=True, hide_index=True)


def render_leadership():
    st.markdown('<div class="section-title">Leadership & Community</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Leadership, public health outreach, student engagement, professional events and extra-curricular strengths presented as evidence of initiative and presence.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">Leadership & Volunteer Work</div>', unsafe_allow_html=True)

    for i in range(0, len(leadership_items), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(leadership_items):
                with col:
                    render_simple_visual_card(leadership_items[i + j])

    render_leadership_impact_matrix()

    st.markdown('<div class="section-title">Extra-Curricular Strengths</div>', unsafe_allow_html=True)

    for i in range(0, len(extra_curricular_items), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(extra_curricular_items):
                with col:
                    render_simple_visual_card(extra_curricular_items[i + j])


def render_proof_points():
    st.markdown('<div class="section-title">Proof Points</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Numbers and evidence that support execution discipline, analytics capability, business ownership and project impact.</div>',
        unsafe_allow_html=True,
    )

    render_image_banner(
        "Evidence of Ownership and Impact",
        "The proof points below bring together measurable outcomes across revenue growth, live delivery, conversion contribution, research, analytics and transformation work.",
        "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=1800&q=90",
    )

    proof_points = [
        ("3×", "Revenue growth at Turfo in 8 months"),
        ("35+", "Weekly engagements managed through operating execution"),
        ("150+", "Monthly conversions contributed through BYJU’S engagement insights"),
        ("2,000+", "Live sessions delivered in high-volume performance environment"),
        ("$3.5M", "Commercial proposal structured for enterprise transformation"),
        ("40%", "Commercial margin logic structured in transformation project"),
        ("100+", "Primary research responses for growth strategy work"),
        ("10+", "Expert / stakeholder interviews for transformation research"),
        ("14+", "Projects and analytics workstreams mapped to portfolio capabilities"),
        ("60%", "Approximate utilisation level achieved through Turfo operating analytics"),
        ("Global", "Dubai, Singapore, UAE, India and cross-market business project exposure"),
        ("Multi-domain", "Fintech, healthcare, EdTech, F&B, logistics and enterprise transformation"),
    ]

    for i in range(0, len(proof_points), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(proof_points):
                with col:
                    render_metric_card(proof_points[i + j][0], proof_points[i + j][1])


def render_contact():
    st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Professional contact and portfolio access details.</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1.2, 1])

    with c1:
        st.markdown(
            """
            <div class="contact-card">
                <h3>Shalini Arun Prakash</h3>
                <p><b>Portfolio Focus:</b> Digital Transformation · Data Analytics · Business Projects · AI-Enabled Business Models · Commercial Execution</p>
                <p><b>Location:</b> India</p>
                <p><b>Email:</b> shaliniarun23@gmail.com</p>
                <p><b>LinkedIn:</b> linkedin.com/in/shaliniarun</p>
                <br>
                <p><b>Professional narrative:</b> Business professional with EdTech, startup operations, analytics, AI-enabled project work, healthcare exposure and global MBA experience.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="contact-card">
                <h3>Portfolio Use</h3>
                <p>This portfolio maps experience, education, projects, analytics work, leadership and community engagement into a single professional profile.</p>
                <p>It is public-safe and does not expose confidential project documents, raw datasets or private submissions.</p>
                <br>
                <p><b>Full reports and confidential project documents are available only on request.</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )


st.markdown(
    """
    <div style="padding: 0.9rem 0 1.4rem 0; border-bottom:1px solid rgba(255,255,255,0.10); margin-bottom:1rem;">
        <div style="font-size: 1.75rem; font-weight: 950; color: #ffffff; text-transform: uppercase; letter-spacing:-0.03em;">
            Shalini Arun Prakash
        </div>
        <div style="color:#a1a1aa; margin-top:0.35rem; font-size:0.95rem;">
            Digital Transformation · Data Analytics · AI-Enabled Business Models · Commercial Execution · Strategy
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

tab_home, tab_experience, tab_education, tab_projects, tab_analytics, tab_skills, tab_leadership, tab_proof, tab_contact = st.tabs(
    ["Home", "Experience", "Education", "Projects", "Analytics", "Skills", "Leadership", "Proof Points", "Contact"]
)

with tab_home:
    render_home()

with tab_experience:
    render_experience()

with tab_education:
    render_education()

with tab_projects:
    render_projects()

with tab_analytics:
    render_analytics()

with tab_skills:
    render_skills()

with tab_leadership:
    render_leadership()

with tab_proof:
    render_proof_points()

with tab_contact:
    render_contact()

st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; color:#a1a1aa; font-size:0.86rem;">
        Designed as a public-safe professional portfolio. Detailed reports and confidential documents available only on request.
    </div>
    """,
    unsafe_allow_html=True,
)
