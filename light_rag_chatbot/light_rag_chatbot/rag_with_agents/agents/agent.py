# agents/agent.py

from agents.tools import book_inspection, show_pricing, escalate_to_human

class HomeSecureAgent:
    def __init__(self):
        self.required_booking_fields = ["address", "date"]

    def check_relevance(self, query):
        keywords = ["inspection", "property", "home", "visit", "appointment", "book"]
        return any(word in query.lower() for word in keywords)

    def check_booking_info(self, booking_details):
        return all(booking_details.get(field) for field in self.required_booking_fields)

    def analyze_intent(self, query):
        """Simple rule-based intent classifier."""
        query_lower = query.lower()
        if "book" in query_lower or "appointment" in query_lower:
            return "book_inspection"
        elif "price" in query_lower or "cost" in query_lower or "pricing" in query_lower:
            return "show_pricing"
        elif "complaint" in query_lower or "problem" in query_lower:
            return "escalate"
        else:
            return "default"

    def handle_query(self, query, booking_details={}):
        if not self.check_relevance(query):
            return "I'm only able to assist with Home Inspection related queries. Please ask about property inspections."

        action = self.analyze_intent(query)

        if action == "book_inspection":
            if self.check_booking_info(booking_details):
                return book_inspection(booking_details)
            else:
                return "To book an inspection, please provide your address and preferred date."
        
        elif action == "show_pricing":
            return show_pricing()
        
        elif action == "escalate":
            return escalate_to_human()
        
        else:
            return "Let me assist you with any questions you have about home inspections!"
