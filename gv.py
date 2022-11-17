import pandas as pd
import numpy as np
import yaml

stream = open(r'./band.yaml', 'r', encoding='utf-8')
data = yaml.load(stream, Loader=yaml.FullLoader)
out = []
for i in data['phonon']:
    for c, j in enumerate(i['band']):
        v = 100*((j['group_velocity'][0])**2+(j['group_velocity'][1])**2+(j['group_velocity'][2])**2)**0.5
        out.append([i['distance'], j['frequency'], j['group_velocity'][0]*100, j['group_velocity'][1]*100,
                    j['group_velocity'][2]*100, v, c+1])
out.append([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
out_pd = pd.DataFrame(out)
out_pd.columns = ['distance(脜-1)', 'frequency', 'gvx(m/s)', 'gvy(m/s)', 'gvz(m/s)', 'gv(m/s)', 'band']
# The unit of frequency is the same as that set in phonopy

i_ls = []
for item, group in out_pd.groupby('band'):
    i_ls += list(group.index) + [list(out_pd.index)[-1]]
tem = out_pd.loc[i_ls]

tem.to_csv(r'gv.txt', index=False, sep='\t')
