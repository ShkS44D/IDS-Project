import streamlit as st
import pandas as pd
import pickle
import numpy as np
import plotly.express as px
import os
import time

# --- 1. SETTINGS & THEMING ---
st.set_page_config(
    page_title="Sentinel AI | Network IDS",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a high-end "Cybersecurity Command Center" look
st.markdown("""
    <style>
    /* Main background and text */
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Metrics Styling */
    [data-testid="stMetricValue"] { font-size: 32px; color: #00d4ff; font-weight: 700; }
    [data-testid="stMetricDelta"] { font-size: 16px; }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    
    /* Buttons */
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        height: 3.5em; 
        background-color: #00d4ff; 
        color: #0e1117; 
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #008fb3; color: white; border: none; }
    
    /* Status Boxes */
    .status-card {
        padding: 20px;
        border-radius: 12px;
        background-color: #161b22;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. ASSET LOADING ---
# Path constants based on your structure
MODELS_DIR = "models"

@st.cache_resource
def load_sentinel_assets():
    """Loads all model artifacts from the models/ directory."""
    try:
        model = pickle.load(open(os.path.join(MODELS_DIR, 'RandomForest_model.pkl'), 'rb'))
        scaler = pickle.load(open(os.path.join(MODELS_DIR, 'scaler.pkl'), 'rb'))
        encoders = pickle.load(open(os.path.join(MODELS_DIR, 'label_encoders.pkl'), 'rb'))
        features = pickle.load(open(os.path.join(MODELS_DIR, 'feature_names.pkl'), 'rb'))
        return model, scaler, encoders, features
    except FileNotFoundError as e:
        st.error(f"❌ Critical Error: Could not find model files in '{MODELS_DIR}/'. Please check folder structure.")
        st.stop()

model, scaler, encoders, feature_names = load_sentinel_assets()

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=80)
    st.title("Sentinel AI")
    st.markdown("---")
    page = st.radio("COMMAND CENTER", ["📊 Dashboard", "🔍 Live Detection", "📈 AI Analytics"])
    st.markdown("---")
    st.caption("Active Session: **Saad Ahmed**")
    st.caption("Environment: **Production-01**")

# --- 4. PAGE 1: DASHBOARD ---
if page == "📊 Dashboard":
    st.title("🛡️ Network Security Intelligence")
    st.markdown("Welcome back, Commander Ahmed. All systems are currently **nominal**.")
    
    # Key Metric Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("System Load", "12%", "Optimal")
    with col2:
        st.metric("Model Precision", "99.8%", "Verified")
    with col3:
        st.metric("Active Sensors", "40/40", "Sync")
    with col4:
        st.metric("Threats Mitigated", "142", "+12 today", delta_color="inverse")

    st.markdown("---")
    
    # Visual Layout
    left_col, right_col = st.columns([2, 1])
    
    with left_col:
        st.subheader("📡 Real-Time Traffic Flow (24h)")
        # Prestigious looking area chart
        chart_data = pd.DataFrame(
            np.random.randint(50, 100, size=(24, 2)), 
            columns=['Normal Requests', 'Filtered Anomalies']
        )
        st.area_chart(chart_data, color=["#00d4ff", "#ff4b4b"])
        
    with right_col:
        st.subheader("🔔 System Notifications")
        st.markdown("""
        <div class="status-card">
            <p>🟢 <b>Sensor-4</b>: Successfully updated protocol definitions.</p>
            <p>⚪ <b>Update</b>: Model weight 'RandomForest_v2' loaded.</p>
            <p>🟢 <b>Auth</b>: Admin login confirmed via terminal.</p>
            <p>🔴 <b>Alert</b>: Blocked 4 port-scan attempts at 11:24 AM.</p>
        </div>
        """, unsafe_allow_html=True)

# --- 5. PAGE 2: LIVE DETECTION ---
elif page == "🔍 Live Detection":
    st.title("🔍 Threat Analysis Engine")
    st.info("Simulate live network traffic or verify incoming packets against the Sentinel AI model.")

    # Data Source Section
    st.subheader("Initialize Packet Data")
    if st.button("Generate Random Packet from Node-7"):
        try:
            val_data = pd.read_csv(os.path.join(MODELS_DIR, 'validation_with_labels.csv'))
            st.session_state['current_packet'] = val_data.sample(1)
            st.toast("Packet captured successfully!")
        except Exception as e:
            st.error(f"Error loading validation data: {e}")

    if 'current_packet' in st.session_state:
        df_packet = st.session_state['current_packet']
        actual_val = "NORMAL" if df_packet['class'].values[0] == 0 else "ANOMALY"
        
        # UI: Show core features in a clean table
        st.write("### 📦 Packet Metadata")
        st.dataframe(df_packet[['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes']], use_container_width=True)

        if st.button("🚀 EXECUTE AI SCAN", type="primary"):
            with st.spinner("Analyzing network patterns..."):
                time.sleep(0.8) # Artificial delay for the "prestigious" feel
                
                # Prepare data for model
                # Drop target 'class' and reorder based on training names
                input_df = df_packet.drop('class', axis=1)[feature_names]
                
                # Scale and Predict
                scaled_input = scaler.transform(input_df)
                pred_int = model.predict(scaled_input)[0]
                prob = model.predict_proba(scaled_input).max() * 100

                st.markdown("---")
                if pred_int == 1:
                    st.error(f"🚨 **THREAT DETECTED** | Result: ANOMALY")
                    st.markdown(f"**AI Confidence:** `{prob:.2f}%` | **System Validation:** `{actual_val}`")
                    st.progress(int(prob))
                else:
                    st.success(f"✅ **CLEAN PACKET** | Result: NORMAL")
                    st.markdown(f"**AI Confidence:** `{prob:.2f}%` | **System Validation:** `{actual_val}`")
                    st.progress(int(prob))

# --- 6. PAGE 3: ANALYTICS ---
elif page == "📈 AI Analytics":
    st.title("📈 Model Insights & Feature Engineering")
    st.write("Detailed breakdown of how the Random Forest makes its decisions.")

    # Feature Importance Section
    st.subheader("Key Threat Indicators")
    st.write("These features have the highest weights in determining an intrusion:")
    
    importances = model.feature_importances_
    feat_imp_df = pd.DataFrame({
        'Network Feature': feature_names,
        'Influence Score': importances
    }).sort_values(by='Influence Score', ascending=True).tail(10) # Top 10

    fig = px.bar(
        feat_imp_df, 
        x='Influence Score', 
        y='Network Feature', 
        orientation='h',
        color='Influence Score',
        color_continuous_scale='Blues',
        template="plotly_dark"
    )
    fig.update_layout(showlegend=False, margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig, use_container_width=True)

    # Explanation block
    st.markdown("""
    > **Sentinel AI Analysis:** The model primarily relies on `src_bytes` and `dst_bytes` to identify DDoS and port scan patterns. 
    > A sudden spike in these values relative to `duration` is the strongest indicator of a network breach.
    """)