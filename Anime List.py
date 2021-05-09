#pip install pandas
import pandas as pd
df = pd.read_csv(r'D:\Upal\Python\AnimeList.csv')
df.sort_values(by=['anime_id'], ascending=True)
df['status'].nunique()
df['status number']=df.groupby('status').ngroup()
df
dfFA = df[df['status number']==1]
dfFA
dfFA['type'].nunique()
dfFA
dfFA['type number']=dfFA.groupby('type').ngroup()
dfFATV = dfFA[dfFA['type number']==5]
#dfFATV
# del dfFATV['title_japanese']
# del dfFATV['broadcast']
# del dfFATV['related']
# del dfFATV['image_url']
# del dfFATV['airing']
# del dfFATV['aired']
# del dfFATV['background']
#del dfFATV [dfFATV['background'], ['opening_theme']]
dfFATV = dfFATV.drop(['background', 'opening_theme','title_japanese','broadcast','related','image_url','airing','aired','ending_theme','title_english','title_synonyms' ], axis=1)
dfFATV=dfFATV.drop(['status number','type number'], axis=1)
dfFATV
dfFATV[dfFATV['title'].str.contains('Naruto')] # Search a Specific item in a collumn
dfat=dfFATV.sort_values(by=['score'], ascending=False)
dfat['premiered rank']=dfat['premiered'].str.extract('.*(\d{4})', expand = False) 
dfat.sort_values(by=['rank'], ascending=True)
dfat.sort_values(by=['popularity'], ascending=True)
dfat[dfat['score']>=7]
dfat['source'].nunique()
dfat['premiered rank'].nunique()
dfat.info()
dfat.rename(columns={'premiered rank':'premiered year'}, inplace=True)
dfat.info()
dfat['premiered year'].unique()
dfat[dfat['title'].str.contains('Hunter x Hunter')]
dfat['premiered year'].replace( ' nan', 0000,inplace=True)
dfat['premiered year'].unique()
dfat.sort_values(by=['premiered year'], ascending=False)
#dfat[dfat['premiered year']>=2005]
dfat['genre'].unique()
dfat
dfat.to_csv (r'D:\Upal\Python\My anime list Git\My-anime-list\export_dataframe.csv', index = None, header=True) 



