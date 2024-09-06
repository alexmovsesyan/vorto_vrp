# Vorto Vehicle Routing Problem

## Description

This repo contains my submission to the Vorto Algorithmic Challenge. The Vehicle Routing Problem (VRP) is solved in the main python script `vehicle_router.py`. Additionally, a couple supplemental classes are included in the files `data_loader.py` and `load.py`.

## Running The Code

to invoke the vehicle router scrip, run the following command:

```python3 vehicle_router.py {path_to_load_data.txt}```

The script takes in a single argument pointing to the path of the sample load data. The load data should be a text file with the following format:

```
loadNumber pickup dropoff
1 (-50.1,80.0) (90.1,12.2)
2 (-24.5,-19.2) (98.5,1.8)
3 (0.3,8.9) (40.9,55.0)
4 (5.3,-61.1) (77.8,-5.4)

```