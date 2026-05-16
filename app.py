import streamlit as st
import numpy as np
from vision_engine import LogiVisionEngine
from decision_orchestrator import LogiDecisionOrchestrator

# Initialize structural engine nodes
vision_unit = LogiVisionEngine()

# Set up browser page styling configurations
st.set_page_config(page_title="LogiVision AI Control Room", layout="wide")

# Sidebar - Edge Telemetry Controls
st.sidebar.markdown("### 🔑 Authentication Matrix")
openai_api_key = st.sidebar.text_input(
    "OpenAI Production Secret Key", 
    type="password", 
    placeholder="sk-...",
    help="Provide your active OpenAI token to power the logistics orchestrator logic."
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🌍 Real-Time Regional Context")

traffic_profile = st.sidebar.selectbox(
    "Metro Traffic Status",
    ["Low (Clear Flow)", "Moderate (Steady)", "High (Gridlock Congestion)"],
    index=2
)

weather_profile = st.sidebar.selectbox(
    "Local Weather Status",
    ["Clear Skies / Dry", "Heavy Fog / Low Visibility", "Monsoons Heavy Downpour"],
    index=2
)

fleet_profile = st.sidebar.selectbox(
    "Assigned Fleet Asset",
    ["Electric 2-Wheeler (EV)", "Standard 3-Wheeler Auto", "Refrigerated Medium Truck"],
    index=0
)

language_profile = st.sidebar.selectbox(
    "Target Regional Localization",
    ["Telugu", "Hindi", "Tamil", "English"],
    index=0
)

# Main Application Header Layout Panel
st.title("👁️ LogiVision AI - Autonomous Dark Store Infrastructure Engine")
st.markdown("---")

# Main Interface Grid Split
column_left, column_right = st.columns([1, 1.2])

with column_left:
            st.subheader("📸 Live Web-Camera Gateway")
            
            # This instantly opens his phone camera or laptop webcam directly inside the webpage!
            camera_image = st.camera_input("Position the product label or barcode clearly in frame:")
            
            # Let them type or match a barcode to trigger the analytics engine
            barcode_digits = st.text_input("Confirm item SKU digits:", value="8901207001761")
            
            if camera_image and st.button("RUN LOGISTICS ANALYSIS MATRIX", use_container_width=True):
                with st.spinner("Processing optical telemetry..."):
                    telemetry_stream = vision_unit.process_cloud_image(barcode_digits)
                
                st.balloons()
                st.success("Analysis complete!")

                st.markdown("#### **Neural Net Spatial Extractions**")
                m1, m2 = st.columns(2)
                m1.metric("Predicted Item Category", telemetry_stream['item_category'])
                m2.metric("Prediction Confidence", f"{telemetry_stream['inference_confidence']*100:.2f}%")
                
                m3, m4 = st.columns(2)
                m3.metric("Structural Verification Check", telemetry_stream['structural_audit'])
                m4.metric("Days Until Item Expiry", f"{telemetry_stream['expiration_horizon_days']} Days")
                
                context_bundle = {
                    "traffic_index": traffic_profile,
                    "weather_condition": weather_profile,
                    "transport_medium": fleet_profile,
                    "target_language": language_profile
                }
                
                with column_right:
                    st.subheader("🧠 Cognitive Supply-Chain Decision System")
                    if not openai_api_key:
                        st.error("Provide your OpenAI key in the sidebar to run the coordinator.")
                    else:
                        with st.spinner("Calculating alternative routing..."):
                            orchestrator_unit = LogiDecisionOrchestrator(api_key=openai_api_key)
                            executive_decision = orchestrator_unit.generate_routing_strategy(
                                vision_data=telemetry_stream,
                                operational_context=context_bundle
                            )
                            st.markdown("#### **AI Operations Briefing Directives**")
                            st.write(executive_decision)