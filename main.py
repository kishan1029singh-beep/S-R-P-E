from pollution_model import calculate_pollution
from solution_engine import suggest_solution
from graph import plot_pollution

def main():
    print("🚦 Smart Road AI Simulation Started")

    traffic_density = 80   # vehicles per minute (example)
    
    pollution = calculate_pollution(traffic_density)
    print(f"Estimated Pollution Level: {pollution}")

    solution = suggest_solution(pollution)
    print(f"AI Suggestion: {solution}")

    plot_pollution(traffic_density, pollution)

if __name__ == "__main__":
    main()
