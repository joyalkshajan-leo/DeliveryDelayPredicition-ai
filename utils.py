def get_route_suggestion(distance, traffic, weather, priority, vehicle, expected_time, route_name):
    """
    Smart Route Recommendation Logic:
    Integrates 7 data parameters to give industry-level dynamic recommendations.
    """
    vehicle_types = {1: "Bike", 2: "Van", 3: "Heavy Truck"}
    v_type = vehicle_types.get(vehicle, "Vehicle")
    
    # Analyze if expected time is realistic simply based on distance (assuming ~50km/h avg)
    realistic_time = distance / 50.0
    time_warning = ""
    if expected_time > 0 and realistic_time > expected_time + 1:
        time_warning = f" Expected {expected_time}h is tight for {distance}km. "

    if traffic == 3:
        if priority == 3:
            return f"CRITICAL: Heavy traffic on {route_name}. Reroute {v_type} via toll/highway immediately to meet high priority deadline.{time_warning}"
        else:
            return f"Delay expected on {route_name} due to heavy traffic. Delay {v_type} dispatch or reroute.{time_warning}"
    
    if weather == 1:
        if vehicle == 1: # Bike
            return f"{v_type} transit is highly unsafe in bad weather on {route_name}. Consider upgrading to Van/Truck."
        return f"Bad weather conditions on {route_name}. Reduce {v_type} speed and advise customer of minor delays."

    if distance > 500:
        return f"Long-haul route on {route_name}. Ensure {v_type} is optimized for highway driving. Proceed safely.{time_warning}"
        
    return f"Conditions optimal on {route_name}. Proceed with standard {v_type} dispatch."

def get_alert(weather, traffic, priority, delay_prediction):
    """
    Smart Alert System Logic based on prediction, weather, traffic, and priority.
    """
    if delay_prediction == 1:
        if priority == 3:
            return "URGENT ALERT: High priority shipment is predicted to be delayed. Immediate intervention required."
        elif traffic == 3 and weather == 1:
            return "SEVERE DISRUPTION: Both heavy traffic and storms reported. Significant delay."
        elif traffic == 3:
            return "TRAFFIC ALERT: Congestion is restricting flow."
        elif weather == 1:
            return "WEATHER ALERT: Storms are restricting operational speeds."
            
    if delay_prediction == 0 and priority == 3:
        return "PRIORITY TRACK: Shipment is on track to meet priority deadline."

    return "No active warnings. System nominal."
