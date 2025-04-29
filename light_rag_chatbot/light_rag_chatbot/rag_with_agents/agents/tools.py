# agents/tools.py

def book_inspection(booking_details):
    # Dummy booking logic
    return f"Booking confirmed for address: {booking_details.get('address')}, date: {booking_details.get('date')}."

def show_pricing():
    return "Our standard home inspection costs $199."

def escalate_to_human():
    return "Your query has been escalated to a human agent. Someone will contact you shortly."
