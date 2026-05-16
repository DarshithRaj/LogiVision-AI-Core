from openai import OpenAI

class LogiDecisionOrchestrator:
    def __init__(self, api_key: str):
        """
        Initializes the dynamic generative dispatch center using 
        the unified OpenAI client module.
        """
        if not api_key:
            raise ValueError("Critical system initialization failure: OpenAI Key missing.")
        self.client = OpenAI(api_key=api_key)

    def generate_routing_strategy(self, vision_data: dict, operational_context: dict) -> str:
        """
        Synthesizes hardware vision anomalies and city environmental context 
        to write live dispatch routing metrics and localized consumer warnings.
        """
        prompt_matrix = f"""
        You are an autonomous dark store logistics platform director. An item has been scanned at the packaging terminal.
        
        [SCANNER TELEMETRY DATA]
        - Verified Item: {vision_data.get('item_category')}
        - Package Structural Status: {vision_data.get('structural_audit')}
        - Days Left Until Expiry: {vision_data.get('expiration_horizon_days')} days
        
        [LIVE ENVIRONMENTAL CONDITIONS]
        - Metro Traffic Index: {operational_context.get('traffic_index')}
        - Weather Situation: {operational_context.get('weather_condition')}
        - Assigned Courier Fleet Type: {operational_context.get('transport_medium')}
        - Customer Alert Target Language: {operational_context.get('target_language')}
        
        TASK INSTRUCTIONS:
        1. Write a 'CRITICAL INVENTORY DIRECTIVE'. Decide if the product is safe to fulfill or needs replacement.
        2. Write a 'SMART ROUTING ENGINE MAP'. Give specific routing tips tailored to the fleet type and weather conditions.
        3. Write a 'TRANSLATED CUSTOMER BROADCAST'. Translate a friendly arrival notification into the requested language.
        
        Keep your briefing direct, crisp, professional, and clear. Do not include markdown headers or code block notation wrappers.
        """
        
        try:
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert real-time supply chain operations engine manager."},
                    {"role": "user", "content": prompt_matrix}
                ],
                temperature=0.3
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"System Execution Intercepted: Provide a valid OpenAI API key in the configuration sidebar. Error details: {str(e)}"