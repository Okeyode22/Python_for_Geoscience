from readdata import read_data

# Column names and column indices
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7, 'windchill': 12}

# Data types for each column (if non-string)
types = {'tempout': float, 'windspeed': float, 'windchill': float}

# Initialize data variable
data = {}
for column in columns:
    data[column] = []

# Read the data file
data = read_data(columns, types=types)

def estimate_windchill(t, v):
    wci = t - 0.7 * v
    return wci
# Initialize windchill
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(estimate_windchill(temp, windspeed))


# Output comparison of data
print('                     ORIGINAL     ESTIMATED')
print(' DATE       TIME     WINDCHILL    WINDCHILL    DIFFERENCE')
print('-------    ------    ---------    ---------    ----------')

zip_data = zip(data['date'], data['time'], data['windchill'], windchill)


for date, time, wc_data, wc_est in zip_data:
    wc_diff = wc_data - wc_est
    print(f'{date}   {time:>6}    {wc_data:9.6f}    {wc_est:9.6f}    {wc_diff:10.6f}')
    
