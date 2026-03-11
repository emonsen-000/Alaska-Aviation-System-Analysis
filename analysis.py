import pandas as pd 

df_facilities= pd.read_excel("Airport_Data.xlsx", sheet_name=0)
df_runway= pd.read_excel("Airport_Data.xlsx", sheet_name=1)
df_schedules= pd.read_excel("Airport_Data.xlsx", sheet_name=2)
df_remarks= pd.read_excel("Airport_Data.xlsx", sheet_name=3)

### DATA CLEANING & PREPROCESSING

# NaN Values
print("Total null values:\n",df_facilities.isnull().sum())

# Fill NaN Values
df_facilities=df_facilities.fillna("Unknown")

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

### DATA OVERVIEW

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
airports_by_county=airports.groupby("County")["Type"].value_counts().sort_values(ascending=False)
print("\nNumber of Airports by County:\n",airports_by_county.head(10))

# Types of Airport Uses
airports_per_use=airports.groupby("Type")["Use"].value_counts()
print("\nTypes of Airport Uses:\n",airports_per_use)

# Total number of facilites by ownership
total_ownership_types=df_facilities.groupby("Type")["Ownership"].value_counts()
print("\nTotal number of facilites by ownership:\n",total_ownership_types)

# Ownership details
print("\nTop Owners:\n",df_facilities["Ownership"].value_counts())   # Public Owned Facility Are Most 
# Most types of uses
print("\nTop Uses:\n",df_facilities["Use"].value_counts())    # Public Used Facility Are Most

