import streamlit as st
from pathlib import Path
import base64


PROFILE_PATH = Path(__file__).parent / "assets" / "profile.jpg"

with open(PROFILE_PATH, "rb") as image_file:
    profile_image = base64.b64encode(
        image_file.read()
    ).decode()

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Mayur Sawant | Python Developer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(99,102,241,0.12),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(14,165,233,0.10),
            transparent 25%
        ),
        #080b12;
    color: #f8fafc;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    text-align: center;
    padding: 85px 20px 65px;
}

.hero-badge {
    display: inline-block;
    padding: 8px 17px;
    border-radius: 50px;

    background: rgba(99,102,241,0.10);
    border: 1px solid rgba(129,140,248,0.35);

    color: #a5b4fc;
    font-size: 14px;
    font-weight: 600;

    margin-bottom: 28px;
}

.hero h1 {
    font-size: clamp(44px, 7vw, 78px);
    line-height: 1;
    font-weight: 800;
    letter-spacing: -4px;

    margin: 0;
}

.gradient-text {
    background: linear-gradient(
        90deg,
        #818cf8,
        #38bdf8,
        #22d3ee
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    max-width: 700px;
    margin: 28px auto;

    color: #94a3b8;

    font-size: 18px;
    line-height: 1.75;
}


/* ============================================================
   SECTIONS
   ============================================================ */

.section {
    margin-top: 75px;
    margin-bottom: 25px;
}

.section-label {
    color: #818cf8;

    font-family: 'JetBrains Mono', monospace;

    font-size: 13px;
    font-weight: 500;

    letter-spacing: 1px;

    margin-bottom: 8px;
}

.section-title {
    font-size: 34px;
    font-weight: 750;

    margin-bottom: 10px;
}

.section-description {
    color: #94a3b8;

    font-size: 16px;
    line-height: 1.7;

    max-width: 700px;
}


/* ============================================================
   ABOUT
   ============================================================ */

.about-card {
    background: rgba(15,23,42,0.72);

    border: 1px solid rgba(148,163,184,0.12);

    border-radius: 20px;

    padding: 30px;
}

.about-card p {
    color: #cbd5e1;

    font-size: 16px;

    line-height: 1.85;

    margin: 0 0 15px 0;
}

.about-card p:last-child {
    margin-bottom: 0;
}


/* ============================================================
   PROJECT CARDS
   ============================================================ */

.project-card {
    min-height: 375px;

    padding: 28px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(15,23,42,0.95),
            rgba(15,23,42,0.65)
        );

    border: 1px solid rgba(148,163,184,0.13);

    transition: all 0.25s ease;
}

.project-card:hover {
    transform: translateY(-5px);

    border-color: rgba(129,140,248,0.5);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.25);
}

.project-icon {
    width: 52px;
    height: 52px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: rgba(99,102,241,0.12);

    border-radius: 14px;

    font-size: 25px;

    margin-bottom: 20px;
}

.project-card h3 {
    margin: 0 0 13px 0;

    font-size: 21px;
}

.project-card p {
    color: #94a3b8;

    font-size: 14px;

    line-height: 1.7;
}

.tech {
    display: flex;
    flex-wrap: wrap;

    gap: 7px;

    margin-top: 20px;
}

.tech span {
    background: rgba(30,41,59,0.9);

    border: 1px solid rgba(148,163,184,0.12);

    color: #cbd5e1;

    padding: 5px 9px;

    border-radius: 7px;

    font-family: 'JetBrains Mono', monospace;

    font-size: 11px;
}


/* ============================================================
   SKILLS
   ============================================================ */

.skill-box {
    height: 100%;

    background: rgba(15,23,42,0.72);

    border: 1px solid rgba(148,163,184,0.12);

    border-radius: 17px;

    padding: 23px;
}

.skill-box h4 {
    margin: 0 0 15px 0;
}

.skill-item {
    color: #cbd5e1;

    padding: 7px 0;

    font-size: 14px;
}


/* ============================================================
   EDUCATION
   ============================================================ */

.timeline-card {
    border-left: 2px solid #6366f1;

    padding-left: 25px;

    margin-top: 20px;
}

.timeline-card h3 {
    margin: 0 0 8px 0;
}

.timeline-card p {
    color: #94a3b8;

    line-height: 1.7;
}


.profile-photo {
    width: 145px;
    height: 145px;

    object-fit: cover;

    border-radius: 50%;

    border: 3px solid rgba(129,140,248,0.65);

    box-shadow:
        0 0 0 8px rgba(99,102,241,0.08),
        0 15px 40px rgba(0,0,0,0.35);

    margin-bottom: 25px;
}

/* ============================================================
   CONTACT
   ============================================================ */

.contact-card {
    text-align: center;

    padding: 55px 30px;

    border-radius: 24px;

    background:
        radial-gradient(
            circle at center,
            rgba(99,102,241,0.15),
            transparent 60%
        ),
        rgba(15,23,42,0.8);

    border: 1px solid rgba(129,140,248,0.15);
}

.contact-card h2 {
    font-size: 36px;

    margin-bottom: 15px;
}

.contact-card p {
    color: #94a3b8;

    max-width: 600px;

    margin: auto;

    line-height: 1.7;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;

    margin-top: 70px;

    padding-top: 25px;

    border-top: 1px solid rgba(148,163,184,0.10);

    color: #64748b;

    font-size: 13px;
}

</style>
""")


# ============================================================
# YOUR INFORMATION
# ============================================================

GITHUB_URL = "https://github.com/mayur-sawant"

LINKEDIN_URL = "https://www.linkedin.com/in/YOUR_USERNAME"

EMAIL = "mayursawant565@gmail.com"


# ============================================================
# PROJECT LINKS
# ============================================================

PROJECT_LINKS = {

    "netrat":
        "https://github.com/mayur-sawant/NetRat",

    "loan":
        "https://github.com/YOUR_USERNAME/Loan-Prediction",

    "eco":
        "https://github.com/YOUR_USERNAME/Eco-Tracker",

    "house":
        "https://github.com/YOUR_USERNAME/House-Price-Prediction"
}


# ============================================================
# HERO
# ============================================================

st.html(f"""
<div class="hero">
    <img
    src="data:image/jpeg;base64,{profile_image}"
    class="profile-photo"
    >

    <div class="hero-badge">
        👋 Hello, I'm Mayur
    </div>

    <h1>
        Python Developer
        <br>
        <span class="gradient-text">
            with Machine Learning & AI
        </span>
    </h1>

    <p class="hero-subtitle">
        MCA graduate passionate about Python, Data Analytics,
        Machine Learning and Cybersecurity. I enjoy turning
        real-world problems into practical software solutions.
    </p>

</div>
""")


# ============================================================
# HERO BUTTONS
# ============================================================

c1, c2, c3, c4, c5 = st.columns(5)

with c2:
    st.link_button(
        "💻 GitHub",
        GITHUB_URL,
        use_container_width=True
    )

with c3:
    st.link_button(
        "🔗 LinkedIn",
        LINKEDIN_URL,
        use_container_width=True
    )

with c4:
    st.link_button(
        "📧 Contact Me",
        f"mailto:{EMAIL}",
        use_container_width=True
    )


# ============================================================
# ABOUT
# ============================================================

st.html("""
<div class="section">

    <div class="section-label">
        // ABOUT ME
    </div>

    <div class="section-title">
        Turning ideas into working projects.
    </div>

</div>

<div class="about-card">

    <p>
        I'm <b>Mayur Sawant</b>, an MCA graduate and Python
        developer interested in building practical applications
        using <b>Python, Data Analytics, Machine Learning
        and Cybersecurity</b>.
    </p>

    <p>
        My projects range from machine-learning based prediction
        systems to network traffic analysis and AI-powered
        wildlife identification.
    </p>

    <p>
        I particularly enjoy understanding how systems work
        underneath and then building something useful around
        that knowledge.
    </p>

    <p>
        Currently, I'm focused on strengthening my skills in
        <b>Python, SQL, Pandas, NumPy, Scikit-Learn,
        Git and backend development</b>.
    </p>

</div>
""")


# ============================================================
# PROJECT SECTION
# ============================================================

st.html("""
<div class="section">

    <div class="section-label">
        // FEATURED PROJECTS
    </div>

    <div class="section-title">
        Things I've built.
    </div>

    <div class="section-description">
        A selection of projects covering machine learning,
        cybersecurity, AI and data-driven applications.
    </div>

</div>
""")


# ============================================================
# PROJECT DATA
# ============================================================

projects = [

    {
        "icon": "🛡️",
        "title": "NetRat — Smart Packet Sniffer",
        "description":
            "A network traffic analysis system that captures "
            "packets, builds network flows and extracts traffic "
            "features for machine-learning based user activity "
            "classification.",
        "tech": [
            "Python",
            "TShark",
            "Pandas",
            "Scikit-Learn",
            "Network Analysis",
            "ML"
        ],
        "link": PROJECT_LINKS["netrat"]
    },

    {
        "icon": "🏦",
        "title": "Loan Approval Prediction",
        "description":
            "A machine learning project that predicts loan "
            "approval using applicant information and financial "
            "attributes. Includes preprocessing, encoding, "
            "model training and prediction workflow.",
        "tech": [
            "Python",
            "Pandas",
            "NumPy",
            "Scikit-Learn",
            "Machine Learning"
        ],
        "link": PROJECT_LINKS["loan"]
    },

    {
        "icon": "🌿",
        "title": "Eco Tracker AI Agent",
        "description":
            "An AI-powered wildlife identification system "
            "that analyzes images, identifies species and "
            "checks conservation information to provide "
            "useful ecological insights.",
        "tech": [
            "Python",
            "Gemini",
            "AI",
            "Image Analysis",
            "IUCN Data"
        ],
        "link": PROJECT_LINKS["eco"]
    },

    {
        "icon": "🏠",
        "title": "House Price Prediction",
        "description":
            "A machine learning project designed to estimate "
            "house prices from property-related features while "
            "demonstrating the complete ML workflow from "
            "preprocessing to prediction.",
        "tech": [
            "Python",
            "Pandas",
            "NumPy",
            "Scikit-Learn",
            "Regression"
        ],
        "link": PROJECT_LINKS["house"]
    }

]


# ============================================================
# PROJECT CARD FUNCTION
# ============================================================

def project_card(project):

    tech_html = ""

    for tech in project["tech"]:
        tech_html += f"<span>{tech}</span>"

    st.html(f"""
    <div class="project-card">

        <div class="project-icon">
            {project["icon"]}
        </div>

        <h3>
            {project["title"]}
        </h3>

        <p>
            {project["description"]}
        </p>

        <div class="tech">
            {tech_html}
        </div>

    </div>
    """)

    st.link_button(
        "View Project →",
        project["link"],
        use_container_width=True
    )


# ============================================================
# PROJECT GRID
# ============================================================

col1, col2 = st.columns(2)

with col1:
    project_card(projects[0])

with col2:
    project_card(projects[1])


st.write("")


col1, col2 = st.columns(2)

with col1:
    project_card(projects[2])

with col2:
    project_card(projects[3])


# ============================================================
# SKILLS
# ============================================================

st.html("""
<div class="section">

    <div class="section-label">
        // TECHNICAL SKILLS
    </div>

    <div class="section-title">
        My toolbox.
    </div>

</div>
""")


skill_columns = st.columns(5)


skills = [

    (
        "🐍 Programming",
        [
            "Python",
            "C",
            "SQL",
            "Bash"
        ]
    ),

    (
        "📊 Data & ML",
        [
            "Pandas",
            "NumPy",
            "Matplotlib",
            "Scikit-Learn"
        ]
    ),

    (
            "📊 Data Visualization",
            [
                "PowerBI",
                "Tableu",
                "Exel"
            ]
        ),

    (
        "🌐 Web & Backend",
        [
            "HTML",
            "CSS",
            "Bootstrap",
            "Streamlit"
        ]
    ),

    (
        "🛠️ Cyber Security",
        [
             "Network analysis", 
             "Vulnerability detection", 
             "Risk Management", 
             "Penetration Testing"
        ]
    )

]


for column, (title, items) in zip(skill_columns, skills):

    items_html = ""

    for item in items:
        items_html += f"""
        <div class="skill-item">
            ▹ {item}
        </div>
        """

    with column:

        st.html(f"""
        <div class="skill-box">

            <h4>
                {title}
            </h4>

            {items_html}

        </div>
        """)


# ============================================================
# EDUCATION
# ============================================================

st.html("""
<div class="section">

    <div class="section-label">
        // EDUCATION
    </div>

    <div class="section-title">
        Academic background.
    </div>

</div>

<div class="timeline-card">

    <h3>
        Master of Computer Applications (MCA)
    </h3>

    <p>
        CGPA: <b>8.12</b>
    </p>

    <p>
        Focus areas: Programming, Databases,
        Data Analytics, Machine Learning
        and Computer Networks.
    </p>

</div>
""")


# ============================================================
# CURRENTLY LEARNING
# ============================================================

st.html("""
<div class="section">

    <div class="section-label">
        // CURRENTLY LEARNING
    </div>

    <div class="section-title">
        Always building. Always learning.
    </div>

</div>
""")


learning = st.columns(3)


with learning[0]:

    st.html("""
    <div class="skill-box">

        <h4>
            🤖 Machine Learning & AI
        </h4>

        <div class="skill-item">
            Model evaluation
        </div>

        <div class="skill-item">
            Feature engineering
        </div>

        <div class="skill-item">
            Scikit-Learn
        </div>

    </div>
    """)


with learning[1]:

    st.html("""
    <div class="skill-box">

        <h4>
            🐍 Python Development
        </h4>

        <div class="skill-item">
            OOP
        </div>

        <div class="skill-item">
            Backend development
        </div>

        <div class="skill-item">
            APIs
        </div>

    </div>
    """)


with learning[2]:

    st.html("""
    <div class="skill-box">

        <h4>
            📈 Data Analytics
        </h4>

        <div class="skill-item">
            SQL
        </div>

        <div class="skill-item">
            Pandas
        </div>

        <div class="skill-item">
            Data visualization
        </div>

    </div>
    """)


# ============================================================
# CONTACT
# ============================================================

st.html("""
<div class="section">

    <div class="section-label">
        // GET IN TOUCH
    </div>

</div>

<div class="contact-card">

    <h2>
        Let's build something useful.
    </h2>

    <p>
        I'm interested in Python development, data,
        machine learning & AI and technology-driven projects.
        If you'd like to discuss a project, opportunity
        or collaboration, feel free to reach out.
    </p>

</div>
""")


st.write("")


contact = st.columns(3)


with contact[0]:

    st.link_button(
        "💻 GitHub",
        GITHUB_URL,
        use_container_width=True
    )


with contact[1]:

    st.link_button(
        "🔗 LinkedIn",
        LINKEDIN_URL,
        use_container_width=True
    )


with contact[2]:

    st.link_button(
        "📧 Email",
        f"mailto:{EMAIL}",
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">

    Built with Python & Streamlit
    •
    © 2026 Mayur Sawant

</div>
""")