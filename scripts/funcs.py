"""Functions file used for analysis of MIRI data.

:History:

Created on Mon May 24 2021

@author: Ioannis Argyriou (KULeuven, Belgium, ioannis.argyriou@kuleuven.be)
"""

# import python modules
import numpy as np

# Definition
#--auxilliary data
def mrs_aux(band):
    allbands = ['1A','1B','1C','2A','2B','2C','3A','3B','3C','4A','4B','4C']
    allchannels = ['1','2','3','4']
    allsubchannels = ['A','B','C']

    # slice IDs on detector
    sliceid1=[111,121,110,120,109,119,108,118,107,117,106,116,105,115,104,114,103,113,102,112,101]
    sliceid2=[201,210,202,211,203,212,204,213,205,214,206,215,207,216,208,217,209]
    sliceid3=[316,308,315,307,314,306,313,305,312,304,311,303,310,302,309,301]
    sliceid4=[412,406,411,405,410,404,409,403,408,402,407,401]

    MRS_bands = {'1A':[4.885,5.751],
        '1B':[5.634,6.632],
        '1C':[6.408,7.524],
        '2A':[7.477,8.765],
        '2B':[8.711,10.228],
        '2C':[10.017,11.753],
        '3A':[11.481,13.441],
        '3B':[13.319,15.592],
        '3C':[15.4,18.072],
        '4A':[17.651,20.938],
        '4B':[20.417,24.22],
        '4C':[23.884,28.329]} # microns

    MRS_R = {'1A':[3320.,3710.],
        '1B':[3190.,3750.],
        '1C':[3100.,3610.],
        '2A':[2990.,3110.],
        '2B':[2750.,3170.],
        '2C':[2860.,3300.],
        '3A':[2530.,2880.],
        '3B':[1790.,2640.],
        '3C':[1980.,2790.],
        '4A':[1460.,1930.],
        '4B':[1680.,1770.],
        '4C':[1630.,1330.]} # R = lambda / delta_lambda

    MRS_lambpix = {'1A':0.0008,
        '1B':0.0009,
        '1C':0.001,
        '2A':0.0014,
        '2B':0.0017,
        '2C':0.0020,
        '3A':0.0023,
        '3B':0.0026,
        '3C':0.0030,
        '4A':0.0036,
        '4B':0.0042,
        '4C':0.0048} # average pixel spectral size

    MRS_nslices = {'1':21,'2':17,'3':16,'4':12} # number of slices

    MRS_alphapix = {'1':0.196,'2':0.196,'3':0.245,'4':0.273} # arcseconds

    MRS_slice = {'1':0.176,'2':0.277,'3':0.387,'4':0.645} # arcseconds

    MRS_FOV = {'1':[3.70,3.70],'2':[4.51,4.71],'3':[6.13,6.19],'4':[7.74,7.74]} # arcseconds along and across slices

    MRS_FWHM = {'1':0.423,'2':0.647,'3':0.99,'4':1.518} # MRS PSF

    return allbands,allchannels,allsubchannels,MRS_bands[band],MRS_R[band],MRS_alphapix[band[0]],MRS_slice[band[0]],MRS_FOV[band[0]],MRS_FWHM[band[0]],MRS_lambpix[band]

def band_to_subband(band):
    if band[1] == 'A':   subband_id = 'SHORT'
    elif band[1] == 'B': subband_id = 'MEDIUM'
    elif band[1] == 'C': subband_id = 'LONG'

    return subband_id

def band_to_det(band):
    if band[0] in ['1','2']:   det_id = 'SHORT'
    elif band[0] in ['3','4']: det_id = 'LONG'
    return det_id

def band_to_channel(band):
    if band[0] in ['1','2']:   channel_id = '12'
    elif band[0] in ['3','4']: channel_id = '34'
    return channel_id
