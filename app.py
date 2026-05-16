import streamlit as st
from vision_engine import LogiVisionEngine
from decision_orchestrator import LogiDecisionOrchestrator

#Configuring high density layout
st.set_page_config(page_title="LogiVision AI Control Room",page_icon="👁️",layout="wide")
st.title("👁️LogiVision AI - Autonomous Dark Store Infrastructure Engine")
st.markdown("---")
#Enterprise Sidebar Configuration for Environment Control Variables
st.sidebar.header("🔑Authentication & Node Security")
secret_key_input = st.sidebar.text_input("OpenAI Production Secret Key",type="password",help="Input your authorization key to instantiate the reasoning modules.")

st.sidebar.markdown("---")
st.sidebar.header("🌍 Real-Time Regional Context")
traffic_profile = st.sidebar.selectbox("Metro Traffic Status",["High (Gridlock Congestion)","Moderate (Active Flows)","Low(Free Route Clearance)"])
weather_profile = st.sidebar.selectbox("Local Weather Status", ["Monsoosn Heavy Downpour","Extreme Summer Wave","Standard Stable Climate"])
fleet_profile = st.sidebar.selectbox("Assigned Fleet Asset",["Electric 2-Wheeler (EV)","Internal Combustion Scooter","Hyper-local Pedestrian Delivery"])
language_profile = st.sidebar.selectbox("Target Regional Localization",["Hindi","Telugu","Kannada","Tamil","English"])
#Instantiate Engines if security key is validated
if secret_key_input:
    try:
        vision_unit = LogiVisionEngine()
        orchestrator_unit = LogiDecisionOrchestrator(api_key=secret_key_input)

        #UI Action workforce Grid layout split 50/50
        column_left,column_right = st.columns(2)
        with column_left:
            st.subheader("📸 Automated Edge-Camera Audit Desk")
            st.info("System tracking ready.Trigger a scan package simulation to process the item payload.")
            
            if st.button("EXECUTE CONVOLUTION SCAN SIMULATION",use_container_width=True):
                #Run the TensorFlow processing unit
                telemetry_stream = vision_unit.audit_package_stream()

                #Render results to the screen nicely using structured metrics panels
                st.markdown("### **Neural Net Spatial Extractions**")
                metric_row_1,metric_row_2 = st.columns(2)
                metric_row_1.metric("Predicted Item Category", telemetry_stream['item_category'])
                metric_row_2.metric("CNN Prediction Confidence",f"{telemetry_stream['inference_confidence']*100:.2f}%")


                metric_row_3,metric_row_4 = st.columns(2)
                metric_row_3.metric("Structural Verification Check",telemetry_stream['structural_audit'])
                metric_row_4.metric("Days Until Item Expiry",f"{telemetry_stream['expiration_horizon_days']}Days")

                #Bundle the live environmental fields chosen in the sidebar
                context_bundle = {
                    "traffic_index": traffic_profile,
                    "weather_condition": weather_profile,
                    "transport_medium": fleet_profile,
                    "target_language": language_profile
                }

                with column_right:
                    st.subheader("🧠 Congnitive Supply-Chain Decision System")
                    st.warning("Passing visual telemetry payload to the LLM core..")

                    #Ship telemetry off to OpenAI's endpoint for analysis
                    with st.spinner("Calculating alternative routing and localized updates.."):
                        executive_decision = orchestrator_unit.generate_routing_strategy(
                            visoin_data=telemetry_stream,
                            operational_context=context_bundle
                        )
                        st.markdown("### **AI Operations Briefing Directives**")
                        st.write(executive_decision)
                        st.success("Operational recovery routine logged successfully.")

    except Exception as initialization_error:
        st.error(f"Critical Runtime System Initialization Halt: {str(initialization_error)}")
else:
    st.warning("🔒 Node Disconnectec: Please input your OpenAI Secret API Key within the security sidebar configuration to instantiate the systems.")
                        


