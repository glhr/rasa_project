import pandas as pd

dfs_pipelines = []
percents = range(0,20,10)
runs = range(1,3)

for pipeline in ['custom', 'pretrained_embeddings_spacy', 'supervised_embeddings']:
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
