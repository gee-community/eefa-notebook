import ee 
import geemap

Map = geemap.Map()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Chapter:      F4.3 Clouds and Image Compositing
#  Checkpoint:   F43d
#  Authors:      Txomin Hermosilla, Saverio Francini, Andréa P. Nicolau,
#                Michael A. Wulder, Joanne C. White, Nicholas C. Coops,
#                Gherardo Chirici
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define required parameters.
targetDay = '06-01'
daysRange = 75
cloudsTh = 70
SLCoffPenalty = 0.7
opacityScoreMin = 0.2
opacityScoreMax = 0.3
cloudDistMax = 1500
despikeTh = 0.65
despikeNbands = 3
startYear = 2015
endYear = 2017

# Define study area.
worldCountries = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')
colombia = worldCountries.filter(ee.Filter.eq('country_na',
    'Colombia'))

# Load the bap library.
library = require('users/sfrancini/bap:library')

# Calculate BAP.
BAPCS = library.BAP(None, targetDay, daysRange, cloudsTh,
    SLCoffPenalty, opacityScoreMin, opacityScoreMax, cloudDistMax)

# Despike the collection.
BAPCS = library.despikeCollection(despikeTh, despikeNbands, BAPCS,
    1984, 2021, True)

# Infill datagaps.
BAPCS = library.infill(BAPCS, 1984, 2021, False, True)

# Visualize the image.
Map.centerObject(colombia, 5)
library.ShowCollection(BAPCS, startYear, endYear, colombia, False,
    None)
library.AddSLider(startYear, endYear)

#  -----------------------------------------------------------------------
#  CHECKPOINT
#  -----------------------------------------------------------------------
Map