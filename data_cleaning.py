import numpy as np 
import pandas as pd 
#after running the webscraper, dumped everything in a txt file

df = pd.read_csv('mls.txt', sep='delimiter', header=None)

# dataframe had 1 column and 9259 rows for roughly 1700 houses sold
# give column a name to work with
df.columns = ['a']

#cleaning to remove listing numbers
df = df[~df['a'].str.contains('/')]

# get all the sale prices
df_sold = df[df['a'].str.contains('$')]
df_sold['_id'] = range(0,1726)
df_sold.columns = ['sale_price', '_id']
#house description
df_description = df[df['a'].str.contains('Bedrms')]
df_description['_id'] = range(0,1726)
df_description.columns = ['description', '_id']
# city 
df_add = df[df['a'].str.contains(', MO')]
df_add['_id'] = range(0,1726)
df_add.columns = ['address', '_id']

int1 = df_sold.merge(df_description, on=['_id'], how=left)
df1 = int1.merge(df_add, on=['_id'], how=left)

# clean up sale price to remove the word sold and convert it to an integer

df1['sale_price'] = df1['sale_price'].apply(lambda x: x[1:-4])
df1['sale_price'] = df1['sale_price'].apply(lambda x: int(x))

# extract town from addresses 
df1['town'] = df1['address'].apply(lambda x:x.split(',')[0].split(' ')[-1])

# extract number of bedrooms, bathroms, sq ft, lot size, year built
df1['bedrooms'] = df1['description'].apply(lambda x: x.split('Bedrms')[0])
df1['bathrooms'] = df1['description'].apply(lambda x: x.split('Bathrms')[0])
df1['lot_size'] = df1['description'].apply(lambda x: x.split('Acres')[0])
df1['yr_built'] = df1['description'].apply(lambda x: x.split('Builtin')[0])


# clean up how town was split up

town_dict = {'Hill': 'Pleasant Hill','Strasburg':'Strasburg','Archie':'Archie',
 'City': 'Garden City','StreetBelton': 'Belton','DriveBelton': 'Belton',
 'AvenueHarrisonville':'Harrisonville','StreetHarrisonville':'Harrisonville',
 'TerraceBelton': 'Belton','RoadHarrisonville': 'Harrisonville','StreetRaymore': 'Raymore',
 'AvenueBelton': 'Belton','HighwayHarrisonville': 'Harrisonville',
 'Lynne':'East Lynne','RoadPeculiar':'Peculiar','StreetPeculiar':'Peculiar',
 'DriveHarrisonville': 'Harrisonville','StreetCreighton':'Creighton',
 'CourtPeculiar':'Peculiar','StreetDrexel':'Drexel','DriveFreeman':'Freeman',
 'StreetArchie':'Archie','TrailBelton': 'Belton','TerraceHarrisonville': 'Harrisonville',
 'LaneBelton': 'Belton','#167Peculiar':'Peculiar','AvenueRaymore': 'Raymore',
 'CircleHarrisonville': 'Harrisonville','StreetFreeman':'Freeman','RoadArchie':'Archie',
 'LaneRaymore': 'Raymore','RoadDrexel':'Drexel','PlaceBelton': 'Belton',
 'BaldwinBelton': 'Belton','LaneHarrisonville':'Harrisonville','DriveRaymore': 'Raymore',
 'BrandonHarrisonville': 'Harrisonville','StreetCleveland':'Cleveland','RoadBelton': 'Belton',
 'ParkwayBelton': 'Belton','TrailRaymore': 'Raymore','PlaceRaymore': 'Raymore',
 'DrivePeculiar':'Peculiar','Summit':'Lees Summit','LanePeculiar':'Peculiar',
 'CourtRaymore': 'Raymore','BoulevardRaymore': 'Raymore','TerraceRaymore': 'Raymore',
 'AvenuePeculiar':'Peculiar','DriveCleveland':'Cleveland','CirclePeculiar':'Peculiar',
 'TerracePeculiar':'Peculiar','RoadRaymore': 'Raymore','DriveGreenwood':'Greenwood',
 'RoadCleveland':'Cleveland','CourtBelton': 'Belton','LaneGreenwood':'Greenwood',
 'WayRaymore': 'Raymore','CircleBelton': 'Belton','ParkwayRaymore': 'Raymore',
 'CircleRaymore': 'Raymore','RoadFreeman':'Freeman','CircleGreenwood':'Greenwood',
 'RoadKingsville':'Kingsville','Winnebago':'Lake Winnebago','WayHarrisonville': 'Harrisonville',
 'HighwayArchie':'Archie','PassCleveland':'Cleveland','HighwayCleveland':'Cleveland',
 'AvenueGreenwood':'Greenwood','HighwayBelton': 'Belton','DriveDrexel':'Drexel',
 'LaneCleveland':'Cleveland','PlaceHarrisonville': 'Harrisonville','HighwayFreeman':'Freeman',
 'CoveRaymore': 'Raymore','Lloyd':'Loch Lloyd','HighwayDrexel':'Drexel',
 'AvenueCleveland':'Cleveland','ViewRaymore': 'Raymore','2Cleveland':'Cleveland',
 'CircleArchie':'Archie','PathRaymore': 'Raymore','KHarrisonville':'Harrisonville',
 'OakwoodHarrisonville': 'Harrisonville','2Harrisonville':'Harrisonville','RoadOther': 'Raymore',
 'FranklinRaymore': 'Raymore','EastwoodHarrisonville': 'Harrisonville'}

 df1['town'] = df1['town'].replace(to_replace=town_dict.keys(), value=town_dict.values())

 