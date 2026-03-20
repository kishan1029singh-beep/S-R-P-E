def calculate_pollution(traffic_density: float) -> float:
    """
    Simple pollution estimation model
    pollution ∝ traffic density

    Args:
        traffic_density: vehicles (or vehicles per minute) used as proxy.

    Returns:
        pollution index (arbitrary units)
    """
    base_emission = 0.5
    pollution_index = traffic_density * base_emission
    return pollution_index
