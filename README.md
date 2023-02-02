# DT-CARGO dataset

Dataset of Trucks' Anonymized Recorded Driving and Operation

### Getting started

A working installation of conda package manager is required.

First, install the provided environment. 
 
`conda env create -f environment.yml`

Activate the environment

`conda activate dt_cargo`

Add the environment as a jupyter kernel.

`python -m ipykernel install --user --name=dt_cargo`

### fleet.csv
The overview of the analyzed fleets.

Column | Data Type | Unit | Description
---|---|---|---
vehicle_id | int | - | Unique serial id of each vehicle
fleet_test_id | int | - | Unique serial id of the fleet the vehicle belongs to
gross_vehicle_weight | int | - | Gross Vehicle Weight Rating (without trailer)
total_mass_with_trailer | int | kg | Gross Combination Weight Rating <br />(with trailer,equals gross_vehicle_weight <br />if no trailer can be attached)
axle_class | int | - | Vehicle class according to [3]

### tracks.csv
The overview of track-wise measured and computed data.

Column | Data Type | Unit | Description
---|---|---|---
track_id | int | - |  Unique serial id of each recorded track <br />(ordered by vehicle_id and start_time)
vehicle_id | int | - |  Unique serial id of each vehicle
tour_id | int | - |  Serial id of each tour, assigned to 1..N tracks
start_time | timestamptz | - |  Start time of the recording with time zone at time of recording
stop_time | timestamptz | - |  Stop time of the recording with time zone at time of recording
distance | int |  m | Dis tance driven during track
track_gap | float |  m | Dis tance gap to following track
avg_speed | float | m/s | Average speed
max_speed | int | m/s | Maximum speed within track
n_signal_loss | int | - |  Number of signal loss events during recording
d_signal_loss | float |  m | Dis tance covered during signal losses
r_signal_loss | float | - |  Ratio of signal loss distance to recorded distance
avg_hdop | float | m | Average horizontal degree of precision during recording
home_base | bool | - | End of recording is at home base of fleet operator
long_haul | bool | - | End of recording is more than 150 km away from home bases
rest_area | bool | - |  End of recording is at an unserviced rest area
service_area_fuel | bool | - |  End of recording is at a service area
industrial_area | bool | - |  End of recording is in an industrial area
cid | int | - |  Cluster id of last location in recording.

### speed.csv
Speed and precision data of each individual track with 10Hz sampling.
Speed data are stored in speed.zip in the folder speed/{vehicle_id}/{track_id}.csv
In this repository only the Example track is provided, please refer to [1] for the full dataset.

Column | Data Type | Unit | Description
---|---|---|---
epoch | int | s | Unix timestamp of measurement<br /> in time zone “Europe/Berlin”
speed | int | m/s | Speed at measurement in m/s
hdop| int | m | Horizontal degree of precision during recording [2]

[1] Zenodo Dataset TODO

[2] u-blox, “MAX-M8 series u-blox M8 concurrent GNSS modules Data Sheet”, UBX-15031506-R05 [Revised May 2019]

[3] Bundesanstalt für Straßenwesen, „Datensatzformat der Achslast-
Jahresauswertungen (ALJA)“, 2018. Accessed: 22 nd Jan 2023 [Online]. Available:
https://www.bast.de/DE/Statistik/Achslast/Daten/Daten-Beschreibung.pdf

### Contributing and Support

For contributing to the code please contact:  

Georg Balke 
Institute of Automotive Technology  
Technical University of Munich  
  
mail: georg.balke@tum.de

### Versioning

V1.0 

### Authors

Georg Balke, Lennart Adenaw

### License

DT-CARGO is made available under the Open Database License: http://opendatacommons.org/licenses/odbl/1.0/. Any rights in individual contents of the database are licensed under the Database Contents License: http://opendatacommons.org/licenses/dbcl/1.0/

A human-readable summary can be found under https://opendatacommons.org/licenses/odbl/summary/. Disclaimer: This is not a license. It is simply a handy reference for understanding the ODbL 1.0 — it is a human-readable expression of some of its key terms. This document has no legal value, and its contents do not appear in the actual license. Read the full ODbL 1.0 license text for the exact terms that apply.

### Associated Article

Will be added after publication.