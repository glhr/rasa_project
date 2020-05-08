import pandas as pd

dfs_pipelines = []
percents = range(0,20,10)
runs = range(1,3)
pipelines = ['custom', 'pretrained_embeddings_spacy', 'supervised_embeddings']

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
    'pretrained_embeddings_spacy': 'CRFEntityExtractor',
    'supervised_embeddings': 'CRFEntityExtractor'
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
