import matplotlib.pyplot as plt
from typing import Sequence, Union

def plot_pollution(traffic: Union[float, Sequence[float]],
                   pollution: Union[float, Sequence[float]],
                   labels: Sequence[str] = None,
                   show: bool = True):
    """
    Plot pollution vs traffic.
    - If traffic and pollution are scalars: plot two bars (Traffic Density, Pollution Level).
    - If lists: plot grouped bars per label (labels required or generated as indices).

    Args:
        traffic: single value or list of values.
        pollution: single value or list of values (same length as traffic when list).
        labels: optional labels for list-mode (e.g., road IDs).
        show: whether to call plt.show() (set False for batch/CI).
    """
    # Detect scalar vs list
    is_scalar = not hasattr(traffic, "__len__") or isinstance(traffic, (str, bytes))
    if is_scalar:
        plt.figure(figsize=(5,4))
        names = ["Traffic Density", "Pollution Level"]
        values = [traffic, pollution]
        bars = plt.bar(names, values, color=["#1f77b4", "#ff7f0e"])
        plt.title("Smart Road AI Analysis")
        plt.ylabel("Value")
        for bar in bars:
            height = bar.get_height()
            plt.annotate(f'{height:.1f}',
                         xy=(bar.get_x() + bar.get_width() / 2, height),
                         xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
    else:
        # list mode
        traffic_vals = list(traffic)
        pollution_vals = list(pollution)
        n = len(traffic_vals)
        if labels is None:
            labels = [str(i) for i in range(1, n+1)]
        x = range(n)
        width = 0.35
        plt.figure(figsize=(max(6, n*1.2), 4))
        plt.bar([xi - width/2 for xi in x], traffic_vals, width, label='Traffic', color="#1f77b4")
        plt.bar([xi + width/2 for xi in x], pollution_vals, width, label='Pollution', color="#ff7f0e")
        plt.xticks(x, labels, rotation=45)
        plt.ylabel("Value")
        plt.title("Traffic vs Estimated Pollution by Road")
        plt.legend()
        # annotate
        for xi, t, p in zip(x, traffic_vals, pollution_vals):
            plt.text(xi - width/2, t + 0.5, f'{t:.0f}', ha='center', va='bottom', fontsize=8)
            plt.text(xi + width/2, p + 0.5, f'{p:.0f}', ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    if show:
        plt.show()
