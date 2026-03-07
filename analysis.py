import pandas as pd 

df_facilities= pd.read_excel("Airport_Data.xlsx", sheet_name=0)
df_runway= pd.read_excel("Airport_Data.xlsx", sheet_name=1)
df_schedules= pd.read_excel("Airport_Data.xlsx", sheet_name=2)
df_remarks= pd.read_excel("Airport_Data.xlsx", sheet_name=3)


### DATA OVERVIEW & STRUCTURE

# NaN Values
print("Total null values:\n",df_facilities.isnull().sum())
# Fill NaN Values
df_facilities=df_facilities.fillna("Unknown")

# Types of the Aviation Facilities
print("Aviation Facility Types:\n",df_facilities["Type"].unique())
# Most used facility
print("\nMost Used Facility:\n",df_facilities["Type"].value_counts())        # Airports are the most common aviation facility

# Average Elevation 
print("\nAverage Elevation:\n",df_facilities["ARPElevation"].mean())

# Highest Elevation
highest=df_facilities.sort_values(by="ARPElevation",ascending=False)
print("\nTop 10 Highest Elevation Facility:\n",highest[["ARPElevation","FacilityName"]].head(10))
print("\nHighest Elevation Value:\n",highest[["ARPElevation","FacilityName"]].head(1))
print("\nLowest Elevation Value:\n",highest[["ARPElevation","FacilityName"]].tail(1))

# Seaplane bases in Alaska
seaplane_bases=df_facilities[df_facilities["Type"]=="SEAPLANE BASE"]
print("\nTotal Seaplane Bases in Alaska:\n",len(seaplane_bases))