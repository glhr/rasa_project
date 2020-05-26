import pandas as pd

dfs_pipelines = []
percents = [0,10,30,50,70]
runs = range(1,4)
pipelines = ['custom',
             'mitie',
             'recommended',
             'spacy',
             'supervised']

# generate CSV for intent classification results
for pipeline in pipelines:
        file = '{}_vs_userdata/intent_report.json'.format(
            pipeline
        )
        df = pd.read_json(file)
        df = df.drop(['confused_with', 'support'])
        print(df)
        df_avg = df
        df_avg['pipeline'] = pipeline
        dfs_pipelines.append(df_avg)

dfs_pipelines = pd.concat(dfs_pipelines)
print(dfs_pipelines)
dfs_pipelines.to_csv('intent_results.csv')

dfs_pipelines = []
extractors = {
    'custom': 'DIETClassifier',
    'recommended': 'DIETClassifier',
    'spacy': 'CRFEntityExtractor',
    'supervised': 'CRFEntityExtractor',
    'mitie': 'MitieEntityExtractor'
}

# generate CSV for entity extraction results
for pipeline in pipelines:
    for percent in percents:
        extractor = extractors[pipeline]
        file = '{}_vs_userdata/{}_report.json'.format(
            pipeline,
            extractor
        )
        df = pd.read_json(file)
        df = df.drop(['support'])
        print(df)
        df_avg = df
        df_avg['pipeline'] = pipeline
        df_avg['split'] = percent
        dfs_pipelines.append(df_avg)

dfs_pipelines = pd.concat(dfs_pipelines)
print(dfs_pipelines)
dfs_pipelines.to_csv('entity_results.csv')

total_phrases = 1887
number_of_examples = [total_phrases - total_phrases*i/100 for i in percents]
