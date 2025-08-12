import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_clusters(
    X_2d, cluster_labels, title="Clusters visualized with UMAP", figsize=(10, 7)
):
    """Visualize clusters in 2D space using UMAP coordinates.

    Args:
        X_2d (array-like, shape (n_samples, 2)): 2D coordinates from UMAP dimensionality reduction
        cluster_labels (array-like, shape (n_samples,)): Cluster labels for each data point
        title (str, optional): Title for the plot. Defaults to "Clusters visualized with UMAP".
        figsize (tuple, optional): Figure size (width, height). Defaults to (10, 7).
    """
    plot_df = pd.DataFrame(X_2d, columns=["UMAP1", "UMAP2"])
    plot_df["Cluster"] = cluster_labels

    plt.figure(figsize=figsize)
    sns.scatterplot(
        data=plot_df,
        x="UMAP1",
        y="UMAP2",
        hue="Cluster",
        palette="tab10",
        s=70,
        alpha=0.85,
    )
    plt.title(title, fontsize=14)
    plt.legend(title="Cluster")
    plt.show()
