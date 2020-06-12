try:
    import pandas as pa
    import numpy as np
    import math
except:
    import pip
    pip.main(['install','pandas'])
    import pandas as pa
    import numpy as np
    pip.main(['install','numpy'])
    import math
    pip.main(['install','math'])


#reading in data frpm xlsx file
NO2_2001 = pa.read_csv('.\NO2 Werte\no2_2001.csv')
Kraftfahrzeugbestand = pa.read_csv('.\Kraftfahrzeugbestand\Kraftfahrzeugbestand.csv')

#functions



