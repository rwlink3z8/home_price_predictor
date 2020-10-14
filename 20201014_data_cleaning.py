# data cleaning for the real estate listings

# to clean lot size and have it only in acres

data = (df['Lot Size'].str.replace(',','')
            .str.extract('([\.\d]+)\s?(ac|X)?([\.\d,]+)?')
       )

data[[0,2]] = data[[0,2]].astype(float)

df['lot_size'] = np.select((data[1].eq('X'), data[1].eq('ac')),
                          (data[0]* data[2]/43560,data[0]), 
                          data[0]/43560 )
# drop outliers

df = df[df['lot_size']<10.5]
df = df[df['Sqft Main']<6000]
df = df[df['Sqft Main']>500]

# in case we want to model lot size in square feet

df['lot_size2'] = df['lot_size']*43560

df = df.dropna(subset=['Sqft Main'])

# small subset that are not single family homes, just drop them
df = df[df['Type']=="Single Family"]

# start looking at groupby's to see any trends with sale price
df.groupby('Floor Plan Description', as_index=False)['sale_price'].mean()
# pictures are easier to look at than numbers
df.groupby('Floor Plan Description')['sale_price'].mean().plot.bar(figsize=(12,12))

# currently 54 floor plans - whittle down to 10
# put all the bungalows together
df['Floor Plan Description'] = df['Floor Plan Description'].replace({'Bungalow, Ranch': 'Bungalow', '1.5 Stories, Bungalow':'Bungalow'})

split_entry = {'Side/Side Split': 'Split Entry', 'Front/Back Split':'Split Entry','Atrium Split':'Split Entry',
       'California Split':'Split Entry', 'Side/Side Split':'Split Entry', 'Front/Back Split, Split Entry':'Split Entry',
        'Front/Back Split':'Split Entry','California Split, Front/Back Split':'Split Entry',
       'Atrium Split, California Split':'Split Entry', 'Atrium Split, Raised Ranch':'Split Entry','Atrium Split, Side/Side Split':'Split Entry', 'Side/Side Split, Split Entry':'Split Entry',
       '2 Stories, Split Entry' 'Atrium Split, Other':'Split Entry', '1.5 Stories, Split Entry':'Split Entry',
       '1.5 Stories, Side/Side Split':'Split Entry', '2 Stories, Atrium Split':'Split Entry',
       'Atrium Split, Tri Level':'Split Entry',
       'Front/Back Split, Tri Level':'Split Entry',  'Atrium Split, Front/Back Split':'Split Entry', 'California Split, Split Entry':'Split Entry',
       'Front/Back Split, Raised Ranch':'Split Entry', '2 Stories, California Split':'Split Entry'}

# put all the split entry's together
df['Floor Plan Description'] = df['Floor Plan Description'].replace(to_replace=split_entry.keys(), value=split_entry.values())

df['Floor Plan Description'] = df['Floor Plan Description'].replace({'Ranch, Raised Ranch': 'Raised Ranch', 'Raised Ranch, Split Entry':'Raised Ranch', 'Raised Ranch, Other':'Raised Ranch',
'Raised Ranch, Side/Side Split':'Raised Ranch', 'Raised 1.5 Story, Ranch':'Raised Ranch', 'Ranch, Other':'Ranch', 'Other':'Bungalow', 'Loft, Ranch':'Bungalow', '1.5 Stories, Front/Back Split':'Split Entry', '2 Stories, Split Entry':'Split Entry',  '2 Stories, Side/Side Split':'Split Entry',
'1.5 Stories, Earth Contact':'Earth Contact', 'Earth Contact, Ranch':'Earth Contact', 'Side/Side Split, Tri Level':'Split Entry', 'Atrium Split, Other':'Split Entry', 'Tri Level':'Split Entry',
'2 Stories, Other': '2 Stories', '1.5 Stories, 2 Stories':'1.5 Stories', 'Reverse 1.5 Story, Raised Ranch':'Reverse 1.5 Story', 'Raised 1.5 Story, Reverse 1.5 Story':'Reverse 1.5 Story',
'1.5 Stories, Raised 1.5 Story':'1.5 Stories', '1.5 Stories, 2 Stories':'1.5 Stories', '1.5 Stories, Ranch':'1.5 Stories''Reverse 1.5 Story, Other':'Reverse 1.5 Story'})

# clean up school district
df['School District'] = df['School District'].replace(to_replace=["Lee's Summit", "Other"], value=['Lees Summit', 'Pleasant Hill'])

df['City'] = df['City'].replace(to_replace=["Lee's Summit", "Other"], value=['Lees Summit', 'Raymore'])

df['Fireplace?'] = df['Fireplace?'].replace({'N':0,'Y':1})

df['Basement'] = df['Basement'].fillna(value=0)

df['Basement'] = df['Basement'].replace({'N':0,'Y':1})
df['Garage/Parking?'] = df['Garage/Parking?'].replace({'N':0,'Y':1})
df['In Floodplain'] = df['In Floodplain'].replace({'No':0,'Yes':1, 'Unknown':0})

df['Inside City Limits'].fillna(value=0, inplace=True)
df['Inside City Limits'] = df['Inside City Limits'].replace({'No':-1,'Yes':1, 'Unknown':0})
df['Central Air'] = df['Central Air'].replace({'N':0,'Y':1})

# clean up year built
df['Year Built'] = df['Year Built'].replace({0:2006})
df['Year Built'] = df['Year Built'].replace({196:1968})
df['Year Built'] = df['Year Built'].replace({1194:1994})

df = df.rename(columns={'School District':'school_district'})

# use only the school districts that have a significant market share, we are less interested in the southern portion of the county

df1 = df.loc[df['school_district'].apply(lambda x: x in ['Raymore-Peculiar','Belton','Pleasant Hill',
                                          'Harrisonville','Sherwood','Lees Summit','Cass-Midway'])]
                                          
df1 = df1.rename(columns={'Floor Plan Description':'fp', 'school_district':'school', 'Street Maintenance':'street'})                                        

# dummize the categorical variables we are interested in in a new dataframe
df2 = pd.get_dummies(data=df1, columns=['Floor Plan Description', 'City', 'school_district', 'Street Maintenance', ], dtype='int64')
