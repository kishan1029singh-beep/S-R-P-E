import matplotlib.pyplot as plt

def plot_pollution(traffic, pollution):
    plt.figure()

    plt.bar(["Traffic Density"], [traffic])
    plt.bar(["Pollution Level"], [pollution])

    plt.title("Smart Road AI Analysis")
    plt.ylabel("Value")

    plt.show()
