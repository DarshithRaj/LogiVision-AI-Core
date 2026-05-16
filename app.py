import streamlit as st
from vision_engine import LogiVisionEngine
from decision_orchestrator import LogiDecisionOrchestrator

st.set_page_config(page_title="LogiVision AI Control Room", page_icon="👁️", layout="wide")

st.title("👁️ LogiVision AI — Autonomous Dark Store Infrastructure Engine")
st.markdown("---")

st.sidebar.header("🔑 Authentication & Node Security")
secret_key_input = st.sidebar.text_input("OpenAI Production Secret Key", type="password")

st.sidebar.markdown("---")
st.sidebar.header("🌍 Real-Time Regional Context")
traffic_profile = st.sidebar.selectbox("Metro Traffic Status", ["High (Gridlock Congestion)", "Moderate (Active Flows)", "Low (Free Route Clearance)"])
weather_profile = st.sidebar.selectbox("Local Weather Status", ["Monsoon Heavy Downpour", "Extreme Summer Wave", "Standard Stable Climate"])
fleet_profile = st.sidebar.selectbox("Assigned Fleet Asset", ["Electric 2-Wheeler (EV)", "Internal Combustion Scooter", "Hyper-local Pedestrian Delivery"])
language_profile = st.sidebar.selectbox("Target Regional Localization", ["Hindi", "Telugu", "Kannada", "Tamil", "English"])

if secret_key_input:
    try:
        vision_unit = LogiVisionEngine()
        orchestrator_unit = LogiDecisionOrchestrator(api_key=secret_key_input)
        
        column_left, column_right = st.columns(2)
        
        with column_left:
            st.subheader("📸 Live Hardware Edge-Camera Desk")
            st.write("Hold any packed product's barcode up to your laptop webcam and click the scan button below.")
            
            if st.button("ACTIVATE WEBCAM & SCAN BARCODE", use_container_width=True):
                with st.spinner("Webcam initializing... Hold product steady!"):
                    telemetry_stream = vision_unit.scan_via_webcam()
                
                if telemetry_stream['barcode_found']:
                    st.balloons()
                    st.success(f"Barcode successfully parsed!")
                else:
                    st.warning("Camera timed out without finding a barcode. Try holding it closer or under better lighting.")

                # ✅ FIXED: This blocks now sits inside the button trigger scope
                st.markdown("#### **Neural Net Spatial Extractions**")
                m1, m2 = st.columns(2)
                m1.metric("Predicted Item Category", telemetry_stream['item_category'])
                m2.metric("CNN Prediction Confidence", f"{telemetry_stream['inference_confidence']*100:.2f}%")
                
                m3, m4 = st.columns(2)
                m3.metric("Structural Verification Check", telemetry_stream['structural_audit'])
                m4.metric("Days Until Item Expiry", f"{telemetry_stream['expiration_horizon_days']} Days")
                
                context_bundle = {
                    "traffic_index": traffic_profile,
                    "weather_condition": weather_profile,
                    "transport_medium": fleet_profile,
                    "target_language": language_profile
                }
                
                # ✅ FIXED: The right column layout updates side-by-side inside the scan event
                with column_right:
                    st.subheader("🧠 Cognitive Supply-Chain Decision System")
                    with st.spinner("Calculating alternative routing and localized updates..."):
                        executive_decision = orchestrator_unit.generate_routing_strategy(
                            vision_data=telemetry_stream,
                            operational_context=context_bundle
                        )
                        st.markdown("#### **AI Operations Briefing Directives**")
                        st.write(executive_decision)

    except Exception as e:
        st.error(f"System Error: {str(e)}")
else:
    st.info("Provide your OpenAI Production Secret Key in the left sidebar configuration block to clear security authorization and launch dashboard systems.")