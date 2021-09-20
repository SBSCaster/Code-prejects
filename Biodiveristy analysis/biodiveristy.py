from matplotlib import pyplot as plt
import pandas as pd
from scipy.stats import chi2_contingency

species = pd.read_csv('species_info.csv')
#print(species.head())

num_species = species.scientific_name.count()
#print(num_species)

categories = species.category.nunique()
#print(categories)

con_status = species.conservation_status.unique()
#print(con_status)


num_null = species.conservation_status.isnull().sum()
#print(num_each_status)
#print(num_null)

species.fillna('No Intervention', inplace = True)


num_each_status = species.groupby('conservation_status').scientific_name.count().reset_index()
#print(num_each_status)


protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')



plt.figure(figsize=(10, 4))
ax = plt.subplot()
plt.bar(range(len(protection_counts['scientific_name'])), protection_counts['scientific_name'].values)
ax.set_xticks(range(5))
ax.set_xticklabels(protection_counts.conservation_status)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
plt.show()


species['is_protected'] = species.conservation_status.apply(lambda x: False if x == 'No Intervention' else True)


category_counts = species.groupby(['category', 'is_protected']).scientific_name.count().reset_index()
#print(category_counts)

category_pivot = category_counts.pivot(
    columns = 'is_protected',
    index = 'category',
    values = 'scientific_name'

).reset_index()

print(category_pivot)


cat = category_pivot.rename(columns = {False: 'not_protected',
                                 True: 'protected'}).reset_index()


print(cat)

cat['percent_protected'] = cat['index'].apply(lambda x: cat['protected'][x]/(cat['protected'][x] + cat['not_protected'][x]) * 100)
#print(cat)

contingency = [38, 176, 79, 442]
contingency2 = [ 5, 74, 38, 176]

_, pval, _, _ = chi2_contingency(contingency2)




observations = pd.read_csv('observations.csv')

species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
species.head()

#species[species.is_sheep]

sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]
#print(sheep_species)

sheep_observations = observations.merge(sheep_species)
#print(sheep_observations)

obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
obs_by_park


plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park)),
        obs_by_park.observations.values)
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name.values)
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
plt.show()