# UCS JSON SCRIPTS

The purpose of these scripts is twofold:

1. take the UCS database and convert it into a JSON 

2. merge the space-track catalog information into that JSON

Why? 

Well for one I prefer JSON to csv formats. 

Moreover, it's useful to have a singular source of data that's pre-merged to use in applications. 

## run

convert UCS to JSON: `python3 convert.py`

merge space-track satcat and UCS: `python3 convertAndMerge.py`

## data sources

[Satellite DataBase](https://www.ucsusa.org/resources/satellite-database)

[Space Track SatCat Query](https://www.space-track.org/basicspacedata/query/class/satcat/orderby/NORAD_CAT_ID%20asc/emptyresult/show)

