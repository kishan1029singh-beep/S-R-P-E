import os
import csv

from pollution_model import calculate_pollution
from solution_engine import suggest_solution
from graph import plot_pollution

def main():
    print("🚦 Smart Road AI Simulation Started")

    csv_path = "data.csv"
    if os.path.exists(csv_path):
        rows = []
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                # basic parsing; adjust if CSV schema changes
                try:
                    r['vehicle_count'] = int(r.get('vehicle_count', 0))
                except ValueError:
                    r['vehicle_count'] = 0
                rows.append(r)

        if not rows:
            print("data.csv present but empty. Falling back to example run.")
        else:
            labels = []
            traffic_vals = []
            pollution_vals = []
            for r in rows:
                road = r.get('road_id', 'unknown')
                traffic = r['vehicle_count']
                pollution = calculate_pollution(traffic)
                suggestion = suggest_solution(pollution)
                print(f"Road {road}: traffic={traffic}, est_pollution={pollution:.1f}, suggestion={suggestion}")
                labels.append(road)
                traffic_vals.append(traffic)
                pollution_vals.append(pollution)

            # Plot aggregated view
            plot_pollution(traffic_vals, pollution_vals, labels=labels)
            return

    # Fallback: single example run (same as previous)
    traffic_density = 80   # vehicles per minute (example)
    pollution = calculate_pollution(traffic_density)
    print(f"Estimated Pollution Level: {pollution}")
    solution = suggest_solution(pollution)
    print(f"AI Suggestion: {solution}")
    plot_pollution(traffic_density, pollution)

if __name__ == "__main__":
    main()
