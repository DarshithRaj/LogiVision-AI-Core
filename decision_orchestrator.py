from openai import OpenAI

class LogiDecisionOrchestrator:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Critical System Initialization Failure: OpenAI API Key missing.")
        self.client = OpenAI(api_key=api_key)

    def generate_routing_strategy(self, vision_data: dict, operational_context: dict) -> str:
        prompt = f"""
        You are the Head of Autonomous Fulfillment at an ultra-fast Dark Store facility in India.
        Evaluate this incoming telemetry bundle and generate a real-time recovery plan.
        
        [TENSORFLOW VISION TELEMETRY LOG]
        - Categorized Inventory Class: {vision_data['item_category']}
        - Package Integrity Assessment: {vision_data['structural_audit']}
        - Shelf Life Remaining: {vision_data['expiration_horizon_days']} days
        - Model Confidence Score: {vision_data['inference_confidence']:.4f}
        
        [LOCAL PHYSICAL ENVIRONMENT STATUS]
        - Transit Infrastructure Gridlock: {operational_context['traffic_index']}
        - Local Meteorological Status: {operational_context['weather_condition']}
        - Assigned Delivery Fleet Asset: {operational_context['transport_medium']}
        - Preferred Customer Interface Language: {operational_context['target_language']}
        
        Return a structured executive briefing covering exactly:
        1. CRITICAL INVENTORY DIRECTIVE: Analyze if product quality matches the delivery standard. Issue precise accept, replace, or drop commands based on shelf-life and damage telemetry.
        2. SMART ROUTING ENGINE MAP: Coordinate how the rider should move based on traffic condition, vehicle type, and weather.
        3. TRANSLATED CUSTOMER BROADCAST: Draft a single-sentence dispatch update explicitly written in {operational_context['target_language']}. Keep it highly clear and reassuring.
        
        Do not output generic introductory phrases. Begin writing the solution parameters directly.
        """
        try:
            execution_payload = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a deterministic, senior supply chain automated operational middleware optimizer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2
            )
            return execution_payload.choices[0].message.content
        except Exception as system_fault:
            return f"System Failure Exception at Core: Unable to complete logic step. Trace: {str(system_fault)}"