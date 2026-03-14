import pandas as pd 

df_fac= pd.read_excel("Airport_Data.xlsx", sheet_name=0)
df_runway= pd.read_excel("Airport_Data.xlsx", sheet_name=1)
df_schedules= pd.read_excel("Airport_Data.xlsx", sheet_name=2)
df_remarks= pd.read_excel("Airport_Data.xlsx", sheet_name=3)

### DATA OVERVIEW

# shape of the dataset
print("Shape of the dataset:\n",df_fac.shape)

# NaN Values
print("Total null values:\n",df_fac.isnull().sum())

# info of the dataset
df_fac.info()

### DATA CLEANING & PREPROCESSING

df_facilities=df_fac[["SiteNumber","Type","County","City","FacilityName","Ownership","Use","ARPLatitude","ARPLongitude","ARPElevation",
                      "MagneticVariation","DistanceFromCBD","DirectionFromCBD","LandAreaCoveredByAirport","AirspaceDetermination",
                      "MilitaryJointUse","LastInspectionDate","OtherServices"]]
print("\nNew Shape:\n",df_facilities.shape)

print("\nNull Values:\n",df_facilities.isnull().sum())

print("\nData types:\n",df_facilities.dtypes)

df_facilities["AirspaceDetermination"]=df_facilities["AirspaceDetermination"].fillna("Unknown")
df_facilities["DistanceFromCBD"]=df_facilities["DistanceFromCBD"].fillna(df_facilities["DistanceFromCBD"].mean())
df_facilities["LandAreaCoveredByAirport"]=df_facilities["LandAreaCoveredByAirport"].fillna(df_facilities["LandAreaCoveredByAirport"].mean())

# Ownership and Use values changed
ownership_map = {
    "PU": "Public Use",
    "PR": "Private Use",
    "MA": "Municipal",
    "CG": "Coast Guard",
    "MR": "Military"
}
df_facilities["Ownership"]=df_facilities["Ownership"].replace(ownership_map)
df_facilities["Use"]=df_facilities["Use"].replace(ownership_map)

### FACILITY DISTRIBUTION EXPLORATION

# Types of the Aviation Facilities
print("\nAviation Facility Types:\n",df_facilities["Type"].unique())

# Seaplane bases in Alaska
seaplane_bases=df_facilities[df_facilities["Type"]=="SEAPLANE BASE"]
print("\nTotal Seaplane Bases in Alaska:\n",len(seaplane_bases))

# Airports in Alaska
airport_bases=df_facilities[df_facilities["Type"]=="AIRPORT"]
print("\nTotal Airports in Alaska:\n",len(airport_bases))

# Heliports in Alaska
heliport_bases=df_facilities[df_facilities["Type"]=="HELIPORT"]
print("\nTotal Heliport Bases in Alaska:\n",len(heliport_bases))

# total locations
print("\nAll locations are:\n",len(df_facilities["City"].unique()))  # this total number contains tiny villages, tribal communities, seasonal airstrips

# Ownership details
print("\nTypes of Ownership:\n",df_facilities["Ownership"].unique())   

print("\nTypes of Airspace Determination:\n",df_facilities["AirspaceDetermination"].unique())

### EXPLORATORY DATA ANALYSIS

# Average Elevation 
print("\nAverage Elevation:\n",df_facilities["ARPElevation"].mean())

# Most used facility
print("\nMost Used Facility:\n",df_facilities["Type"].value_counts())        # Airports are the most common aviation facility

# Highest Elevation
highest=df_facilities.sort_values(by="ARPElevation",ascending=False)
print("\nTop 10 Highest Elevation Facility:\n",highest[["ARPElevation","FacilityName"]].head(10))
print("\nHighest Elevation Value:\n",highest[["ARPElevation","FacilityName"]].head(1))
print("\nLowest Elevation Value:\n",highest[["ARPElevation","FacilityName"]].tail(1))

# Airports by County
airports=df_facilities[df_facilities["Type"]=="AIRPORT"]
print("\nNumber of Airports by County:\n",airports["County"].value_counts())

# Types of Airport Uses
print("\nTypes of Airport Uses:\n",airports["Use"].value_counts())

# Total number of facilites by ownership
total_ownership_types=df_facilities.groupby("Type")["Ownership"].value_counts()
print("\nTotal number of facilites by ownership:\n",total_ownership_types)

# Most Ownerships
print("\nTop Owners:\n",df_facilities["Ownership"].value_counts())   # Public Owned Facility Are Most 
# Most types of uses
print("\nTop Uses:\n",df_facilities["Use"].value_counts())    # Public Used Facility Are Most

# number of airspace determination
print("\nAirspace Dtermination:\n",df_facilities["AirspaceDetermination"].value_counts())

# objectional and unknown airspaces
airspace=df_facilities[(df_facilities["AirspaceDetermination"]=="OBJECTIONABLE") | (df_facilities["AirspaceDetermination"]=="Unknown")]
print("\nObjectional and Unknown airspaces\n",airspace) 

# average distance from CBD
print("\nAverage distance from CBD:\n",df_facilities["DistanceFromCBD"].mean())

#total land area covered 
print("\nTotal Land Area Covered:\n",df_facilities["LandAreaCoveredByAirport"].sum())

# land area covered per facility type
total_land_per_type=df_facilities.groupby("Type")["LandAreaCoveredByAirport"].sum()
print("\nTotal land covered per type:\n",total_land_per_type)

# average land area per facility type
avg_land_per_type=df_facilities.groupby("Type")["LandAreaCoveredByAirport"].mean()
print("\nAverage land per type:\n",avg_land_per_type)
