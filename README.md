# zephyros

zephyros, named after one of the Greek gods of wind,
is a package designed for predicting power output from wind turbines
(or wind farms) using different methods ranging from physical power 
calculations to machine learning.

## Install

Download the source code of the newest release from
[GitHub](https://github.com/kenokrieger/zephyros). Then run
```bash
python3 -m pip install .
``` 
in the  highest directory.

## Usage

### Examples

#### Example 1: Use the physical prediction method

```python
import matplotlib.pyplot as plt

from zephyros.physical_predictor import predict
from zephyros.sample_data import get_sample_data

x = get_sample_data().sort_index()
x = x.iloc[1_000:1_200]
# calculate the expected power output of a wind turbine
# based on wind speed, temperature and power coefficient
x["predicted_power"], x["predicted_power_uncertainty"] = predict(x)

# visualise the results
fig, ax = plt.subplots()
plt.plot(x.index, x["power_measured"], label="measured power")
plt.plot(x.index, x["predicted_power"], label="predicted power")
plt.fill_between(
    x.index, x["predicted_power"] + x["predicted_power_uncertainty"],
             x["predicted_power"] - x["predicted_power_uncertainty"],
    color="orange", alpha=0.3, linewidth=0, label="uncertainty")
plt.legend()
ax.set_title("Power Prediction based on Physical Calculations")
ax.set_xlabel("Time index")
ax.set_ylabel("Power in kW")
plt.show()
```

### Example 2: Use the empirical prediction method

```python
import matplotlib.pyplot as plt

from zephyros.empirical_predictor import learn_and_predict
from zephyros.sample_data import get_sample_data

x = get_sample_data()
nrows = x.shape[0]
# use 99 % of data for "learning"
learn_predict_split = int(0.99 * nrows)
learn_data = x.iloc[:learn_predict_split]
predict_data = x.iloc[learn_predict_split:]
# predict the power output of a wind turbine based on
# historical values of wind speed and temperature
# and the respective resulting power generation of
# the turbine
features = ["wind_speed", "temperature"]
target = "power_measured"
y = learn_and_predict(learn_data, predict_data,
                      features, target, accuracy=12)
print(y.index)
# visualise the results
fig, ax = plt.subplots()
plt.plot(y.index, predict_data["power_measured"], label="expected power")
plt.plot(y.index, y["predicted"], label="predicted power")
plt.fill_between(
    y.index, y["predicted"] + y["uncertainty"],
    y["predicted"] - y["uncertainty"],
    color="orange", alpha=0.3, linewidth=0, label="uncertainty")
plt.legend()
ax.set_title("Power Prediction based on Historically Measured Values")
ax.set_xlabel("Time index")
ax.set_ylabel("Power in kW")
plt.show()
```

## Development

### Tests

**IMPORTANT NOTICE: Test data in the test_data directory is 
licensed under CC BY Attribution 4.0 International license**

Tests can be run by executing 
```bash
python3 -m pytest
```
in the highest
directory.

## License

This project is licensed under GNU GENERAL PUBLIC LICENSE.
For more details see the LICENSE file.

## Acknowledgements

### Sample Turbine Data

Plumley, C. (2022). Kelmarsh wind farm data (0.0.3) [Data set]. Zenodo.
https://doi.org/10.5281/zenodo.5841834
