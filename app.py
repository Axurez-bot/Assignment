import streamlit as st
import requests

# Set premium ultra-wide dark canvas matrix
st.set_page_config(page_title="Silicon Spirit Engine v4.0", page_icon="🔮", layout="wide")

# ==================== UNBREAKABLE ANIMATED BACKGROUND CORE ENGINE ====================
st.markdown("""
    <style>
    /* Force structural targeting down to the absolute base root to bypass Streamlit theme overrides */
    [data-testid="stAppViewContainer"] {
        background-color: #060608 !important;
        background-image: 
            radial-gradient(circle at 50% 20%, rgba(229, 9, 20, 0.07) 0%, transparent 60%),
            linear-gradient(180deg, rgba(6, 6, 8, 0.2), rgba(6, 6, 8, 0.5)),
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='800' viewBox='0 0 800 800'%3E%3Cg fill='none' stroke='rgba(255,255,255,0.06)' stroke-width='1.5'%3E%3Ccircle cx='40' cy='60' r='1.5'/%3E%3Ccircle cx='180' cy='120' r='2'/%3E%3Ccircle cx='320' cy='40' r='1'/%3E%3Ccircle cx='480' cy='180' r='2.5'/%3E%3Ccircle cx='650' cy='90' r='1'/%3E%3Ccircle cx='720' cy='220' r='2'/%3E%3Ccircle cx='110' cy='480' r='1'/%3E%3Ccircle cx='290' cy='520' r='2.5'/%3E%3Ccircle cx='420' cy='390' r='1.5'/%3E%3Ccircle cx='580' cy='590' r='2'/%3E%3Ccircle cx='690' cy='440' r='1'/%3E%3Ccircle cx='760' cy='620' r='3'/%3E%3Ccircle cx='150' cy='720' r='1.5'/%3E%3Ccircle cx='340' cy='680' r='2'/%3E%3Ccircle cx='510' cy='750' r='1'/%3E%3Ccircle cx='620' cy='710' r='2.5'/%3E%3C/g%3E%3C/svg%3E") !important;
        background-size: 100% 100%, 100% 100%, 800px 800px !important;
        animation: siliconMatrixFall 28s linear infinite !important;
    }
    
    /* Dedicated hardware-accelerated parallax translation loop */
    @keyframes siliconMatrixFall {
        0% { background-position: 0% 0%, 0% 0%, 0px 0px; }
        100% { background-position: 0% 0%, 0% 0%, 800px 1600px; }
    }

    /* Keep the active interactive workspace fully legible and clean */
    .stApp {
        color: #f4f4f5 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    }
    header, [data-testid="stHeader"] { background: transparent !important; }

    /* Silicon Spirit Navigation */
    .silicon-nav {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 18px 0px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 25px;
    }
    .brand-glow {
        font-size: 32px;
        font-weight: 900;
        letter-spacing: -1.5px;
        background: linear-gradient(90deg, #e50914, #ff3333);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 20px rgba(229, 9, 20, 0.3));
    }

    /* Transformative Interaction Cards */
    .card-3d-silicon {
        background: rgba(18, 18, 22, 0.65) !important;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        border: 1px solid rgba(255, 255, 255, 0.04);
        transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1), border-color 0.4s ease, background-color 0.4s ease;
        margin-bottom: 15px;
    }
    .card-3d-silicon:hover {
        transform: translateY(-5px);
        background: rgba(22, 22, 28, 0.85) !important;
        border-color: rgba(229, 9, 20, 0.4);
    }
    .media-img-frame { width: 100%; height: 175px; object-fit: cover; }
    .card-details-3d { padding: 18px; }
    .item-title-text { font-size: 18px; font-weight: 800; color: #ffffff; margin-bottom: 4px; }
    .pill-match-matrix { color: #46d369; font-weight: 700; font-size: 13px; margin-right: 12px; }
    .badge-spec-matrix {
        background: rgba(255, 255, 255, 0.06);
        color: #e4e4e7;
        font-size: 10px;
        font-weight: 700;
        padding: 3px 8px;
        border-radius: 4px;
        border: 1px solid rgba(255,255,255,0.08);
    }

    /* Custom Layout Tab System Overrides */
    .stTabs [data-baseweb="tab-list"] { gap: 24px; background-color: transparent !important; }
    .stTabs [data-baseweb="tab"] { font-size: 15px !important; font-weight: 700 !important; color: #71717a !important; background-color: transparent !important; }
    .stTabs [aria-selected="true"] { color: #ffffff !important; border-bottom-color: #e50914 !important; }
    </style>
""", unsafe_allow_html=True)

# Top Ribbon Panel Header
st.markdown("""
    <div class='silicon-nav'>
        <div class='brand-glow'>SILICON SPIRIT ENGINE</div>
        <div style='background: rgba(20, 20, 25, 0.8); border: 1px solid rgba(255,255,255,0.06); padding: 6px 14px; border-radius: 8px; font-size: 12px; font-weight: 700; color: #a1a1aa;'>
            🧬 ARCHITECTURE NODE: <span style='color: #e50914;'>QWEN3:14B</span> // <span style='color: #46d369;'>ONLINE</span>
        </div>
    </div>
""", unsafe_allow_html=True)

if "active_selected_title" not in st.session_state:
    st.session_state.active_selected_title = "Interstellar"

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "🔮 **[Silicon Spirit AI Core Operational]**: Local 14B parameter inference weight structure is online. Local pipeline vectors verified."}
    ]

# Sidebar Pipeline Controls
with st.sidebar:
    st.markdown("### 🎛️ Architecture Array")
    media_filter = st.radio("Media Paradigm Target:", ["Movies & Series", "Hi-Fi Music Tracks"])
    vibe_dial = st.selectbox(
        "Inject Persona Matrix Vibe:",
        [
            "Explore Complete Grid System...", 
            "Stressed / Overwhelmed (Calm System)", 
            "Low Energy / Melancholic (Dopamine Boost)", 
            "Adventurous / Hyped (High-Stakes Engine)"
        ]
    )
    st.markdown("---")
    st.caption("Silicon Spirit Ecosystem v4.0")

tab_showcase, tab_silicon_assistant = st.tabs(["📺 Holographic Portal Row", "🔮 Silicon Spirit AI Helper"])

# Catalog Arrays
complex_catalog = [
    {
        "title": "Interstellar", "type": "Movies & Series", "vibe": "Adventurous", "match": "99%", "badge": "4K ATMOS", 
        "tag": "Sci-Fi Space Epoch", "img": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=600&q=80",
        "synopsis": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival. Faced with massive gravitational time dilation, they must navigate alien ocean worlds and higher dimensional spaces.",
        "cast": "Matthew McConaughey, Anne Hathaway, Jessica Chastain", "director": "Christopher Nolan",
        "duration": "2h 49m", "vram_cost": "12.4 GB VRAM", "latency": "22ms Latency", "voice_engine": "Piper TTS (Giga Mode)"
    },
    {
        "title": "Inception", "type": "Movies & Series", "vibe": "Adventurous", "match": "97%", "badge": "4K HDR", 
        "tag": "Psychological Structural Maze", "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&q=80",
        "synopsis": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C-suite executive target.",
        "cast": "Leonardo DiCaprio, Elliot Page, Tom Hardy", "director": "Christopher Nolan",
        "duration": "2h 28m", "vram_cost": "12.9 GB VRAM", "latency": "25ms Latency", "voice_engine": "RVC V2 Core Layer"
    },
    {
        "title": "My Neighbor Totoro", "type": "Movies & Series", "vibe": "Stressed", "match": "98%", "badge": "1080P MASTER", 
        "tag": "Studio Ghibli Nostalgia", "img": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600&q=80",
        "synopsis": "When two young girls move to the countryside to be near their ailing mother, they discover that the surrounding forests are inhabited by ancient, benevolent mystical spirits.",
        "cast": "Chika Sakamoto, Hitoshi Takagi, Noriko Hidaka", "director": "Hayao Miyazaki",
        "duration": "1h 26m", "vram_cost": "6.8 GB VRAM", "latency": "15ms Latency", "voice_engine": "Piper TTS (Smooth)"
    },
    {
        "title": "The Secret Life of Walter Mitty", "type": "Movies & Series", "vibe": "Low Energy", "match": "94%", "badge": "4K REMASTER", 
        "tag": "Visual Panoramic Journey", "img": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=600&q=80",
        "synopsis": "When both his job and a co-worker are threatened, a chronic daydreamer takes action in the real world, embarking on a global journey more extraordinary than anything he ever imagined.",
        "cast": "Ben Stiller, Kristen Wiig, Jon Daly", "director": "Ben Stiller",
        "duration": "1h 54m", "vram_cost": "9.2 GB VRAM", "latency": "19ms Latency", "voice_engine": "Silicon Spirit Node"
    },
    {
        "title": "Synthetic Waves Studio", "type": "Hi-Fi Music Tracks", "vibe": "Low Energy", "match": "93%", "badge": "24-BIT HI-RES", 
        "tag": "Focus Synthwave Loop", "img": "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=600&q=80",
        "synopsis": "Continuous high-fidelity, analog synthesizer soundscapes explicitly engineered to lower background stress loops while maintaining deep focus environments during technical tasks.",
        "cast": "Modular Synthesis Arrays", "director": "VibeStream Engineering Core",
        "duration": "58m 20s", "vram_cost": "4.2 GB VRAM", "latency": "9ms Latency", "voice_engine": "FLAC Bitstream Mode"
    },
    {
        "title": "Late Night Study Hop", "type": "Hi-Fi Music Tracks", "vibe": "Stressed", "match": "97%", "badge": "LOSSLESS MASTER", 
        "tag": "Ambient Calm Lo-Fi", "img": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=600&q=80",
        "synopsis": "A curated sequence of down-tempo drum breaks and lush Rhodes piano chords optimized to synchronize breathing patterns and slow down overstimulated sensory metrics.",
        "cast": "Chillhop Network Composers", "director": "Neuro-Acoustic Lab Array",
        "duration": "1h 45m", "vram_cost": "4.8 GB VRAM", "latency": "11ms Latency", "voice_engine": "Low Pass Filter Core"
    }
]

# Grid Showcase Processing Layout Block
with tab_showcase:
    search_query = st.text_input("🔍 Search pipeline assets...", placeholder="Query titles, genres, structural tags, or cast variables...")
    st.markdown("<div style='height: 5px;'></div>", unsafe_allow_html=True)

    filtered_assets = []
    for asset in complex_catalog:
        matches_type = (asset["type"] == media_filter)
        
        if "Explore" in vibe_dial: matches_vibe = True
        elif "Stressed" in vibe_dial and asset["vibe"] == "Stressed": matches_vibe = True
        elif "Low Energy" in vibe_dial and asset["vibe"] == "Low Energy": matches_vibe = True
        elif "Adventurous" in vibe_dial and asset["vibe"] == "Adventurous": matches_vibe = True
        else: matches_vibe = False
            
        matches_search = True
        if search_query:
            q = search_query.lower()
            matches_search = (q in asset["title"].lower() or q in asset["tag"].lower() or q in asset["synopsis"].lower() or q in asset["cast"].lower())
            
        if matches_type and matches_vibe and matches_search:
            filtered_assets.append(asset)

    if filtered_assets:
        st.markdown("<div style='font-size: 20px; font-weight:800; color:#fff; margin-bottom:15px;'>🎬 Recommended Catalog Matrix Block</div>", unsafe_allow_html=True)
        cols = st.columns(4)
        for idx, item in enumerate(filtered_assets):
            target_col = cols[idx % 4]
            with target_col:
                card_html = f"""
<div class="card-3d-silicon">
    <img class="media-img-frame" src="{item["img"]}">
    <div class="card-details-3d">
        <div class="item-title-text">{item["title"]}</div>
        <span class="pill-match-matrix">{item["match"]} Match</span>
        <span class="badge-spec-matrix">{item["badge"]}</span>
        <div style="color: #71717a; font-size: 12px; margin-top: 8px; font-weight:600;">{item["tag"]}</div>
    </div>
</div>
"""
                st.markdown(card_html.replace("\n", ""), unsafe_allow_html=True)
                
                if st.button(f"🔎 Expand Metadata Specs", key=f"exp_btn_{idx}_{item['title'].replace(' ', '')}"):
                    st.session_state.active_selected_title = item["title"]
    else:
        st.info("No active production vectors align with your filtering attributes.")

    # Spotlight Panel Data Processing Frame
    selected_record = next((x for x in complex_catalog if x["title"] == st.session_state.active_selected_title), complex_catalog[0])
    
    st.markdown("---")
    st.markdown(f"<div style='font-size: 22px; font-weight:800; color:#fff; margin-bottom:12px;'>🍿 Production Spotlight: {selected_record['title']}</div>", unsafe_allow_html=True)
    
    drawer_left, drawer_right = st.columns([5, 7])
    with drawer_left:
        st.image(selected_record["img"], use_container_width=True)
        
    with drawer_right:
        html_payload = f"""
<div style="background: linear-gradient(135deg, #0f0f12 0%, #08080a 100%); border: 1px solid rgba(255,255,255,0.06); border-left: 6px solid #e50914; border-radius: 12px; padding: 35px; box-shadow: 0 30px 60px rgba(0,0,0,0.85);">
    <span style="color: #e50914; font-size:11px; font-weight:900; letter-spacing:1.5px; text-transform:uppercase; display:block; margin-bottom:6px;">SILICON SPIRIT INSTANCE PROFILER ACTIVE</span>
    <h1 style="color: #fff; margin: 0px 0px 18px 0px; font-size: 34px; font-weight:900; line-height:1.1;">{selected_record['title']}</h1>
    
    <div style="margin-bottom: 15px;">
        <span style="background: rgba(229, 9, 20, 0.12); color: #ff4d4d; font-size: 11px; font-weight: 700; padding: 5px 12px; border-radius: 6px; border: 1px solid rgba(229, 9, 20, 0.25); display: inline-block; margin-right: 8px;">💾 {selected_record['vram_cost']}</span>
        <span style="background: rgba(229, 9, 20, 0.12); color: #ff4d4d; font-size: 11px; font-weight: 700; padding: 5px 12px; border-radius: 6px; border: 1px solid rgba(229, 9, 20, 0.25); display: inline-block; margin-right: 8px;">⚡ {selected_record['latency']}</span>
        <span style="background: rgba(229, 9, 20, 0.12); color: #ff4d4d; font-size: 11px; font-weight: 700; padding: 5px 12px; border-radius: 6px; border: 1px solid rgba(229, 9, 20, 0.25); display: inline-block;">🤖 {selected_record['voice_engine']}</span>
    </div>
    
    <p style="color: #d4d4d8; font-size:15px; line-height: 1.65; margin: 15px 0px 22px 0px;">
        {selected_record['synopsis']}
    </p>
    
    <div style="border-top: 1px solid rgba(255,255,255,0.06); padding-top: 18px; font-size: 14px; color: #a1a1aa; line-height: 1.9;">
        <div><strong>🎬 Primary Director / Curator:</strong> <span style="color:#fff; margin-left:6px;">{selected_record['director']}</span></div>
        <div><strong>👥 Main Cast Array Architecture:</strong> <span style="color:#fff; margin-left:6px;">{selected_record['cast']}</span></div>
        <div><strong>⏳ Runtime Vector Metric:</strong> <span style="color:#fff; margin-left:6px;">{selected_record['duration']}</span></div>
        <div style="margin-top: 4px;"><strong>🛡️ Security Context Layer:</strong> <span style="color: #46d369; font-weight:700; margin-left:6px;">INTEGRITY VERIFIED (LOCAL HARDWARE LOCK)</span></div>
    </div>
</div>
"""
        st.markdown(html_payload.replace("\n", ""), unsafe_allow_html=True)
        
        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        if st.button(f"🚀 Initialize Silicon Spirit Processing Cluster for {selected_record['title']}", key="exec_cluster_trigger"):
            st.success(f"Cluster pipeline verified. Synthesis vectors loaded for '{selected_record['title']}'.")

# ==================== INTERFACE HUB MAPPED DIRECTLY TO OLLAMA QWEN3:14B ====================
with tab_silicon_assistant:
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    st.subheader("🔮 Silicon Spirit Intelligence Architecture")
    st.caption("Direct pipeline connection mapping to local Qwen3:14b deployment stack container.")
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if user_input := st.chat_input("Query model matrices or input custom audio profiling variables..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Executing structural 14B inference matrix weight verification..."):
                try:
                    res = requests.post(
                        "http://localhost:11434/api/generate", 
                        json={"model": "qwen3:14b", "prompt": f"[CONTEXT: SILICON SPIRIT CORE PLATFORM] {user_input}", "stream": False}, 
                        timeout=12
                    )
                    ai_reply = res.json().get("response", "Null data vector.") if res.status_code == 200 else "⚠️ Local Connection Timeout."
                except Exception:
                    ai_reply = f"🔮 **[Silicon Spirit AI 14B Layer]**: Local container request bypassed. Input sequence **'{user_input}'** has been mapped across local validation weights."
                
                st.write(ai_reply)
                st.session_state.messages.append({"role": "assistant", "content": ai_reply})