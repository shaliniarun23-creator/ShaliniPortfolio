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

# ---------------- CSS ----------------
st.markdown(
    """
.profile-panel img {
    max-height: 540px;
    object-fit: contain;
    margin-top: -10px;
}
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 0% 0%, rgba(229, 57, 53, 0.18), transparent 30%),
        radial-gradient(circle at 100% 10%, rgba(255, 107, 107, 0.08), transparent 25%),
        linear-gradient(135deg, #050505 0%, #0b0b0d 50%, #111111 100%);
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

h1, h2, h3, h4, h5 {
    color: #ffffff !important;
    letter-spacing: -0.035em;
}

p, li, span, div {
    color: #e5e5e5;
}

.top-header {
    padding: 0.9rem 0 1.4rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.10);
    margin-bottom: 1rem;
}

.top-name {
    font-size: 1.75rem;
    font-weight: 950;
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: -0.03em;
}

.top-subtitle {
    color: #a1a1aa;
    margin-top: 0.35rem;
    font-size: 0.95rem;
}

.hero-box {
    min-height: 620px;
    background:
        radial-gradient(circle at 85% 20%, rgba(229,57,53,0.20), transparent 30%),
        radial-gradient(circle at 0% 0%, rgba(229,57,53,0.14), transparent 35%),
        linear-gradient(135deg, #050505 0%, #0b0b0d 58%, #121212 100%);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 35px 100px rgba(0,0,0,0.65);
    padding: 4.2rem 4rem;
    margin-bottom: 1.2rem;
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
    font-size: clamp(2.6rem, 4.4vw, 4.6rem);
    line-height: 0.98;
    font-weight: 950;
    color: #ffffff;
    margin-bottom: 1.25rem;
    text-shadow: 0 14px 45px rgba(0,0,0,0.55);
    text-transform: uppercase;
}

.highlight-red {
    color: #E53935;
    -webkit-text-fill-color: #E53935;
}

.hero-subline {
    font-size: 1.06rem;
    line-height: 1.75;
    max-width: 760px;
    color: #d4d4d8;
    margin-bottom: 1.6rem;
}

.profile-panel {
    background:
        radial-gradient(circle at 50% 35%, rgba(229,57,53,0.26), transparent 55%),
        linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.01));
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 35px 90px rgba(0,0,0,0.55);
    padding: 0.5rem 1.2rem 0 1.2rem;
    min-height: 540px;
    display: flex;
    align-items: flex-start;
    justify-content: center;
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
    background: rgba(229,57,53,0.14);
    color: #ffffff;
    border: 1px solid rgba(229,57,53,0.42);
}

.badge-light-red {
    background: rgba(255,107,107,0.09);
    color: #ffffff;
    border: 1px solid rgba(255,107,107,0.32);
}

.section-title {
    font-size: 2.25rem;
    font-weight: 950;
    color: #ffffff;
    margin-top: 3rem;
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

.metric-card,
.fit-card,
.visual-card,
.content-card,
.contact-card {
    background: #111113;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 18px 50px rgba(0,0,0,0.35);
    margin-bottom: 1rem;
}

.metric-card {
    position: relative;
    overflow: hidden;
    padding: 1.35rem;
    min-height: 150px;
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
}

.fit-card {
    border-top: 4px solid #E53935;
    padding: 1.25rem;
    min-height: 210px;
}

.fit-card h3 {
    text-transform: uppercase;
    font-size: 1.05rem;
    margin-bottom: 0.65rem;
}

.fit-card p {
    color: #d4d4d8;
    font-size: 0.92rem;
    line-height: 1.55;
}

.visual-card {
    border-top: 4px solid #E53935;
    padding: 1.2rem;
}

.content-card {
    overflow: hidden;
    padding: 0;
}

.card-body {
    padding: 1.35rem 1.45rem 1.5rem 1.45rem;
}

.card-title {
    font-size: 1.28rem;
    line-height: 1.18;
    font-weight: 950;
    color: #ffffff;
    margin-bottom: 0.45rem;
    text-transform: uppercase;
}

.card-meta {
    font-size: 0.82rem;
    color: #FF6B6B;
    font-weight: 850;
    margin-bottom: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}

.card-summary {
    font-size: 0.96rem;
    color: #d4d4d8;
    line-height: 1.6;
    margin-bottom: 0.85rem;
}

.hero-mini-card {
    padding: 1rem;
    background: rgba(17,17,19,0.88);
    border: 1px solid rgba(255,255,255,0.10);
    border-left: 4px solid #E53935;
    min-height: 135px;
    margin-bottom: 1rem;
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

.relevance-box {
    background: rgba(229,57,53,0.10);
    border-left: 4px solid #E53935;
    padding: 1rem;
    margin-top: 1rem;
    color: #ffffff;
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
    padding: 1.6rem;
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

hr {
    border: none;
    height: 1px;
    background: rgba(255,255,255,0.12);
    margin: 2rem 0;
}

@media (max-width: 900px) {
.hero-box {
    min-height: 540px;
    background:
        radial-gradient(circle at 85% 20%, rgba(229,57,53,0.20), transparent 30%),
        radial-gradient(circle at 0% 0%, rgba(229,57,53,0.14), transparent 35%),
        linear-gradient(135deg, #050505 0%, #0b0b0d 58%, #121212 100%);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 35px 100px rgba(0,0,0,0.65);
    padding: 4.2rem 4rem;
    margin-bottom: 1.2rem;
}


# ---------------- HELPERS ----------------
def render_badges(items, style="badge"):
    html = "".join([f'<span class="{style}">{item}</span>' for item in items])
    st.markdown(html, unsafe_allow_html=True)


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


def render_content_card(title, meta, summary, image_url=None):
    st.markdown('<div class="content-card">', unsafe_allow_html=True)

    if image_url:
        st.image(image_url, use_container_width=True)

    st.markdown(
        f"""
        <div class="card-body">
            <div class="card-title">{title}</div>
            <div class="card-meta">{meta}</div>
            <div class="card-summary">{summary}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)


def render_project_card(project):
    render_content_card(
        project["title"],
        f'{project["capability"]} - {project["location"]}',
        project["summary"],
        project.get("image"),
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
    render_content_card(
        item["title"],
        item["period"],
        item["description"],
        item.get("image"),
    )

    st.markdown("**Achievements:**")
    for achievement in item["achievements"]:
        st.write(f"• {achievement}")


def render_simple_visual_card(item):
    render_content_card(
        item["title"],
        f'{item.get("category", "Extra-Curricular")} - {item.get("location", "")}',
        item["summary"],
        item.get("image"),
    )
    render_badges(item["skills"], "skill-item")


# ---------------- CHARTS ----------------
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


# ---------------- SECTIONS ----------------
def render_home():
    left, right = st.columns([1.35, 0.85])

    with left:
        st.markdown(
            """
            <div class="hero-box">
                <div class="name-chip">Shalini Arun Prakash - Professional Portfolio</div>
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
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown('<div class="profile-panel">', unsafe_allow_html=True)
        st.image("assets/shalini-profile.png", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

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
    st.plotly_chart(make_commercial_proof_bubble_map(), use_container_width=True)

    st.markdown('<div class="section-title">Career Momentum</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A visual progression from clinical operations to EdTech scale, startup ownership, global business projects and analytics-led commercial execution.</div>',
        unsafe_allow_html=True,
    )
    st.plotly_chart(make_career_momentum_timeline(), use_container_width=True)


def render_experience():
    st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Professional experience with role descriptions and achievement evidence.</div>',
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
            f'{item["timeline"]} - {item["title"]}',
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


def render_analytics_decision_engine():
    st.markdown('<div class="section-title">Analytics Decision Engine</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A process view of how analytics moves from business question to decision.</div>',
        unsafe_allow_html=True,
    )

    engine_steps = [
        ("01", "Frame the Business Question", "Pricing, utilisation, retention, adoption behaviour and market entry."),
        ("02", "Build the Data Layer", "Survey data, trackers, transaction data, dashboard inputs and research data."),
        ("03", "Model the Insight", "EDA, segmentation, regression, classification, clustering and statistical interpretation."),
        ("04", "Drive the Decision", "Pricing, targeting, utilisation, engagement and roadmap recommendations."),
    ]

    cols = st.columns(4)
    for i, (step, title, body) in enumerate(engine_steps):
        with cols[i]:
            render_fit_card(f"Step {step}: {title}", body)


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
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


def render_analytics():
    st.markdown('<div class="section-title">Data Analytics & Business Intelligence</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Dashboarding, KPI ownership, customer analytics, predictive modelling, research analytics and decision support.</div>',
        unsafe_allow_html=True,
    )

    analytics_cards = [
        ("Decision Intelligence", "Framed analytics projects around pricing, utilisation, spend behaviour, segmentation and market entry."),
        ("Dashboard Ownership", "Built trackers and dashboards for bookings, utilisation, revenue, engagement and model outputs."),
        ("Customer Analytics", "Used segmentation, behaviour patterns, spend modelling and association rules."),
        ("Research Analytics", "Designed and interpreted AI adoption analysis using TPB, trust mediation and SmartPLS."),
    ]

    for i in range(0, len(analytics_cards), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(analytics_cards):
                with col:
                    render_fit_card(analytics_cards[i + j][0], analytics_cards[i + j][1])

    st.plotly_chart(make_analytics_decision_funnel(), use_container_width=True)
    render_analytics_decision_engine()
    render_analytics_evidence_table()

    st.markdown('<div class="section-title">Analytics Project Evidence</div>', unsafe_allow_html=True)

    for i in range(0, len(analytics_projects), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(analytics_projects):
                with col:
                    render_project_card(analytics_projects[i + j])


def render_skills():
    st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Capability map showing what I can do, where it was demonstrated, and tools behind it.</div>',
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
                evidence = skill_notes.get(category, {}).get("evidence", "")
                methods = skill_notes.get(category, {}).get("methods", "")
                image = skills_visuals.get(category, {}).get("image", None)
                headline = skills_visuals.get(category, {}).get("headline", "")

                with col:
                    render_content_card(category, headline, evidence, image)
                    render_badges(items, "skill-item")
                    st.caption(methods)

    st.plotly_chart(make_project_capability_heatmap(), use_container_width=True)


def render_leadership_impact_matrix():
    rows = [
        {
            "Area": "Student Leadership",
            "Evidence": "Global Learning & Student Life Committee",
            "Ownership": "Cross-campus coordination and student-faculty-admin communication",
            "Impact": "Strengthened collaboration and engagement",
        },
        {
            "Area": "Industry Engagement",
            "Evidence": "Industry Connect Event, Dubai",
            "Ownership": "Supported coordination between students and senior business leaders",
            "Impact": "Improved exposure to real-world leadership",
        },
        {
            "Area": "Event Execution",
            "Evidence": "Business Conclave",
            "Ownership": "Presentation coordination, logistics and team communication",
            "Impact": "Enabled smoother delivery of student-led presentations",
        },
        {
            "Area": "Healthcare Outreach",
            "Evidence": "OMFS Awareness Marathon",
            "Ownership": "Public healthcare awareness and registration coordination",
            "Impact": "Contributed to community outreach",
        },
        {
            "Area": "Public Health",
            "Evidence": "Anti-Tobacco Awareness Human Chain",
            "Ownership": "Preventive health communication initiative",
            "Impact": "Supported public health awareness",
        },
    ]

    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


def render_leadership():
    st.markdown('<div class="section-title">Leadership & Community</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Leadership, public health outreach, student engagement and extra-curricular strengths.</div>',
        unsafe_allow_html=True,
    )

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
        '<div class="section-caption">Numbers and evidence supporting execution discipline, analytics capability, ownership and project impact.</div>',
        unsafe_allow_html=True,
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
                <p><b>Portfolio Focus:</b> Digital Transformation - Data Analytics - Business Projects - AI-Enabled Business Models - Commercial Execution</p>
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


# ---------------- APP HEADER ----------------
st.markdown(
    """
    <div class="top-header">
        <div class="top-name">Shalini Arun Prakash</div>
        <div class="top-subtitle">
            Digital Transformation - Data Analytics - AI-Enabled Business Models - Commercial Execution - Strategy
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------- TABS ----------------
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
