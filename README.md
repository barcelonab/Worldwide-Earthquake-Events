**This is a personal project. Since earthquakes frequently occur here in the USA, especially in California, I created this report to show the total number of earthquakes worldwide and their impact.**

**Visualized on the Dashboard are**

- Over an 8-day period, there are 1,552 earthquake events Worldwide.
- Out of those events, 7 are of High significance including 5 from Russia with Max Magnitude of 7.8, 1 from Indonesia - Magnitude 6.10 and 1 from Papua New Guinea - Magnitude 6.00.
- Over this period, the USA recorded the highest number of earthquake events.
- Most events from USA are of low significance. With a maximum recorded magnitude of 5.20, no high-significance events were observed, as these are defined as magnitude 6.0 or greater.

**Here are the steps taken to complete the analysis**

- Used Microsoft Fabric to Prepare the Data
- Ingested the Data using Notebook RestAPI-https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date}&endtime={end_date}
- Transformed and cleaned the data by removing columns and rows that are not needed using PySpark.
- Added Environment using the reverse_geocoder package to determine the country by using Latitude and Longitude using PySpark.
- Saved the data frame created in PySpark as Table in Lakehouse.
- Created a new Semantic Model from Lakehouse.
- Opened new Power BI desktop and used the Semantic Model created.
- Created several DAX measures for the desired metrics.
- Published, Administered and created an App in Power BI Service.