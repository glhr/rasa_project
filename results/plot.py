import pandas as pd

dfs_pipelines = []

for pipeline in ['custom', 'pretrained_embeddings_spacy', 'supervised_embeddings']:
    dfs_runs = []
    for run in range(1,3):
        file = 'run_{}/0%_exclusion/{}_report/intent_report.json'.format(
            run,
            pipeline
        )
        df = pd.read_json(file)
        df = df.drop(['confused_with', 'support'])
        # print(df)
        dfs_runs.append(df)
    df_avg = pd.concat(dfs_runs).groupby(level=0).mean()
    df_avg['pipeline'] = pipeline
    df_avg['split'] = 0

    dfs_pipelines.append(df_avg)

dfs_pipelines = pd.concat(dfs_pipelines)
print(dfs_pipelines)
