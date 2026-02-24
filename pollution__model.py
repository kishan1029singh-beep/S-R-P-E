def
calculate_pollution(traffic_density):
    """
    Simple pollution estimation model
    pollution ∝ traffic density
    """

    base_emission = 0.5
    pollution_index = traffic_density * base_emission

    return pollution_index
