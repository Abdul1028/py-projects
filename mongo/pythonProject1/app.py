import streamlit as st
from typing import List


st.set_page_config(page_title="Instagram Feed Control", page_icon="📊", layout="wide")

SESSION_PROGRESS = 72
DAILY_TARGET_PROGRESS = 88

st.markdown(
    """
    <style>
    .stApp {background-color: #0e1117; color: #f3f4f6;}
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    .card {
        background: #161b22;
        border: 1px solid #2d333b;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 0.75rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def toggle_widget(label: str, key: str, value: bool = True) -> bool:
    if hasattr(st, "toggle"):
        return st.toggle(label, value=value, key=key)
    return st.checkbox(label, value=value, key=key)


def render_tab(title: str, hint: str, examples: List[str], key_prefix: str) -> None:
    left, right = st.columns([2.2, 1])
    with left:
        st.markdown(f"### {title} Training")
        st.text_input("Target", placeholder=hint, key=f"{key_prefix}_target")
        st.selectbox(
            "Content Preference",
            ["Reels", "Posts", "Stories", "Mixed"],
            key=f"{key_prefix}_content",
        )
        st.multiselect(
            "Audience Regions",
            ["Global", "North America", "Europe", "South Asia", "MENA"],
            default=["Global"],
            key=f"{key_prefix}_regions",
        )
        st.slider("Intensity", 1, 10, 6, key=f"{key_prefix}_intensity")
        c1, c2, c3 = st.columns(3)
        with c1:
            toggle_widget("Auto-like", key=f"{key_prefix}_autolike")
        with c2:
            toggle_widget("Auto-comment", key=f"{key_prefix}_autocomment", value=False)
        with c3:
            toggle_widget("Auto-follow", key=f"{key_prefix}_autofollow", value=False)
        if st.button("Start Training", key=f"{key_prefix}_start"):
            st.success("Training simulation started. Preview updated.")

    with right:
        st.markdown("### Session Status")
        st.metric("Estimated Reach", "42.8K", "+12%")
        st.metric("Engagement Lift", "8.4%", "+1.1%")
        st.progress(SESSION_PROGRESS, text="Simulation Progress")

    st.markdown("#### Dummy Preview")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown(
            f"<div class='card'><strong>Top Signal</strong><br>{examples[0]}</div>",
            unsafe_allow_html=True,
        )
    with p2:
        st.markdown(
            f"<div class='card'><strong>Secondary Signal</strong><br>{examples[1]}</div>",
            unsafe_allow_html=True,
        )
    with p3:
        st.markdown(
            f"<div class='card'><strong>Suggested Boost</strong><br>{examples[2]}</div>",
            unsafe_allow_html=True,
        )


st.title("Instagram Feed Control Dashboard")
st.caption("Frontend-only prototype for feed training controls and preview simulation.")

with st.sidebar:
    st.markdown("## Profile & Settings")
    st.selectbox("Profile", ["@creator_alpha", "@brand_hub", "@growth_lab"])
    st.selectbox("Theme", ["Dark"], index=0)
    st.select_slider("Automation Window", options=["Low", "Medium", "High"], value="Medium")
    toggle_widget("Safe Mode", "safe_mode", value=True)
    toggle_widget("Use conservative pacing", "pacing_mode", value=True)
    st.button("Save Settings", use_container_width=True)
    st.divider()
    st.metric("Profile Health", "91/100", "+3")
    st.progress(DAILY_TARGET_PROGRESS, text="Daily Target Completion")

top_cols = st.columns(4)
top_cols[0].metric("Active Training Sets", "4")
top_cols[1].metric("Predicted New Followers", "1,240", "+9%")
top_cols[2].metric("Avg. Engagement Score", "7.8/10", "+0.4")
top_cols[3].metric("Risk Index", "Low", "-2")

st.markdown("---")
tabs = st.tabs(["By Audio", "By Hashtag", "By Likes", "By Followers"])

with tabs[0]:
    render_tab(
        "By Audio",
        "e.g. dreamy synthwave",
        ["Audio trend: Retro Waves", "Reels completion up by 14%", "Boost creators using this sound"],
        "audio",
    )
with tabs[1]:
    render_tab(
        "By Hashtag",
        "e.g. #streetstyle",
        ["Hashtag cluster: #streetstyle", "Audience overlap: Fashion (63%)", "Increase reel mix by 20%"],
        "hashtag",
    )
with tabs[2]:
    render_tab(
        "By Likes",
        "e.g. users who liked @designdaily",
        ["Like source: @designdaily", "Intent confidence: High", "Prioritize design niche creators"],
        "likes",
    )
with tabs[3]:
    render_tab(
        "By Followers",
        "e.g. followers of @fitnesscoach",
        ["Follower similarity: 78%", "Best posting hour: 7 PM", "Test stronger call-to-action"],
        "followers",
    )
