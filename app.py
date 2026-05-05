import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------

st.set_page_config(
    page_title="Shalini Arun Prakash",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------------------
# CSS — PREMIUM BLACK / RED PORTFOLIO STYLE
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
    max-width: 1340px;
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
        linear-gradient(90deg, rgba(0,0,0,0.98), rgba(0,0,0,0.86), rgba(0,0,0,0.40)),
        url('https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=1800&q=90');
    background-size: cover;
    background-position: center;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 35px 100px rgba(0,0,0,0.65);
    margin-bottom: 2rem;
}

.hero-content {
    max-width: 1080px;
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
    font-size: clamp(3rem, 5.8vw, 6.1rem);
    line-height: 0.94;
    font-weight: 950;
    color: #ffffff;
    margin-bottom: 1.35rem;
    max-width: 1150px;
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
    max-width: 890px;
    color: #d4d4d8;
    margin-bottom: 1.6rem;
}

.hero-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
    margin-top: 2rem;
    max-width: 1080px;
}

.hero-mini-card {
    padding: 1rem;
    border-radius: 0px;
    background: rgba(17,17,19,0.88);
    border: 1px solid rgba(255,255,255,0.10);
    border-left: 4px solid #E53935;
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
    margin-top: 2.7rem;
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
    max-width: 980px;
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
}

.project-img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    border-bottom: 4px solid #E53935;
    opacity: 0.88;
    filter: grayscale(30%) contrast(1.08);
}

.project-body {
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

.timeline-card {
    position: relative;
    background: #111113;
    padding: 1.2rem 1.35rem 1.2rem 1.5rem;
    border-radius: 0px;
    border: 1px solid rgba(255,255,255,0.12);
    margin-bottom: 1rem;
    box-shadow: 0 16px 45px rgba(0,0,0,0.32);
}

.timeline-card:before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 5px;
    background: #E53935;
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
    .hero-grid { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# DATA
# ------------------------------------------------------------

metrics = [
    ("3×", "Revenue growth achieved through startup operations and commercialization"),
    ("150+", "Monthly conversions contributed through engagement and performance insights"),
    ("35+", "Weekly engagements managed through customer-facing operations"),
    ("$3.5M", "Commercial proposal structured for enterprise transformation"),
    ("14+", "Projects across strategy, operations, AI, growth and transformation"),
    ("100+", "Primary research responses used for market and customer insight"),
    ("10+", "Expert / stakeholder interviews across transformation research"),
    ("5+", "Years across healthcare, EdTech, startup operations and strategy projects"),
]

strategic_fit_areas = [
    {
        "area": "Business ownership & revenue growth",
        "evidence": "Turfo revenue growth, BYJU’S conversion support, Bunk Station turnaround logic and high-volume operating discipline."
    },
    {
        "area": "Ecosystem development",
        "evidence": "TrueLayer platform ecosystem assessment, FinWise stakeholder model, Royal Dutch Clinic customer acquisition and referral pathway analysis."
    },
    {
        "area": "Commercial strategy & unit economics",
        "evidence": "Bunk Station AOV and operating roadmap, LM Instruments $3.5M commercial model, GSK market entry and financial model."
    },
    {
        "area": "AI-powered operations",
        "evidence": "FinWise AI-enabled MVP, AI Adoption Research, Smart Hospitals automation/KPI governance and DP World emerging-tech use cases."
    },
    {
        "area": "Stakeholder activation",
        "evidence": "BYJU’S high-retention sessions, patient/customer journey projects, clinical coordination and cross-functional MBA projects."
    },
    {
        "area": "Market intelligence",
        "evidence": "GSK oncology market assessment, TrueLayer open banking analysis, DP World digital trade ecosystem and Royal Dutch Clinic growth research."
    },
]

projects = [
    {
        "title": "Turfo – Startup Operations & Revenue Growth",
        "capability": "Business Ownership & Revenue",
        "location": "India",
        "context": "Co-founder and operations lead experience | Jan 2024 – Jan 2025",
        "image": "https://images.unsplash.com/photo-1526232761682-d26e03ac148e?auto=format&fit=crop&w=1400&q=85",
        "summary": "Built and operated a multi-sport play area business, driving revenue growth, partnerships, operations, pricing and utilisation tracking.",
        "problem": "Early-stage businesses require disciplined execution across acquisition, pricing, scheduling, vendor management and daily operations.",
        "role": "Co-founded the venture and handled operations, revenue tracking, partnerships, vendors and customer engagement from Jan 2024 to Jan 2025.",
        "approach": ["Built Excel trackers for bookings, utilisation and revenue.", "Optimised pricing and slot utilisation.", "Managed vendors, partners and weekly engagements.", "Coordinated execution across operations and customer touchpoints."],
        "frameworks": ["Revenue Operations", "Utilisation Tracking", "Pricing Optimisation", "Stakeholder Management"],
        "tools": ["Excel", "Google Sheets", "Operations tracking", "Customer coordination"],
        "outputs": ["3× revenue growth in 8 months.", "35+ weekly engagements.", "5+ partnerships.", "Structured booking and utilisation trackers."],
        "strategic_relevance": "Direct evidence of business ownership, revenue improvement, partner coordination, performance tracking and target-oriented execution."
    },
    {
        "title": "Bunk Station – Strategic Turnaround & Investment Roadmap",
        "capability": "Commercial Strategy & Unit Economics",
        "location": "Dubai",
        "context": "Live consulting-style F&B turnaround project",
        "image": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1400&q=85",
        "summary": "Developed a strategic turnaround plan by diagnosing market demand, customer segments, branding gaps, operational inefficiency and revenue growth opportunities.",
        "problem": "Bunk Station had strong fundamentals such as best-selling SKUs and a student customer base, but weak visibility, poor ratings, branding gaps and operational inefficiency.",
        "role": "Conducted business diagnosis and recommended an investment-led repositioning strategy instead of maintaining status quo or shutting down.",
        "approach": ["Analysed DIAC student market demand and customer personas.", "Reviewed brand positioning, menu architecture, operations and competitive context.", "Identified bottlenecks around visibility, service speed and revenue conversion.", "Developed a turnaround roadmap covering menu engineering, combo pricing, QR ordering, loyalty programs and KPI tracking."],
        "frameworks": ["Turnaround Strategy", "Customer Persona", "Menu Engineering", "KPI Tracking", "Investment Decision"],
        "tools": ["PowerPoint", "Market analysis", "Primary research", "Financial logic"],
        "outputs": ["Strategic turnaround recommendation.", "Investment-led repositioning plan.", "Menu and combo pricing strategy.", "QR-based ordering and KPI roadmap.", "Revenue growth and operating efficiency logic."],
        "strategic_relevance": "Strong fit for unit economics, commercial diagnosis, growth planning, KPI tracking, customer acquisition and performance improvement."
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
        "approach": ["Analysed PSD2, API infrastructure and open banking regulation.", "Evaluated market expansion opportunities using readiness and demand criteria.", "Assessed operating model capabilities such as compliance agility, scalability and ecosystem integration.", "Linked platform strategy to financial services business model innovation."],
        "frameworks": ["Platform Strategy", "Open Banking", "API Ecosystem", "Regulatory Strategy", "Market Expansion"],
        "tools": ["Case analysis", "PowerPoint", "Strategic frameworks", "Secondary research"],
        "outputs": ["Open banking strategy assessment.", "Market expansion prioritisation logic.", "Operating model capability review.", "Ecosystem partnership analysis."],
        "strategic_relevance": "Relevant to ecosystem development, platform partnerships, regulated fintech analysis, market readiness and expansion logic."
    },
    {
        "title": "FinWise – AI-Powered Financial Literacy Platform",
        "capability": "AI-Powered Operations",
        "location": "UAE",
        "context": "AI-enabled B2B2C education/product strategy",
        "image": "https://images.unsplash.com/photo-1553729459-efe14ef6055d?auto=format&fit=crop&w=1400&q=85",
        "summary": "Designed a scalable AI-enabled financial literacy model for students, parents, schools and CSR partners with structured learning journeys and implementation logic.",
        "problem": "Financial literacy gaps among school-aged learners are driven by curriculum gaps, behavioural gaps, parental engagement gaps and system constraints.",
        "role": "Structured the product concept, stakeholder model, MVP logic, journey maps, service blueprint and scale roadmap.",
        "approach": ["Defined target stakeholders: students, parents, schools and sponsors.", "Mapped learning journeys and behavioural reinforcement logic.", "Structured B2B2C operating model and partner-led rollout.", "Developed TOWS, service blueprint and governance logic."],
        "frameworks": ["TOWS", "Service Blueprint", "Customer Journey", "B2B2C Model", "MVP Design"],
        "tools": ["PowerPoint", "AI tools", "Business model design", "Journey mapping"],
        "outputs": ["AI-enabled MVP structure.", "Student-parent-school journey map.", "Service blueprint.", "3-year scale roadmap."],
        "strategic_relevance": "Shows AI-enabled workflow thinking, stakeholder ecosystems, onboarding journeys and scalable operating model design."
    },
    {
        "title": "BYJU’S – Academic Delivery, Engagement & Conversion Support",
        "capability": "Business Ownership & Revenue",
        "location": "India",
        "context": "Academic Specialist – Biology",
        "image": "https://images.unsplash.com/photo-1523580846011-d3a5bc25702b?auto=format&fit=crop&w=1400&q=85",
        "summary": "Delivered high-volume live learning sessions, supported learner engagement and contributed to performance-driven conversion outcomes.",
        "problem": "Large-scale EdTech delivery requires consistency, communication quality, learner engagement and data-backed performance improvement.",
        "role": "Delivered live academic sessions, analysed learner performance and supported engagement-led conversion outcomes.",
        "approach": ["Delivered structured live sessions at scale.", "Translated complex biology concepts into clear explanations.", "Used performance insights to improve learner engagement.", "Worked in a target-oriented, high-volume delivery environment."],
        "frameworks": ["Learning Delivery", "Performance Tracking", "Learner Engagement", "Conversion Support"],
        "tools": ["Learning platforms", "Excel", "Communication frameworks", "Performance dashboards"],
        "outputs": ["2,000+ live sessions delivered.", "150+ monthly conversions contributed.", "Top 20% month-on-month performance.", "Awards for TAT and heavy lifting."],
        "strategic_relevance": "Evidence of target-driven execution, high-volume stakeholder communication, performance tracking and resilience under delivery pressure."
    },
    {
        "title": "BYJU’S – Learning Experience Design & High-Retention Sessions",
        "capability": "Stakeholder Activation",
        "location": "India",
        "context": "Learning delivery and student engagement design",
        "image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1400&q=85",
        "summary": "Designed high-energy biology sessions using hooks, storytelling, interactive layers, energy resets, visual reinforcement, gamified challenges and cognitive load management.",
        "problem": "Online learning sessions can lose student attention quickly unless content is structured around engagement, clarity, rhythm and retention.",
        "role": "Converted complex biology topics into layered, interactive and retention-focused learning experiences.",
        "approach": ["Used strong opening questions and recall tasks to activate prior knowledge.", "Structured sessions with curiosity peaks, explanation depth and energy resets.", "Used gamified challenges, rapid polls and predictive prompts to sustain engagement.", "Simplified difficult diagrams through layered visual explanation and side-by-side comparisons."],
        "frameworks": ["Learning Experience Design", "Cognitive Load Management", "Student Journey", "Engagement Design"],
        "tools": ["Live teaching platforms", "Visual explanation", "Polls", "Session planning"],
        "outputs": ["High-retention session structures.", "Interactive biology explanations.", "Gamified engagement formats.", "Improved student participation and attention flow."],
        "strategic_relevance": "Relevant to stakeholder activation and enablement: simplifying complex topics, sustaining engagement and creating structured onboarding experiences."
    },
    {
        "title": "LM Instruments – SAP S/4HANA Transformation Strategy",
        "capability": "AI-Powered Operations",
        "location": "Dubai",
        "context": "SAP transformation RFP and commercial model",
        "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1400&q=85",
        "summary": "Structured AS-IS / TO-BE workflows, SAP-aligned operating blueprints, data migration logic and commercial proposal for enterprise transformation.",
        "problem": "Enterprise transformation requires clear process design, data readiness, governance, cost logic and implementation sequencing across functions.",
        "role": "Mapped business requirements, process dependencies, data entities and commercial proposal logic.",
        "approach": ["Structured AS-IS and TO-BE workflows across enterprise functions.", "Translated business inputs into SAP-aligned process blueprints.", "Defined data migration and validation logic across critical entities.", "Built commercial model with cost, margin and governance assumptions."],
        "frameworks": ["AS-IS / TO-BE", "RFP Response", "Operating Blueprint", "Governance Model"],
        "tools": ["Excel", "PowerPoint", "Process mapping", "Cost modelling"],
        "outputs": ["5+ enterprise workflow maps.", "SAP-aligned operating blueprint.", "Data validation logic across 6+ entities.", "$3.5M commercial proposal with margin logic."],
        "strategic_relevance": "Shows structured onboarding logic, process automation, data workflow design, governance and commercial model discipline."
    },
    {
        "title": "DP World – Digital Trade & Supply Chain Transformation",
        "capability": "Market Intelligence",
        "location": "Dubai",
        "context": "Emerging technology strategy project",
        "image": "https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3?auto=format&fit=crop&w=1400&q=85",
        "summary": "Assessed how AI, blockchain, AR/VR and drones can improve trade visibility, logistics efficiency, documentation speed and operational resilience.",
        "problem": "Trade and logistics ecosystems face inefficiencies across documentation, customs, visibility, yard planning and asset monitoring.",
        "role": "Conducted use-case analysis, operating model assessment and technology-to-business-impact mapping.",
        "approach": ["Assessed emerging technology use cases across trade operations.", "Mapped impact across customs, cargo visibility, workforce enablement and asset monitoring.", "Linked automation and digital workflows to operational throughput and documentation improvements.", "Structured recommendations around efficiency, trust and resilience."],
        "frameworks": ["Emerging Tech Strategy", "Use-Case Prioritisation", "Operating Model", "Digital Trade Ecosystem"],
        "tools": ["PowerPoint", "Research synthesis", "Benchmarking", "Process analysis"],
        "outputs": ["Emerging technology use-case map.", "Digital trade ecosystem assessment.", "Operational improvement logic.", "Strategic recommendation deck."],
        "strategic_relevance": "Relevant for global ecosystem thinking, emerging technology, operational visibility and cross-border commercial environments."
    },
    {
        "title": "Royal Dutch Clinic – Growth Strategy & Operating Model Analysis",
        "capability": "Stakeholder Activation",
        "location": "UAE",
        "context": "Healthcare growth and operating model project",
        "image": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=1400&q=85",
        "summary": "Assessed growth potential, patient journey, referral pathways, pricing sensitivity and operational bottlenecks for a premium healthcare services context.",
        "problem": "Healthcare service growth can be constrained by unclear patient acquisition pathways, pricing friction, operational bottlenecks and inconsistent service conversion.",
        "role": "Supported market and operational analysis using primary research, benchmarking and patient journey assessment.",
        "approach": ["Analysed patient journey and inquiry-to-appointment funnel.", "Reviewed referral pathways and competitive healthcare landscape.", "Used 100+ primary research responses for demand and pricing insights.", "Recommended service, pricing and operating model improvements."],
        "frameworks": ["Patient Journey Mapping", "Operating Model", "Growth Strategy", "Customer Insight"],
        "tools": ["Excel", "Survey analysis", "PowerPoint", "Benchmarking"],
        "outputs": ["Growth strategy recommendations.", "Patient funnel and service workflow insights.", "Pricing and demand observations.", "Operating model improvement priorities."],
        "strategic_relevance": "Shows customer acquisition logic, stakeholder mapping, service conversion thinking and operating model improvement."
    },
    {
        "title": "GSK – U.S. Oncology Market Entry & Commercial Strategy",
        "capability": "Market Intelligence",
        "location": "Dubai",
        "context": "Global strategy project",
        "image": "https://images.unsplash.com/photo-1579154341098-e4e158cc7f55?auto=format&fit=crop&w=1400&q=85",
        "summary": "Analysed U.S. oncology market opportunity, competitive landscape, commercial positioning and investment logic for a new prostate cancer drug context.",
        "problem": "Pharma market entry requires clarity on market attractiveness, competitive differentiation, pricing logic, stakeholder access and investment feasibility.",
        "role": "Worked on market intelligence, competitive benchmarking, financial modelling and commercial strategy framing.",
        "approach": ["Assessed oncology market size and growth context.", "Benchmarked competitor positioning and portfolio overlaps.", "Structured stakeholder ecosystem across HCPs, payers and institutions.", "Built scenario-led financial and launch logic."],
        "frameworks": ["Market Entry Strategy", "Competitor Benchmarking", "Scenario Analysis", "Commercial Strategy"],
        "tools": ["Excel", "PowerPoint", "Secondary research", "Financial modelling"],
        "outputs": ["U.S. oncology market assessment.", "Competitive benchmarking and whitespace logic.", "5-year financial model.", "Pricing and investment recommendation logic."],
        "strategic_relevance": "Relevant to market intelligence, competitor benchmarking, commercial modelling and executive-level commercial recommendation."
    },
    {
        "title": "Smart Hospitals – Digital Transformation Strategy",
        "capability": "AI-Powered Operations",
        "location": "Singapore",
        "context": "SingHealth-focused academic consulting project",
        "image": "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&w=1400&q=85",
        "summary": "Designed a healthcare digital transformation roadmap focused on interoperability, workflow standardisation, KPI governance, digital adoption and patient journey improvement.",
        "problem": "Hospitals often face fragmented workflows, uneven digital adoption, interoperability gaps and weak KPI visibility across patient-facing and back-office processes.",
        "role": "Conducted research, synthesised expert and patient inputs, assessed workflow adoption gaps and structured the SMART-DX transformation framework.",
        "approach": ["Mapped patient journey and hospital workflow pain points.", "Reviewed digital maturity benchmarks and transformation barriers.", "Synthesised expert interviews, patient inputs and healthcare evidence.", "Developed a SMART-DX framework and 3-year transformation roadmap."],
        "frameworks": ["SMART-DX", "TOWS", "Scenario Analysis", "KPI Governance", "Stakeholder Mapping"],
        "tools": ["Excel", "PowerPoint", "Research synthesis", "Interview analysis"],
        "outputs": ["SMART-DX digital transformation framework.", "3-year roadmap for standardisation, integration and automation.", "KPI-led governance recommendations.", "Patient journey and workflow improvement priorities."],
        "strategic_relevance": "Relevant to AI-enabled operational redesign, KPI governance, stakeholder adoption and transformation roadmap thinking."
    },
    {
        "title": "Clinical Operations – Consultation Flow & Care Coordination",
        "capability": "Stakeholder Activation",
        "location": "India",
        "context": "Dental clinic and hospital-linked clinical workflow experience",
        "image": "https://images.unsplash.com/photo-1606811971618-4486d14f3f99?auto=format&fit=crop&w=1400&q=85",
        "summary": "Managed patient consultation flow, documentation, follow-ups, staff coordination and external lab/vendor coordination across high-volume clinical workflows.",
        "problem": "Clinical service quality depends on disciplined documentation, timely follow-ups, staff coordination, patient communication and material readiness.",
        "role": "Coordinated consultation workflows, treatment documentation, patient follow-ups and service readiness across clinical and support stakeholders.",
        "approach": ["Managed weekly consultation flow and patient documentation.", "Coordinated with staff and external labs for treatment readiness.", "Supported follow-up communication and continuity of care.", "Strengthened documentation discipline and service coordination."],
        "frameworks": ["Patient Flow", "Clinical Documentation", "Care Coordination", "Service Operations"],
        "tools": ["Clinical records", "Scheduling", "Follow-up tracking", "Stakeholder coordination"],
        "outputs": ["Structured patient documentation.", "Improved follow-up discipline.", "Coordinated staff and lab workflows.", "Supported smoother patient experience."],
        "strategic_relevance": "Relevant to lifecycle discipline: structured follow-ups, service coordination, operational clarity and stakeholder communication."
    },
    {
        "title": "AI Adoption Research – TPB with Trust Mediation",
        "capability": "AI-Powered Operations",
        "location": "Academic research",
        "context": "Research Methods / SmartPLS project",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1400&q=85",
        "summary": "Developed and analysed an AI adoption research model using the Theory of Planned Behavior with trust as a mediating variable.",
        "problem": "AI adoption is influenced by behavioural, trust, risk, self-efficacy and social expectation factors, requiring structured research modelling.",
        "role": "Designed the research model, reviewed literature, generated/analysed data and interpreted SmartPLS outputs.",
        "approach": ["Applied Theory of Planned Behavior constructs.", "Integrated trust as a mediating variable.", "Reviewed ABDC-rated literature.", "Analysed measurement and structural model outputs."],
        "frameworks": ["Theory of Planned Behavior", "PLS-SEM", "Trust Mediation", "Research Design"],
        "tools": ["SmartPLS", "Excel", "Literature review", "Statistical interpretation"],
        "outputs": ["Research framework.", "Measurement model interpretation.", "Structural model interpretation.", "Academic reflective report."],
        "strategic_relevance": "Relevant to AI transformation: understanding adoption, trust, behavioural barriers and AI-enabled work redesign."
    },
]

experience = [
    {
        "title": "Co-Founder & Operations Lead – Turfo",
        "period": "Jan 2024 – Jan 2025 | India",
        "details": "Managed operations, pricing, partnerships, vendors, utilisation tracking and revenue growth for a multi-sport play area. Achieved 3× revenue growth in 8 months and managed 35+ weekly engagements."
    },
    {
        "title": "Academic Specialist – Biology – BYJU’S",
        "period": "Nov 2021 – Apr 2024 | India",
        "details": "Delivered 2,000+ live sessions, supported learner engagement and contributed to 150+ monthly conversions through performance insights in a high-volume, target-driven EdTech environment."
    },
    {
        "title": "Associate Dentist – Happy Smile Dental Clinic",
        "period": "Oct 2019 – Oct 2021 | India",
        "details": "Managed patient communication, documentation, consultation flow, treatment explanation and care coordination across clinical stakeholders."
    },
    {
        "title": "Global MBA – SP Jain School of Global Management",
        "period": "Feb 2025 – Feb 2026 | Singapore · Dubai · India",
        "details": "Completed global business projects across fintech, healthcare, life sciences, enterprise transformation, AI product strategy, commercial modelling and operating model design."
    },
]

skills = {
    "Strategic Growth & Commercial Execution": [
        "Business ownership",
        "Ecosystem development",
        "Revenue growth",
        "Stakeholder activation",
        "Commercial follow-up",
        "Execution discipline"
    ],
    "Commercial Mechanics & Unit Economics": [
        "Pricing strategy",
        "AOV growth",
        "P&L visibility",
        "KPI tracking",
        "Financial modelling",
        "Commercial proposal logic"
    ],
    "AI-Powered Operations": [
        "AI-enabled MVP design",
        "Workflow automation",
        "Lifecycle logic",
        "Digital transformation",
        "AI adoption research",
        "KPI governance"
    ],
    "Market Intelligence": [
        "Market entry strategy",
        "Competitor benchmarking",
        "Ecosystem analysis",
        "Regulatory context",
        "Customer insights",
        "Growth opportunity mapping"
    ],
    "Tools": [
        "Excel",
        "PowerPoint",
        "Power BI",
        "Tableau",
        "SmartPLS",
        "Python",
        "Streamlit",
        "AI tools"
    ],
}

# ------------------------------------------------------------
# HELPER FUNCTIONS
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

            st.markdown("#### Strategic Relevance")
            st.markdown(f"""
            <div class="relevance-box">
                {project["strategic_relevance"]}
            </div>
            """, unsafe_allow_html=True)

def make_capability_bar_chart():
    df = pd.DataFrame(projects)
    counts = df["capability"].value_counts().reset_index()
    counts.columns = ["Capability", "Count"]
    fig = px.bar(
        counts,
        x="Capability",
        y="Count",
        text="Count",
        color="Capability",
        title="Project Coverage by Capability"
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#d4d4d8",
        title_font_color="#ffffff",
        xaxis_tickangle=-25,
        height=450,
        showlegend=False,
        margin=dict(l=20, r=20, t=60, b=110)
    )
    fig.update_traces(textposition="outside")
    return fig

def make_project_mix_donut():
    df = pd.DataFrame(projects)
    counts = df["capability"].value_counts().reset_index()
    counts.columns = ["Capability", "Count"]
    fig = px.pie(
        counts,
        names="Capability",
        values="Count",
        hole=0.52,
        title="Portfolio Mix by Strategic Theme"
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#d4d4d8",
        title_font_color="#ffffff",
        height=430,
        legend=dict(font=dict(color="#d4d4d8"))
    )
    return fig

def make_strategy_radar():
    categories = [
        "Revenue Growth",
        "Ecosystem Development",
        "AI Operations",
        "Unit Economics",
        "Market Intelligence",
        "Stakeholder Activation",
    ]
    scores = [9, 8, 8, 8, 8, 9]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=categories,
        fill="toself",
        name="Capability Strength",
        line=dict(color="#E53935", width=3),
        fillcolor="rgba(229,57,53,0.25)"
    ))
    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True, range=[0, 10], color="#a1a1aa"),
            angularaxis=dict(color="#d4d4d8")
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#d4d4d8",
        title=dict(text="Strategic Growth Capability Radar", font=dict(color="#ffffff")),
        showlegend=False,
        height=430
    )
    return fig

def render_home():
    st.markdown("""
    <div class="hero-shell">
        <div class="hero-content">
            <div class="name-chip">Shalini Arun Prakash · Strategic Growth Portfolio</div>
            <div class="hero-title">
                Building <span class="highlight-red">strategic growth</span><br>
                with execution, data and impact.
            </div>
            <div class="hero-subline">
                A professional portfolio spanning healthcare strategy, digital transformation,
                startup operations, AI-enabled business models, commercial execution, market intelligence
                and evidence-backed problem solving.
            </div>
            <span class="badge badge-red">Strategic Growth</span>
            <span class="badge badge-red">Business Ownership</span>
            <span class="badge badge-red">Commercial Execution</span>
            <span class="badge">AI-Powered Operations</span>
            <span class="badge">Market Intelligence</span>

            <div class="hero-grid">
                <div class="hero-mini-card">
                    <b>Commercial Builder</b>
                    <p>Startup operations, turnaround strategy and conversion support show revenue-oriented execution.</p>
                </div>
                <div class="hero-mini-card">
                    <b>Ecosystem Thinker</b>
                    <p>Fintech, healthcare and education projects show stakeholder ecosystems and activation logic.</p>
                </div>
                <div class="hero-mini-card">
                    <b>AI + Operations Fit</b>
                    <p>AI-enabled product, workflow transformation and adoption research show systems thinking.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    for i, (value, label) in enumerate(metrics[:4]):
        with cols[i]:
            render_metric_card(value, label)

    cols = st.columns(4)
    for i, (value, label) in enumerate(metrics[4:]):
        with cols[i]:
            render_metric_card(value, label)

    st.markdown('<div class="section-title">Strategic Fit</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A structured view of the capabilities behind the portfolio: business ownership, ecosystem development, commercial strategy, AI-powered operations, stakeholder activation and market intelligence.</div>',
        unsafe_allow_html=True
    )

    for i in range(0, len(strategic_fit_areas), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(strategic_fit_areas):
                with col:
                    item = strategic_fit_areas[i + j]
                    render_fit_card(item["area"], item["evidence"])

    st.markdown('<div class="section-title">Portfolio Visuals</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A visual summary of how the project portfolio maps to strategic growth capabilities.</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="visual-card">', unsafe_allow_html=True)
        st.plotly_chart(make_capability_bar_chart(), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="visual-card">', unsafe_allow_html=True)
        st.plotly_chart(make_project_mix_donut(), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="visual-card">', unsafe_allow_html=True)
    st.plotly_chart(make_strategy_radar(), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_strategic_fit():
    st.markdown('<div class="section-title">Strategic Fit Map</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A direct evidence map connecting experience and projects to high-growth business capabilities.</div>',
        unsafe_allow_html=True
    )

    for i in range(0, len(strategic_fit_areas), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(strategic_fit_areas):
                with col:
                    item = strategic_fit_areas[i + j]
                    render_fit_card(item["area"], item["evidence"])

def render_projects():
    st.markdown('<div class="section-title">Project Portfolio</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A detailed portfolio across healthcare strategy, digital transformation, startup operations, AI-enabled business models, commercial execution and market intelligence.</div>',
        unsafe_allow_html=True
    )

    capability_filter = st.selectbox(
        "Filter by capability",
        ["All"] + sorted(set([p["capability"] for p in projects]))
    )

    filtered = projects
    if capability_filter != "All":
        filtered = [p for p in projects if p["capability"] == capability_filter]

    st.write(f"Showing {len(filtered)} project(s).")

    for i in range(0, len(filtered), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(filtered):
                with col:
                    render_project_card(filtered[i + j])

def render_experience():
    st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">A coherent professional story across healthcare, EdTech, entrepreneurship and global business projects.</div>',
        unsafe_allow_html=True
    )

    for item in experience:
        st.markdown(f"""
        <div class="timeline-card">
            <div class="timeline-title">{item["title"]}</div>
            <div class="timeline-meta">{item["period"]}</div>
            <div>{item["details"]}</div>
        </div>
        """, unsafe_allow_html=True)

def render_skills():
    st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Skills grouped around strategic growth, commercial execution, AI-powered operations, market intelligence and stakeholder activation.</div>',
        unsafe_allow_html=True
    )

    for category, items in skills.items():
        st.markdown(f"### {category}")
        render_badges(items, "badge-red")
        st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Project-to-Capability Map</div>', unsafe_allow_html=True)

    mapping_data = []
    for p in projects:
        mapping_data.append({
            "Project": p["title"],
            "Capability": p["capability"],
            "Frameworks": ", ".join(p["frameworks"]),
            "Tools": ", ".join(p["tools"]),
            "Strategic Relevance": p["strategic_relevance"]
        })

    st.dataframe(pd.DataFrame(mapping_data), use_container_width=True, hide_index=True)

def render_proof_points():
    st.markdown('<div class="section-title">Proof Points</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-caption">Numbers and evidence that support strategic growth, execution discipline and business impact.</div>',
        unsafe_allow_html=True
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
        ("14+", "Projects mapped to strategic capabilities"),
        ("6", "Core capability areas: ownership, ecosystems, AI, unit economics, stakeholders, intelligence"),
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
            <p><b>Portfolio Focus:</b> Strategic Growth · Healthcare Strategy · Digital Transformation · Commercial Execution · AI-Powered Operations</p>
            <p><b>Location:</b> India</p>
            <p><b>Email:</b> shaliniarun23@gmail.com</p>
            <p><b>LinkedIn:</b> linkedin.com/in/shaliniarun</p>
            <br>
            <p><b>Professional narrative:</b> Strategic growth professional with healthcare, EdTech, startup operations, AI-enabled product strategy and global MBA project exposure.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="contact-card">
            <h3>Portfolio Use</h3>
            <p>This portfolio maps evidence from projects and experience to strategic growth, business ownership, commercial execution, AI-powered operations and stakeholder activation.</p>
            <br>
            <p><b>Full reports and confidential project documents are available only on request.</b></p>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------------------------
# TOP NAVIGATION
# ------------------------------------------------------------

st.markdown("""
<div style="padding: 0.9rem 0 1.2rem 0;">
    <div style="font-size: 1.65rem; font-weight: 950; color: #ffffff; text-transform: uppercase;">Shalini Arun Prakash</div>
    <div style="color:#a1a1aa; margin-top:0.25rem;">Strategic Growth · Healthcare Strategy · Digital Transformation · Commercial Execution · AI-Powered Operations</div>
</div>
""", unsafe_allow_html=True)

tab_home, tab_fit, tab_projects, tab_experience, tab_skills, tab_proof, tab_contact = st.tabs(
    ["Home", "Strategic Fit", "Projects", "Experience", "Skills", "Proof Points", "Contact"]
)

with tab_home:
    render_home()

with tab_fit:
    render_strategic_fit()

with tab_projects:
    render_projects()

with tab_experience:
    render_experience()

with tab_skills:
    render_skills()

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
