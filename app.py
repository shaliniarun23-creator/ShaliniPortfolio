import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------

st.set_page_config(
    page_title="Shalini Arun Prakash | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------------------
# CSS
# ------------------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 0% 0%, rgba(229, 57, 53, 0.18), transparent 30%),
        radial-gradient(circle at 100% 10%, rgba(229, 57, 53, 0.10), transparent 25%),
        linear-gradient(135deg, #050505 0%, #0b0b0d 48%, #111111 100%);
    color: #ffffff;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

[data-testid="stSidebar"] {
    display: none;
}

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
    border-radius: 0px;
    min-height: 650px;
    background:
        linear-gradient(90deg, rgba(0,0,0,0.98), rgba(0,0,0,0.88), rgba(0,0,0,0.46)),
        url('https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1800&q=90');
    background-size: cover;
    background-position: center;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 35px 100px rgba(0,0,0,0.65);
    margin-bottom: 1.2rem;
}

.hero-content {
    max-width: 1110px;
    padding: 4.2rem 4rem 3.2rem 4rem;
}

.name-chip {
    display: inline-flex;
    padding: 0.65rem 1.05rem;
    border-radius: 2px;
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
    max-width: 910px;
    color: #d4d4d8;
    margin-bottom: 1.6rem;
}

.hero-mini-card {
    padding: 1rem;
    border-radius: 0px;
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

.badge {
    display: inline-block;
    padding: 0.48rem 0.85rem;
    margin: 0.24rem 0.28rem 0.24rem 0;
    border-radius: 0px;
    background: rgba(255,255,255,0.06);
    color: #f5f5f5;
    border: 1px solid rgba(255,255,255,0.14);
    font-size: 0.78rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

.badge-red {
    background: rgba(229,57,53,0.12);
    color: #ffffff;
    border: 1px solid rgba(229,57,53,0.55);
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
    border-radius: 0px;
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
}

.project-card {
    overflow: hidden;
    background: #111113;
    border: 1px solid rgba(255,255,255,0.11);
    border-radius: 0px;
    padding: 0;
    margin-bottom: 1.25rem;
    box-shadow: 0 20px 62px rgba(0, 0, 0, 0.35);
    transition: all 0.22s ease-in-out;
}

.project-card:hover,
.metric-card:hover,
.fit-card:hover,
.visual-card:hover,
.skill-visual-card:hover {
    transform: translateY(-3px);
    transition: all 0.22s ease-in-out;
    border-color: rgba(229,57,53,0.42);
    box-shadow: 0 24px 70px rgba(0,0,0,0.48);
}

.project-img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    border-bottom: 4px solid #E53935;
    opacity: 0.90;
    filter: grayscale(22%) contrast(1.08);
}

.experience-img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-bottom: 4px solid #E53935;
    opacity: 0.90;
    filter: grayscale(20%) contrast(1.08);
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
    color: #ff6b6b;
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
    color: #ff6b6b;
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

/* ---------- PREMIUM SKILLS IMAGE CARDS ---------- */

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
    filter: grayscale(20%) contrast(1.08);
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
    border: 1px solid rgba(229,57,53,0.45);
    background: rgba(229,57,53,0.10);
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
    border-radius: 0px;
    padding: 1.6rem;
    box-shadow: 0 22px 60px rgba(0,0,0,0.36);
    min-height: 300px;
    border-top: 5px solid #E53935;
}

div[data-testid="stExpander"] {
    background: #111113;
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 0px;
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
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# CORE DATA
# ------------------------------------------------------------

metrics = [
    ("3×", "Revenue growth achieved through startup operations and commercialization"),
    ("2,000+", "Live learning sessions delivered in a high-volume EdTech environment"),
    ("150+", "Monthly conversions contributed through engagement and performance insights"),
    ("$3.5M", "Commercial proposal structured for enterprise transformation"),
    ("100+", "Primary research responses used for market and customer insight"),
    ("10+", "Expert / stakeholder interviews across transformation research"),
    ("14+", "Projects and analytics workstreams across strategy, operations, AI and BI"),
    ("5+", "Years across healthcare, EdTech, startup operations and business projects"),
]

portfolio_fit_areas = [
    {
        "area": "Business ownership & execution",
        "evidence": "Turfo operating ownership, BYJU’S high-volume delivery, clinical care coordination and MBA transformation projects."
    },
    {
        "area": "Commercial thinking",
        "evidence": "Bunk Station turnaround logic, GSK market entry model, Royal Dutch growth strategy and enterprise proposal work."
    },
    {
        "area": "Data analytics & BI",
        "evidence": "TasteMate analytics dashboard, Turfo revenue/utilisation trackers, BYJU’S performance insights and AI adoption modelling."
    },
    {
        "area": "AI-powered business models",
        "evidence": "FinWise AI-enabled MVP, Smart Hospitals digital transformation, AI adoption research and workflow automation thinking."
    },
    {
        "area": "Stakeholder activation",
        "evidence": "Learning experience design, patient/customer journey mapping, expert interviews, partner/vendor coordination and event leadership."
    },
    {
        "area": "Market intelligence",
        "evidence": "GSK oncology market assessment, TrueLayer open banking analysis, DP World ecosystem strategy and healthcare growth research."
    },
]
projects = [
    {
        "title": "Bunk Station – Strategic Turnaround & Investment Roadmap",
        "capability": "Commercial Strategy & Unit Economics",
        "location": "Dubai",
        "context": "Live consulting-style F&B turnaround project",
        "image": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1400&q=85",
        "summary": "Developed a strategic turnaround plan by diagnosing market demand, customer segments, branding gaps, operational inefficiency and revenue growth opportunities.",
        "problem": "Bunk Station had strong fundamentals such as best-selling SKUs and a student customer base, but weak visibility, poor ratings, branding gaps and operational inefficiency.",
        "role": "Conducted business diagnosis and recommended an investment-led repositioning strategy instead of maintaining status quo or shutting down.",
        "approach": [
            "Analysed DIAC student market demand and customer personas.",
            "Reviewed brand positioning, menu architecture, operations and competitive context.",
            "Identified bottlenecks around visibility, service speed and revenue conversion.",
            "Developed a turnaround roadmap covering menu engineering, combo pricing, QR ordering, loyalty programs and KPI tracking."
        ],
        "frameworks": ["Turnaround Strategy", "Customer Persona", "Menu Engineering", "KPI Tracking", "Investment Decision"],
        "tools": ["PowerPoint", "Market analysis", "Primary research", "Financial logic"],
        "outputs": [
            "Strategic turnaround recommendation.",
            "Investment-led repositioning plan.",
            "Menu and combo pricing strategy.",
            "QR-based ordering and KPI roadmap.",
            "Revenue growth and operating efficiency logic."
        ],
        "strategic_relevance": "Strong evidence of commercial diagnosis, growth planning, KPI thinking, customer acquisition and operating improvement."
    },
    {
        "title": "TrueLayer – Open Banking Strategy & Ecosystem Assessment",
        "capability": "Ecosystem Development",
        "location": "Dubai",
        "context": "Enterprise Innovation & Digital Transformation case analysis",
        "image": "https://images.unsplash.com/photo-1559526324-593bc073d938?auto=format&fit=crop&w=1400&q=85",
        "summary": "Assessed TrueLayer’s open banking platform by analysing how regulation, APIs and ecosystem partnerships enable fintech innovation and competitive advantage.",
        "problem": "Open banking platforms must balance regulation, trust, API infrastructure, ecosystem partnerships and market readiness to scale effectively.",
        "role": "Conducted a strategic assessment of TrueLayer’s platform model, regulatory context and expansion opportunities.",
        "approach": [
            "Analysed PSD2, API infrastructure and open banking regulation.",
            "Evaluated market expansion opportunities using readiness and demand criteria.",
            "Assessed operating model capabilities such as compliance agility, scalability and ecosystem integration.",
            "Linked platform strategy to financial services business model innovation."
        ],
        "frameworks": ["Platform Strategy", "Open Banking", "API Ecosystem", "Regulatory Strategy", "Market Expansion"],
        "tools": ["Case analysis", "PowerPoint", "Strategic frameworks", "Secondary research"],
        "outputs": [
            "Open banking strategy assessment.",
            "Market expansion prioritisation logic.",
            "Operating model capability review.",
            "Ecosystem partnership analysis."
        ],
        "strategic_relevance": "Relevant to ecosystem development, platform partnerships, regulated fintech analysis, market readiness and expansion logic."
    },
    {
        "title": "FinWise – AI-Powered Financial Literacy Platform",
        "capability": "AI-Powered Business Models",
        "location": "UAE",
        "context": "AI-enabled B2B2C education/product strategy",
        "image": "https://images.unsplash.com/photo-1516321497487-e288fb19713f?auto=format&fit=crop&w=1400&q=85",
        "summary": "Designed a scalable AI-enabled financial literacy model for students, parents, schools and CSR partners with structured learning journeys and implementation logic.",
        "problem": "Financial literacy gaps among school-aged learners are driven by curriculum gaps, behavioural gaps, parental engagement gaps and system constraints.",
        "role": "Structured the product concept, stakeholder model, MVP logic, journey maps, service blueprint and scale roadmap.",
        "approach": [
            "Defined target stakeholders: students, parents, schools and sponsors.",
            "Mapped learning journeys and behavioural reinforcement logic.",
            "Structured B2B2C operating model and partner-led rollout.",
            "Developed TOWS, service blueprint and governance logic."
        ],
        "frameworks": ["TOWS", "Service Blueprint", "Customer Journey", "B2B2C Model", "MVP Design"],
        "tools": ["PowerPoint", "AI tools", "Business model design", "Journey mapping"],
        "outputs": [
            "AI-enabled MVP structure.",
            "Student-parent-school journey map.",
            "Service blueprint.",
            "3-year scale roadmap."
        ],
        "strategic_relevance": "Shows AI-enabled workflow thinking, stakeholder ecosystems, onboarding journeys and scalable operating model design."
    },
    {
        "title": "LM Instruments – SAP S/4HANA Transformation Strategy",
        "capability": "Enterprise Transformation",
        "location": "Dubai",
        "context": "SAP transformation RFP and commercial model",
        "image": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1400&q=85",
        "summary": "Structured AS-IS / TO-BE workflows, SAP-aligned operating blueprints, data migration logic and commercial proposal for enterprise transformation.",
        "problem": "Enterprise transformation requires clear process design, data readiness, governance, cost logic and implementation sequencing across functions.",
        "role": "Mapped business requirements, process dependencies, data entities and commercial proposal logic.",
        "approach": [
            "Structured AS-IS and TO-BE workflows across enterprise functions.",
            "Translated business inputs into SAP-aligned process blueprints.",
            "Defined data migration and validation logic across critical entities.",
            "Built commercial model with cost, margin and governance assumptions."
        ],
        "frameworks": ["AS-IS / TO-BE", "RFP Response", "Operating Blueprint", "Governance Model"],
        "tools": ["Excel", "PowerPoint", "Process mapping", "Cost modelling"],
        "outputs": [
            "5+ enterprise workflow maps.",
            "SAP-aligned operating blueprint.",
            "Data validation logic across 6+ entities.",
            "$3.5M commercial proposal with margin logic."
        ],
        "strategic_relevance": "Shows structured process thinking, data workflow design, governance and commercial model discipline."
    },
    {
        "title": "DP World – Digital Trade & Supply Chain Transformation",
        "capability": "Digital Transformation",
        "location": "Dubai",
        "context": "Emerging technology strategy project",
        "image": "https://images.unsplash.com/photo-1494412651409-8963ce7935a7?auto=format&fit=crop&w=1400&q=85",
        "summary": "Assessed how AI, blockchain, AR/VR and drones can improve trade visibility, logistics efficiency, documentation speed and operational resilience.",
        "problem": "Trade and logistics ecosystems face inefficiencies across documentation, customs, visibility, yard planning and asset monitoring.",
        "role": "Conducted use-case analysis, operating model assessment and technology-to-business-impact mapping.",
        "approach": [
            "Assessed emerging technology use cases across trade operations.",
            "Mapped impact across customs, cargo visibility, workforce enablement and asset monitoring.",
            "Linked automation and digital workflows to operational throughput and documentation improvements.",
            "Structured recommendations around efficiency, trust and resilience."
        ],
        "frameworks": ["Emerging Tech Strategy", "Use-Case Prioritisation", "Operating Model", "Digital Trade Ecosystem"],
        "tools": ["PowerPoint", "Research synthesis", "Benchmarking", "Process analysis"],
        "outputs": [
            "Emerging technology use-case map.",
            "Digital trade ecosystem assessment.",
            "Operational improvement logic.",
            "Strategic recommendation deck."
        ],
        "strategic_relevance": "Relevant for global ecosystem thinking, emerging technology, operational visibility and cross-border commercial environments."
    },
    {
        "title": "Royal Dutch Clinic – Growth Strategy & Operating Model Analysis",
        "capability": "Healthcare Growth Strategy",
        "location": "UAE",
        "context": "Healthcare growth and operating model project",
        "image": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=1400&q=85",
        "summary": "Assessed growth potential, patient journey, referral pathways, pricing sensitivity and operational bottlenecks for a premium healthcare services context.",
        "problem": "Healthcare service growth can be constrained by unclear patient acquisition pathways, pricing friction, operational bottlenecks and inconsistent service conversion.",
        "role": "Supported market and operational analysis using primary research, benchmarking and patient journey assessment.",
        "approach": [
            "Analysed patient journey and inquiry-to-appointment funnel.",
            "Reviewed referral pathways and competitive healthcare landscape.",
            "Used 100+ primary research responses for demand and pricing insights.",
            "Recommended service, pricing and operating model improvements."
        ],
        "frameworks": ["Patient Journey Mapping", "Operating Model", "Growth Strategy", "Customer Insight"],
        "tools": ["Excel", "Survey analysis", "PowerPoint", "Benchmarking"],
        "outputs": [
            "Growth strategy recommendations.",
            "Patient funnel and service workflow insights.",
            "Pricing and demand observations.",
            "Operating model improvement priorities."
        ],
        "strategic_relevance": "Shows customer acquisition logic, stakeholder mapping, service conversion thinking and operating model improvement."
    },
    {
        "title": "GSK – U.S. Oncology Market Entry & Commercial Strategy",
        "capability": "Market Intelligence",
        "location": "Dubai",
        "context": "Global strategy project",
        "image": "https://images.unsplash.com/photo-1581093588401-fbb62a02f120?auto=format&fit=crop&w=1400&q=85",
        "summary": "Analysed U.S. oncology market opportunity, competitive landscape, commercial positioning and investment logic for a new prostate cancer drug context.",
        "problem": "Pharma market entry requires clarity on market attractiveness, competitive differentiation, pricing logic, stakeholder access and investment feasibility.",
        "role": "Worked on market intelligence, competitive benchmarking, financial modelling and commercial strategy framing.",
        "approach": [
            "Assessed oncology market size and growth context.",
            "Benchmarked competitor positioning and portfolio overlaps.",
            "Structured stakeholder ecosystem across HCPs, payers and institutions.",
            "Built scenario-led financial and launch logic."
        ],
        "frameworks": ["Market Entry Strategy", "Competitor Benchmarking", "Scenario Analysis", "Commercial Strategy"],
        "tools": ["Excel", "PowerPoint", "Secondary research", "Financial modelling"],
        "outputs": [
            "U.S. oncology market assessment.",
            "Competitive benchmarking and whitespace logic.",
            "5-year financial model.",
            "Pricing and investment recommendation logic."
        ],
        "strategic_relevance": "Relevant to market intelligence, competitor benchmarking, commercial modelling and executive-level commercial recommendation."
    },
    {
        "title": "Smart Hospitals – Digital Transformation Strategy",
        "capability": "Healthcare Digital Transformation",
        "location": "Singapore",
        "context": "SingHealth-focused academic consulting project",
        "image": "https://images.unsplash.com/photo-1581091870622-7c80116a9d48?auto=format&fit=crop&w=1400&q=85",
        "summary": "Designed a healthcare digital transformation roadmap focused on interoperability, workflow standardisation, KPI governance, digital adoption and patient journey improvement.",
        "problem": "Hospitals often face fragmented workflows, uneven digital adoption, interoperability gaps and weak KPI visibility across patient-facing and back-office processes.",
        "role": "Conducted research, synthesised expert and patient inputs, assessed workflow adoption gaps and structured the SMART-DX transformation framework.",
        "approach": [
            "Mapped patient journey and hospital workflow pain points.",
            "Reviewed digital maturity benchmarks and transformation barriers.",
            "Synthesised expert interviews, patient inputs and healthcare evidence.",
            "Developed a SMART-DX framework and 3-year transformation roadmap."
        ],
        "frameworks": ["SMART-DX", "TOWS", "Scenario Analysis", "KPI Governance", "Stakeholder Mapping"],
        "tools": ["Excel", "PowerPoint", "Research synthesis", "Interview analysis"],
        "outputs": [
            "SMART-DX digital transformation framework.",
            "3-year roadmap for standardisation, integration and automation.",
            "KPI-led governance recommendations.",
            "Patient journey and workflow improvement priorities."
        ],
        "strategic_relevance": "Relevant to AI-enabled operational redesign, KPI governance, stakeholder adoption and transformation roadmap thinking."
    },
    {
        "title": "Clinical Operations – Consultation Flow & Care Coordination",
        "capability": "Healthcare Operations",
        "location": "India",
        "context": "Dental clinic and hospital-linked clinical workflow experience",
        "image": "https://images.unsplash.com/photo-1606811971618-4486d14f3f99?auto=format&fit=crop&w=1400&q=85",
        "summary": "Managed patient consultation flow, documentation, follow-ups, staff coordination and external lab/vendor coordination across clinical workflows.",
        "problem": "Clinical service quality depends on disciplined documentation, timely follow-ups, staff coordination, patient communication and material readiness.",
        "role": "Coordinated consultation workflows, treatment documentation, patient follow-ups and service readiness across clinical and support stakeholders.",
        "approach": [
            "Managed consultation flow and patient documentation.",
            "Coordinated with staff and external labs for treatment readiness.",
            "Supported follow-up communication and continuity of care.",
            "Strengthened documentation discipline and service coordination."
        ],
        "frameworks": ["Patient Flow", "Clinical Documentation", "Care Coordination", "Service Operations"],
        "tools": ["Clinical records", "Scheduling", "Follow-up tracking", "Stakeholder coordination"],
        "outputs": [
            "Structured patient documentation.",
            "Improved follow-up discipline.",
            "Coordinated staff and lab workflows.",
            "Supported smoother patient experience."
        ],
        "strategic_relevance": "Relevant to lifecycle discipline: structured follow-ups, service coordination, operational clarity and stakeholder communication."
    },
]
analytics_projects = [
    {
        "title": "TasteMate Cloud Kitchen – End-to-End Analytics Dashboard",
        "capability": "Customer Analytics & Decision Intelligence",
        "location": "Academic / Business Analytics Project",
        "context": "Cloud kitchen analytics project using customer and transaction data",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1400&q=85",
        "summary": "Designed an end-to-end analytics dashboard framework connecting customer behaviour, revenue drivers, segmentation, predictive modelling and recommendation logic to business decisions.",
        "problem": "Cloud kitchens need more than sales reports. They need visibility into customer behaviour, spend drivers, loyalty patterns, retention risk, meal combinations and pricing opportunities.",
        "role": "Owned the analytics storyline from business problem framing to dashboard logic, modelling choices, insight generation and business recommendations.",
        "approach": [
            "Cleaned and transformed customer and transaction-level data for analysis.",
            "Used EDA to understand demand, spend behaviour and operational patterns.",
            "Used clustering to segment customers into behavioural personas.",
            "Used regression to model average spend and support pricing and packaging decisions.",
            "Applied classification models for prediction-oriented customer and business decisions.",
            "Used association rule mining to identify revenue-driving meal combinations.",
            "Designed Streamlit dashboard tabs for visualisation, model comparison and business insights."
        ],
        "frameworks": ["EDA", "Customer Segmentation", "Regression", "Classification", "Clustering", "Association Rule Mining"],
        "tools": ["Python", "Streamlit", "Pandas", "Scikit-learn", "Plotly", "Excel"],
        "outputs": [
            "Interactive analytics dashboard structure.",
            "Customer segmentation logic.",
            "Average spend modelling approach.",
            "Classification model comparison.",
            "Association rules for meal combination insights.",
            "Business recommendations for pricing, campaigns and retention."
        ],
        "strategic_relevance": "Shows ownership of analytics as a decision system: from raw data to insight, model logic, dashboarding and commercial recommendations."
    },
    {
        "title": "Turfo Revenue & Utilization Analytics",
        "capability": "Operational Analytics & KPI Ownership",
        "location": "India",
        "context": "Startup operations analytics and dashboard-led decision-making",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1400&q=85",
        "summary": "Built operating trackers and dashboard logic to monitor bookings, pricing performance, utilisation and revenue trends, directly supporting business ownership and growth decisions.",
        "problem": "A growing sports facility needed visibility into slot demand, pricing efficiency, utilisation, customer engagement and revenue performance.",
        "role": "Owned the operating analytics layer by creating trackers, reviewing demand patterns and using performance data to support pricing, scheduling and utilisation decisions.",
        "approach": [
            "Built Excel dashboards for bookings, utilisation and revenue trends.",
            "Analysed customer demand patterns and peak-hour usage.",
            "Tracked weekly performance metrics across utilisation, revenue and engagement.",
            "Used insights to support pricing and scheduling improvements.",
            "Connected operational visibility with revenue growth decisions."
        ],
        "frameworks": ["KPI Tracking", "Utilisation Analysis", "Revenue Analytics", "Pricing Analytics"],
        "tools": ["Excel", "Google Sheets", "Dashboard tracking", "Operational reporting"],
        "outputs": [
            "3× revenue growth in 8 months.",
            "Utilisation improved to approximately 60%.",
            "Structured booking and revenue trackers.",
            "Weekly operational performance visibility."
        ],
        "strategic_relevance": "Direct evidence of dashboard-led business ownership, pricing analytics, utilisation analysis and operating performance tracking."
    },
    {
        "title": "BYJU’S Engagement & Conversion Analytics",
        "capability": "Performance Analytics",
        "location": "India",
        "context": "High-volume EdTech performance and engagement analytics",
        "image": "https://images.unsplash.com/photo-1553877522-43269d4ea984?auto=format&fit=crop&w=1400&q=85",
        "summary": "Used learner engagement and performance signals to identify learning gaps, refine delivery strategies and support conversion-oriented outcomes in a high-volume EdTech environment.",
        "problem": "Large-scale online learning delivery requires continuous visibility into engagement, learner gaps, feedback, session quality and conversion outcomes.",
        "role": "Used performance signals and learner feedback to improve session delivery, communication and student outcomes.",
        "approach": [
            "Reviewed learner engagement and performance dashboards.",
            "Identified learning gaps and adjusted session delivery strategies.",
            "Collected feedback and performance insights across live sessions.",
            "Supported engagement-led conversion outcomes.",
            "Worked in a target-driven performance environment."
        ],
        "frameworks": ["Performance Analysis", "Engagement Analytics", "Learning Gap Analysis", "Conversion Support"],
        "tools": ["Internal dashboards", "Excel", "Performance reports", "Session analytics"],
        "outputs": [
            "2,000+ live sessions delivered.",
            "150+ monthly conversions contributed.",
            "Improved learner engagement and delivery quality.",
            "Top 20% month-on-month performance."
        ],
        "strategic_relevance": "Shows ability to use performance data, feedback and dashboard insights to improve outcomes in a target-driven environment."
    },
    {
        "title": "AI Adoption Research – TPB with Trust Mediation",
        "capability": "Research Analytics & Statistical Modelling",
        "location": "Academic research",
        "context": "Research Methods / SmartPLS project",
        "image": "https://images.unsplash.com/photo-1509228627152-72ae9ae6848d?auto=format&fit=crop&w=1400&q=85",
        "summary": "Developed and analysed an AI adoption research model using the Theory of Planned Behavior with trust as a mediating variable.",
        "problem": "AI adoption is influenced by behavioural, trust, risk, self-efficacy and social expectation factors, requiring structured research modelling.",
        "role": "Designed the research model, reviewed literature, generated/analysed data and interpreted SmartPLS outputs.",
        "approach": [
            "Applied Theory of Planned Behavior constructs.",
            "Integrated trust as a mediating variable.",
            "Reviewed ABDC-rated literature.",
            "Analysed measurement and structural model outputs.",
            "Interpreted model quality, path relationships and adoption implications."
        ],
        "frameworks": ["Theory of Planned Behavior", "PLS-SEM", "Trust Mediation", "Research Design"],
        "tools": ["SmartPLS", "Excel", "Literature review", "Statistical interpretation"],
        "outputs": [
            "Research framework.",
            "Measurement model interpretation.",
            "Structural model interpretation.",
            "Academic reflective report."
        ],
        "strategic_relevance": "Shows research analytics, statistical reasoning, AI adoption insight and evidence-based decision-making."
    },
]

experience = [
    {
        "title": "Co-Founder & Operations Lead – Turfo",
        "period": "Jan 2024 – Jan 2025 | India",
        "image": "https://images.unsplash.com/photo-1526232761682-d26e03ac148e?auto=format&fit=crop&w=1400&q=85",
        "description": "Built and operated a multi-sport play area business, managing daily operations, pricing, vendor coordination, partnerships, customer engagement, booking visibility and revenue tracking.",
        "achievements": [
            "Achieved 3× revenue growth in 8 months through pricing, utilisation and engagement improvements.",
            "Managed 35+ weekly engagements across bookings, customers, partners and operations.",
            "Built Excel trackers for bookings, revenue trends, utilisation and pricing performance.",
            "Improved utilisation to approximately 60% through demand pattern analysis and slot optimisation.",
            "Coordinated 5+ partnerships and vendor relationships while handling ground-level execution."
        ]
    },
    {
        "title": "Academic Specialist – Biology – BYJU’S",
        "period": "Nov 2021 – Apr 2024 | India",
        "image": "https://images.unsplash.com/photo-1523580846011-d3a5bc25702b?auto=format&fit=crop&w=1400&q=85",
        "description": "Delivered live Biology sessions in a high-volume EdTech environment, combining teaching, learner engagement, performance feedback and conversion-supporting academic communication.",
        "achievements": [
            "Delivered 2,000+ live sessions across Biology learning modules.",
            "Contributed to 150+ monthly conversions through engagement and performance insights.",
            "Consistently performed in the top 20% month-on-month.",
            "Received awards for TAT and heavy lifting.",
            "Used learner performance patterns and feedback to improve delivery quality and student engagement."
        ]
    },
    {
        "title": "Associate Dentist – Happy Smile Dental Clinic",
        "period": "Oct 2019 – Oct 2021 | India",
        "image": "https://images.unsplash.com/photo-1606811971618-4486d14f3f99?auto=format&fit=crop&w=1400&q=85",
        "description": "Managed patient care, treatment explanation, clinical documentation, consultation flow, follow-ups, staff coordination and external lab communication.",
        "achievements": [
            "Handled patient-facing consultation workflows and treatment plan communication.",
            "Maintained structured documentation and follow-up discipline.",
            "Coordinated with staff and external labs to support treatment readiness.",
            "Built strong grounding in healthcare operations, patient trust and service coordination."
        ]
    },
    {
        "title": "Global MBA – SP Jain School of Global Management",
        "period": "Feb 2025 – Feb 2026 | Singapore · Dubai · India",
        "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=1400&q=85",
        "description": "Completed global business projects across healthcare, fintech, enterprise transformation, life sciences, AI-enabled product strategy, data analytics and commercial modelling.",
        "achievements": [
            "Worked on consulting-style projects across Dubai, Singapore, UAE and India.",
            "Conducted 100+ primary research responses and 10+ expert/stakeholder interviews across projects.",
            "Built commercial models, operating frameworks, market intelligence outputs and transformation recommendations.",
            "Created portfolio work across Smart Hospitals, GSK, TrueLayer, FinWise, LM Instruments, DP World and Royal Dutch Clinic."
        ]
    },
]

leadership_items = [
    {
        "title": "Global Learning & Student Life Committee",
        "category": "Student Leadership",
        "location": "SP Jain School of Global Management",
        "image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1400&q=85",
        "summary": "Supported cross-campus student engagement, coordination and student-faculty-admin communication during the Global MBA journey.",
        "skills": ["Leadership", "Coordination", "Student engagement", "Cross-functional communication"]
    },
    {
        "title": "Industry Connect Event",
        "category": "Industry Engagement",
        "location": "Dubai",
        "image": "https://images.unsplash.com/photo-1515169067865-5387ec356754?auto=format&fit=crop&w=1400&q=85",
        "summary": "Supported an industry engagement event connecting students with senior business leaders and real-world decision-making discussions.",
        "skills": ["Event coordination", "Industry interface", "Stakeholder communication", "Execution"]
    },
    {
        "title": "Business Conclave",
        "category": "Leadership Event",
        "location": "Dubai",
        "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=1400&q=85",
        "summary": "Contributed to event coordination and student presentation support for a business leadership conclave.",
        "skills": ["Presentation support", "Logistics", "Team coordination", "Professional presence"]
    },
    {
        "title": "OMFS Awareness Marathon",
        "category": "Healthcare Outreach",
        "location": "Chennai",
        "image": "https://images.unsplash.com/photo-1552674605-db6ffd4facb5?auto=format&fit=crop&w=1400&q=85",
        "summary": "Supported a public healthcare awareness event focused on oral and maxillofacial surgery awareness.",
        "skills": ["Healthcare outreach", "Public engagement", "Event execution", "Community awareness"]
    },
    {
        "title": "Anti-Tobacco Awareness Human Chain",
        "category": "Public Health",
        "location": "Chennai",
        "image": "https://images.unsplash.com/photo-1469571486292-0ba58a3f068b?auto=format&fit=crop&w=1400&q=85",
        "summary": "Participated in a public health awareness initiative promoting anti-tobacco education and preventive health communication.",
        "skills": ["Public health", "Community service", "Preventive health", "Awareness building"]
    },
]

extra_curricular_items = [
    {
        "title": "Live Communication & Public Speaking",
        "image": "https://images.unsplash.com/photo-1475721027785-f74eccf877e2?auto=format&fit=crop&w=1400&q=85",
        "summary": "Built through 2,000+ live sessions, MBA presentations, stakeholder discussions and project delivery conversations.",
        "skills": ["Public speaking", "Live delivery", "Audience engagement", "Clarity"]
    },
    {
        "title": "Business Simulations & Strategy Games",
        "image": "https://images.unsplash.com/photo-1552664688-cf412ec27db2?auto=format&fit=crop&w=1400&q=85",
        "summary": "Worked on business simulation environments such as BOSS / Markstrat-style decision-making, market strategy and performance tracking.",
        "skills": ["Decision-making", "Market strategy", "Competitive thinking", "Scenario planning"]
    },
    {
        "title": "Dashboard & Portfolio Building",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1400&q=85",
        "summary": "Built Streamlit dashboards and analytics-driven portfolio assets to present work, data and business evidence visually.",
        "skills": ["Streamlit", "Dashboarding", "Data storytelling", "Portfolio design"]
    },
    {
        "title": "Research Interviews & Insight Collection",
        "image": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=1400&q=85",
        "summary": "Conducted expert and stakeholder interviews across healthcare transformation, patient experience and business research projects.",
        "skills": ["Interviewing", "Research synthesis", "Stakeholder listening", "Insight generation"]
    },
]
skills = {
    "Business & Commercial Execution": [
        "Business ownership",
        "Revenue growth",
        "Stakeholder activation",
        "Commercial follow-up",
        "Pricing thinking",
        "Execution discipline"
    ],
    "Strategy & Transformation": [
        "Market entry strategy",
        "Operating model design",
        "Digital transformation",
        "Ecosystem analysis",
        "Scenario analysis",
        "TOWS / SWOT"
    ],
    "Data Analytics & BI": [
        "Dashboards",
        "EDA",
        "KPI tracking",
        "Regression",
        "Classification",
        "Clustering",
        "Association rule mining"
    ],
    "Healthcare & Life Sciences": [
        "Patient journey mapping",
        "Healthcare operations",
        "Clinical workflow understanding",
        "Market research",
        "Scientific communication",
        "Digital health strategy"
    ],
    "Tools": [
        "Excel",
        "PowerPoint",
        "Power BI",
        "Tableau",
        "Python",
        "Streamlit",
        "SmartPLS",
        "AI tools"
    ],
}

skill_notes = {
    "Business & Commercial Execution": {
        "evidence": "Turfo operating ownership, revenue tracking, pricing decisions, stakeholder handling and high-volume EdTech performance delivery.",
        "methods": "Revenue tracking · Pricing thinking · Stakeholder coordination · Execution discipline"
    },
    "Strategy & Transformation": {
        "evidence": "Consulting-style MBA projects across fintech, healthcare, enterprise systems, life sciences and digital trade.",
        "methods": "Market entry · Operating model design · TOWS/SWOT · Scenario analysis"
    },
    "Data Analytics & BI": {
        "evidence": "TasteMate dashboard, Turfo revenue/utilisation trackers, BYJU’S engagement analytics and AI adoption modelling.",
        "methods": "EDA · Regression · Classification · Clustering · KPI dashboards"
    },
    "Healthcare & Life Sciences": {
        "evidence": "BDS clinical experience, healthcare operations, digital health strategy, patient journey work and life sciences market intelligence.",
        "methods": "Patient journey mapping · Clinical workflow · Research synthesis · Healthcare strategy"
    },
    "Tools": {
        "evidence": "Used across dashboards, analysis, modelling, reporting, presentations and portfolio development.",
        "methods": "Excel · PowerPoint · Power BI · Tableau · Python · Streamlit · SmartPLS · AI tools"
    }
}

skills_visuals = {
    "Business & Commercial Execution": {
        "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1400&q=85",
        "headline": "Execution, ownership and commercial discipline"
    },
    "Strategy & Transformation": {
        "image": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1400&q=85",
        "headline": "Structured business problem solving across markets and systems"
    },
    "Data Analytics & BI": {
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1400&q=85",
        "headline": "Dashboards, modelling and decision intelligence"
    },
    "Healthcare & Life Sciences": {
        "image": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=1400&q=85",
        "headline": "Clinical grounding plus healthcare strategy exposure"
    },
    "Tools": {
        "image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1400&q=85",
        "headline": "Practical stack for analysis, reporting and portfolio building"
    }
}

# ------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------

def render_badges(items, style="badge"):
    st.markdown("".join([f'<span class="{style}">{item}</span>' for item in items]), unsafe_allow_html=True)

def render_metric_card(value, label):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)

def render_fit_card(area, evidence):
    st.markdown(f"""
    <div class="fit-card">
        <h3>{area}</h3>
        <p>{evidence}</p>
    </div>
    """, unsafe_allow_html=True)

def render_project_card(project):
    st.markdown(f"""
    <div class="project-card">
        <img src="{project["image"]}" class="project-img">
        <div class="project-body">
            <div class="project-title">{project["title"]}</div>
            <div class="project-meta">{project["capability"]} · {project["location"]}</div>
            <div class="project-summary">{project["summary"]}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    render_badges(project["frameworks"][:5], "badge-red")

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
            render_badges(project["tools"], "badge-red")

            st.markdown("#### Relevance")
            st.markdown(f"""
            <div class="relevance-box">
                {project["strategic_relevance"]}
            </div>
            """, unsafe_allow_html=True)

def render_experience_card(item):
    achievement_html = "".join([f"<li>{achievement}</li>" for achievement in item["achievements"]])
    st.markdown(f"""
    <div class="project-card">
        <img src="{item["image"]}" class="experience-img">
        <div class="experience-body">
            <div class="timeline-title">{item["title"]}</div>
            <div class="timeline-meta">{item["period"]}</div>
            <div class="timeline-detail">{item["description"]}</div>
            <div class="achievement-list">
                <b>Achievements:</b>
                <ul>
                    {achievement_html}
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_simple_visual_card(item):
    chips = "".join([f'<span class="skill-item">{skill}</span>' for skill in item["skills"]])
    st.markdown(f"""
    <div class="project-card">
        <img src="{item["image"]}" class="project-img">
        <div class="project-body">
            <div class="project-title">{item["title"]}</div>
            <div class="project-meta">{item.get("category", "Extra-Curricular")} · {item.get("location", "")}</div>
            <div class="project-summary">{item["summary"]}</div>
            <div>{chips}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def make_project_capability_chart():
    df = pd.DataFrame(projects)
    counts = df["capability"].value_counts().reset_index()
    counts.columns = ["Capability", "Count"]
    fig = px.bar(counts, x="Capability", y="Count", text="Count", color="Capability", title="Project Coverage by Capability")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#d4d4d8", title_font_color="#ffffff", xaxis_tickangle=-25, height=450, showlegend=False, margin=dict(l=20, r=20, t=60, b=110))
    fig.update_traces(textposition="outside")
    return fig

def make_project_mix_donut():
    df = pd.DataFrame(projects)
    counts = df["capability"].value_counts().reset_index()
    counts.columns = ["Capability", "Count"]
    fig = px.pie(counts, names="Capability", values="Count", hole=0.52, title="Project Portfolio Mix")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#d4d4d8", title_font_color="#ffffff", height=430, legend=dict(font=dict(color="#d4d4d8")))
    return fig

def make_analytics_methods_chart():
    methods = pd.DataFrame({
        "Method": ["Dashboards", "EDA", "Regression", "Classification", "Clustering", "Association Rules", "KPI Tracking", "Financial Modelling"],
        "Strength": [9, 8, 7, 7, 7, 6, 9, 8]
    })
    fig = px.bar(methods, x="Method", y="Strength", text="Strength", title="Analytics Method Coverage")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#d4d4d8", title_font_color="#ffffff", xaxis_tickangle=-25, height=420, showlegend=False)
    fig.update_traces(textposition="outside")
    return fig

def make_analytics_workflow_chart():
    fig = go.Figure(go.Funnel(
        y=["Raw Data", "Cleaning & Transformation", "EDA", "Modelling", "Dashboard", "Business Decisions"],
        x=[100, 90, 80, 65, 55, 45],
        textinfo="value+percent initial",
        marker={"color": ["#E53935", "#C62828", "#B71C1C", "#8E1B1B", "#6D1717", "#4A0F0F"]}
    ))
    fig.update_layout(title="Analytics Workflow: From Raw Data to Business Decisions", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#d4d4d8", title_font_color="#ffffff", height=430)
    return fig

def make_analytics_project_chart():
    df = pd.DataFrame(analytics_projects)
    counts = df["capability"].value_counts().reset_index()
    counts.columns = ["Analytics Capability", "Count"]
    fig = px.pie(counts, names="Analytics Capability", values="Count", hole=0.52, title="Analytics Project Mix")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#d4d4d8", title_font_color="#ffffff", height=430)
    return fig

def make_capability_radar():
    categories = ["Execution", "Commercial Thinking", "Analytics", "AI / Digital", "Healthcare", "Stakeholder Management"]
    scores = [9, 8, 9, 8, 8, 9]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=scores, theta=categories, fill="toself", line=dict(color="#E53935", width=3), fillcolor="rgba(229,57,53,0.25)"))
    fig.update_layout(polar=dict(bgcolor="rgba(0,0,0,0)", radialaxis=dict(visible=True, range=[0, 10], color="#a1a1aa"), angularaxis=dict(color="#d4d4d8")), paper_bgcolor="rgba(0,0,0,0)", font_color="#d4d4d8", title=dict(text="Portfolio Capability Radar", font=dict(color="#ffffff")), showlegend=False, height=430)
    return fig

def make_leadership_mix_chart():
    df = pd.DataFrame(leadership_items)
    counts = df["category"].value_counts().reset_index()
    counts.columns = ["Leadership Area", "Count"]
    fig = px.bar(counts, x="Leadership Area", y="Count", text="Count", color="Leadership Area", title="Leadership & Community Coverage")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#d4d4d8", title_font_color="#ffffff", xaxis_tickangle=-20, height=420, showlegend=False)
    fig.update_traces(textposition="outside")
    return fig

# ------------------------------------------------------------
# RENDER SECTIONS
# ------------------------------------------------------------

def render_home():
    st.markdown("""
    <div class="hero-shell">
        <div class="hero-content">
            <div class="name-chip">Shalini Arun Prakash · Professional Portfolio</div>
            <div class="hero-title">
                I turn <span class="highlight-red">complex problems</span><br>
                into structured business outcomes.
            </div>
            <div class="hero-subline">
                A portfolio across healthcare, digital transformation, startup operations,
                data analytics, AI-enabled business models, commercial execution and
                evidence-backed problem solving.
            </div>
            <span class="badge badge-red">Healthcare</span>
            <span class="badge badge-red">Digital Transformation</span>
            <span class="badge badge-red">Data Analytics</span>
            <span class="badge">Commercial Execution</span>
            <span class="badge">AI-Enabled Business Models</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="hero-mini-card"><b>Execution Operator</b><p>Startup operations, EdTech delivery and clinical coordination show ground-level ownership.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="hero-mini-card"><b>Business Problem Solver</b><p>Consulting-style projects across healthcare, fintech, transformation and market strategy.</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="hero-mini-card"><b>Analytics + AI Builder</b><p>Dashboards, modelling, research analytics and AI-enabled product/system thinking.</p></div>""", unsafe_allow_html=True)

    cols = st.columns(4)
    for i, (value, label) in enumerate(metrics[:4]):
        with cols[i]:
            render_metric_card(value, label)

    cols = st.columns(4)
    for i, (value, label) in enumerate(metrics[4:]):
        with cols[i]:
            render_metric_card(value, label)

    st.markdown('<div class="section-title">Portfolio Fit</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">A structured view of how my experience and project work connect across execution, commercial thinking, analytics, healthcare, AI and stakeholder management.</div>', unsafe_allow_html=True)

    for i in range(0, len(portfolio_fit_areas), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(portfolio_fit_areas):
                with col:
                    item = portfolio_fit_areas[i + j]
                    render_fit_card(item["area"], item["evidence"])

    st.markdown('<div class="section-title">Portfolio Visuals</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="visual-card">', unsafe_allow_html=True)
        st.plotly_chart(make_project_capability_chart(), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="visual-card">', unsafe_allow_html=True)
        st.plotly_chart(make_project_mix_donut(), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="visual-card">', unsafe_allow_html=True)
    st.plotly_chart(make_capability_radar(), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_experience():
    st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Professional experience with role descriptions, visual context and achievement evidence under each experience.</div>', unsafe_allow_html=True)
    for i in range(0, len(experience), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(experience):
                with col:
                    render_experience_card(experience[i + j])

def render_projects():
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Consulting-style and business project work across healthcare, fintech, digital transformation, commercial strategy, AI-enabled models and market intelligence. Work experience such as Turfo is intentionally kept in Experience.</div>', unsafe_allow_html=True)
    capability_filter = st.selectbox("Filter by capability", ["All"] + sorted(set([p["capability"] for p in projects])))
    filtered = projects if capability_filter == "All" else [p for p in projects if p["capability"] == capability_filter]
    st.write(f"Showing {len(filtered)} project(s).")
    for i in range(0, len(filtered), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(filtered):
                with col:
                    render_project_card(filtered[i + j])

def render_analytics():
    st.markdown('<div class="section-title">Data Analytics & Business Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">A dedicated section for dashboarding, KPI ownership, customer analytics, predictive modelling, research analytics and data-driven decision support.</div>', unsafe_allow_html=True)
    analytics_cards = [
        {"area": "Decision intelligence", "evidence": "Framed analytics projects around business choices: pricing, utilisation, spend behaviour, segmentation, retention and operational performance."},
        {"area": "Dashboard ownership", "evidence": "Built trackers and dashboard structures that made performance visible across bookings, utilisation, revenue, engagement and model outputs."},
        {"area": "Customer analytics", "evidence": "Used segmentation, behaviour patterns, spend modelling and association rules to move beyond reporting into actionable commercial insight."},
        {"area": "Research analytics", "evidence": "Designed and interpreted AI adoption analysis using TPB, trust mediation, SmartPLS outputs and evidence-backed reasoning."},
    ]
    for i in range(0, len(analytics_cards), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(analytics_cards):
                item = analytics_cards[i + j]
                with col:
                    render_fit_card(item["area"], item["evidence"])

    st.markdown('<div class="section-title">Analytics Visuals</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="visual-card">', unsafe_allow_html=True)
        st.plotly_chart(make_analytics_methods_chart(), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="visual-card">', unsafe_allow_html=True)
        st.plotly_chart(make_analytics_workflow_chart(), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="visual-card">', unsafe_allow_html=True)
    st.plotly_chart(make_analytics_project_chart(), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Analytics Project Evidence</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Analytics evidence is separated from the main Projects tab to make dashboarding, modelling and BI ownership visible on its own.</div>', unsafe_allow_html=True)
    for i in range(0, len(analytics_projects), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(analytics_projects):
                with col:
                    render_project_card(analytics_projects[i + j])

def render_skills():
    st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">A visual capability map showing what I can do, where it was demonstrated, and the tools or methods behind it.</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="skill-strip">
        <div class="skill-strip-item">Business Ownership</div>
        <div class="skill-strip-item">Healthcare Strategy</div>
        <div class="skill-strip-item">Data Analytics</div>
        <div class="skill-strip-item">AI-Enabled Workflows</div>
        <div class="skill-strip-item">Commercial Execution</div>
    </div>
    """, unsafe_allow_html=True)

    skill_items = list(skills.items())
    for i in range(0, len(skill_items), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(skill_items):
                category, items = skill_items[i + j]
                chips = "".join([f'<span class="skill-item">{item}</span>' for item in items])
                evidence = skill_notes.get(category, {}).get("evidence", "")
                methods = skill_notes.get(category, {}).get("methods", "")
                image = skills_visuals.get(category, {}).get("image", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1400&q=85")
                headline = skills_visuals.get(category, {}).get("headline", "")
                with col:
                    st.markdown(f"""
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
                    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Project-to-Capability Map</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">A recruiter-friendly map connecting project evidence to capabilities, frameworks and tools.</div>', unsafe_allow_html=True)
    mapping_data = []
    for p in projects:
        mapping_data.append({"Project": p["title"], "Capability": p["capability"], "Frameworks": ", ".join(p["frameworks"]), "Tools": ", ".join(p["tools"]), "Relevance": p["strategic_relevance"]})
    st.dataframe(pd.DataFrame(mapping_data), use_container_width=True, hide_index=True)

def render_leadership():
    st.markdown('<div class="section-title">Leadership & Community</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Leadership, public health outreach, student engagement, professional events and extra-curricular strengths presented as evidence of initiative and presence.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Leadership & Volunteer Work</div>', unsafe_allow_html=True)
    for i in range(0, len(leadership_items), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(leadership_items):
                with col:
                    render_simple_visual_card(leadership_items[i + j])

    st.markdown('<div class="section-title">Leadership Visual</div>', unsafe_allow_html=True)
    st.markdown('<div class="visual-card">', unsafe_allow_html=True)
    st.plotly_chart(make_leadership_mix_chart(), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Extra-Curricular Strengths</div>', unsafe_allow_html=True)
    for i in range(0, len(extra_curricular_items), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(extra_curricular_items):
                with col:
                    render_simple_visual_card(extra_curricular_items[i + j])

def render_proof_points():
    st.markdown('<div class="section-title">Proof Points</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Numbers and evidence that support execution discipline, analytics capability, business ownership and project impact.</div>', unsafe_allow_html=True)
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
        ("Multi-domain", "Fintech, healthcare, EdTech, F&B, logistics and enterprise transformation")
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
        st.markdown("""
        <div class="contact-card">
            <h3>Shalini Arun Prakash</h3>
            <p><b>Portfolio Focus:</b> Healthcare · Digital Transformation · Business Projects · Data Analytics · AI-Enabled Business Models</p>
            <p><b>Location:</b> India</p>
            <p><b>Email:</b> shaliniarun23@gmail.com</p>
            <p><b>LinkedIn:</b> linkedin.com/in/shaliniarun</p>
            <br>
            <p><b>Professional narrative:</b> Healthcare-rooted business professional with EdTech, startup operations, analytics, AI-enabled project work and global MBA exposure.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="contact-card">
            <h3>Portfolio Use</h3>
            <p>This portfolio maps experience, projects, analytics work, leadership and community engagement into a single professional profile.</p>
            <p>It is public-safe and does not expose confidential project documents, raw datasets or private submissions.</p>
            <br>
            <p><b>Full reports and confidential project documents are available only on request.</b></p>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------

st.markdown("""
<div style="padding: 0.9rem 0 1.4rem 0; border-bottom:1px solid rgba(255,255,255,0.10); margin-bottom:1rem;">
    <div style="font-size: 1.75rem; font-weight: 950; color: #ffffff; text-transform: uppercase; letter-spacing:-0.03em;">
        Shalini Arun Prakash
    </div>
    <div style="color:#a1a1aa; margin-top:0.35rem; font-size:0.95rem;">
        Healthcare · Digital Transformation · Data Analytics · AI-Enabled Business Models · Commercial Execution
    </div>
</div>
""", unsafe_allow_html=True)

tab_home, tab_experience, tab_projects, tab_analytics, tab_skills, tab_leadership, tab_proof, tab_contact = st.tabs(
    ["Home", "Experience", "Projects", "Analytics", "Skills", "Leadership", "Proof Points", "Contact"]
)

with tab_home:
    render_home()

with tab_experience:
    render_experience()

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
    unsafe_allow_html=True
)
