import pandas as pd

dfs_pipelines = []
percents = [0,10,30,50,70]
runs = range(1,4)
pipelines = ['custom',
             'mitie',
             'recommended',
             'pretrained_embeddings_spacy',
             'supervised_embeddings']

# generate CSV for intent classification results
for pipeline in pipelines:
    for percent in percents:
        dfs_runs = []
        for run in runs:
            file = 'run_{}/{}%_exclusion/{}_report/intent_report.json'.format(
                run,
                percent,
                pipeline
            )
            df = pd.read_json(file)
            df = df.drop(['confused_with', 'support'])
            df = df.drop(columns='accuracy')
            print(df)
            dfs_runs.append(df)
        df_avg = pd.concat(dfs_runs, keys=runs)
        df_avg['pipeline'] = pipeline
        df_avg['split'] = percent
        dfs_pipelines.append(df_avg)

dfs_pipelines = pd.concat(dfs_pipelines)
print(dfs_pipelines)
dfs_pipelines.to_csv('intent_results.csv')

dfs_pipelines = []
extractors = {
    'custom': 'DIETClassifier',
    'recommended': 'DIETClassifier',
    'pretrained_embeddings_spacy': 'CRFEntityExtractor',
    'supervised_embeddings': 'CRFEntityExtractor',
    'mitie': 'MitieEntityExtractor'
}

# generate CSV for entity extraction results
for pipeline in pipelines:
    for percent in percents:
        dfs_runs = []
        for run in runs:
            extractor = extractors[pipeline]
            file = 'run_{}/{}%_exclusion/{}_report/{}_report.json'.format(
                run,
                percent,
                pipeline,
                extractor
            )
            df = pd.read_json(file)
            df = df.drop(['support'])
            print(df)
            dfs_runs.append(df)
        df_avg = pd.concat(dfs_runs, keys=runs)
        df_avg['pipeline'] = pipeline
        df_avg['split'] = percent
        dfs_pipelines.append(df_avg)

dfs_pipelines = pd.concat(dfs_pipelines)
print(dfs_pipelines)
dfs_pipelines.to_csv('entity_results.csv')

total_phrases = 1887
number_of_examples = [total_phrases - total_phrases*i/100 for i in percents]

def _plot_curve(
    number_of_examples,
    x_label_text,
    y_label_text,
    graph_path,
) -> None:
    """Plot the results from a model comparison.
    Args:
        output: Output directory to save resulting plots to
        number_of_examples: Number of examples per run
        x_label_text: text for the x axis
        y_label_text: text for the y axis
        graph_path: output path of the plot
    """
    output = ""
    import matplotlib.pyplot as plt
    import numpy as np
    import rasa.utils.io
    import os

    ax = plt.gca()

    # load results from file
    data = rasa.utils.io.read_json_file("results.json")
    x = number_of_examples

    # compute mean of all the runs for different configs
    for label in data.keys():
        if len(data[label]) == 0:
            continue
        mean = np.mean(data[label], axis=0)
        std = np.std(data[label], axis=0)
        ax.plot(x, mean, label=label, marker=".")
        ax.fill_between(
            x,
            [m - s for m, s in zip(mean, std)],
            [m + s for m, s in zip(mean, std)],
            color="#6b2def",
            alpha=0.2,
        )
    ax.legend(loc=4)

    ax.set_xlabel(x_label_text)
    ax.set_ylabel(y_label_text)
    plt.tight_layout()

    plt.savefig(graph_path, format="png", dpi=400)

    print(f"Comparison graph saved to '{graph_path}'.")


_plot_curve(
    number_of_examples,
    x_label_text="Number of intent examples present during training",
    y_label_text="Weighted average F1 score on test set",
    graph_path="intents-average-plot.png",
)
