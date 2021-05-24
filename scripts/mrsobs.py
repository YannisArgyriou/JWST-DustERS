# -*- coding: utf-8 -*-
"""

File paths to MIRI observations.

:History:

Created on Mon May 24 2021

@author: Ioannis Argyriou (KULeuven, Belgium, ioannis.argyriou@kuleuven.be)
"""
# some trivia
allbands = ['1A','1B','1C','2A','2B','2C','3A','3B','3C','4A','4B','4C']
allchannels = ['1','2','3','4']
allsubchannels = ['A','B','C']

# filepaths
def dusters_miri_observations(lvl2path,band,bb_temp=None,corr1='',output='img',int_ramp=1):
    sci_imgs = {"1A":lvl2path +'FM1T00011282{}/MIRFM1T00011282_1_495_SE_2011-05-31T02h15m32_LVL2.fits'.format(corr1),
                "1B":lvl2path +'FM1T00011283{}/MIRFM1T00011283_1_495_SE_2011-05-31T03h12m30_LVL2.fits'.format(corr1),
                "1C":lvl2path +'FM1T00011284{}/MIRFM1T00011284_1_495_SE_2011-05-31T04h09m25_LVL2.fits'.format(corr1),
                "2A":lvl2path +'FM1T00011282{}/MIRFM1T00011282_1_495_SE_2011-05-31T02h15m32_LVL2.fits'.format(corr1),
                "2B":lvl2path +'FM1T00011283{}/MIRFM1T00011283_1_495_SE_2011-05-31T03h12m30_LVL2.fits'.format(corr1),
                "2C":lvl2path +'FM1T00011284{}/MIRFM1T00011284_1_495_SE_2011-05-31T04h09m25_LVL2.fits'.format(corr1),
                "3A":lvl2path +'FM1T00011282{}/MIRFM1T00011282_1_494_SE_2011-05-31T02h15m02_LVL2.fits'.format(corr1),
                "3B":lvl2path +'FM1T00011283{}/MIRFM1T00011283_1_494_SE_2011-05-31T03h11m59_LVL2.fits'.format(corr1),
                "3C":lvl2path +'FM1T00011284{}/MIRFM1T00011284_1_494_SE_2011-05-31T04h08m55_LVL2.fits'.format(corr1),
                "4A":lvl2path +'FM1T00011282{}/MIRFM1T00011282_1_494_SE_2011-05-31T02h15m02_LVL2.fits'.format(corr1),
                "4B":lvl2path +'FM1T00011283{}/MIRFM1T00011283_1_494_SE_2011-05-31T03h11m59_LVL2.fits'.format(corr1),
                "4C":lvl2path +'FM1T00011284{}/MIRFM1T00011284_1_494_SE_2011-05-31T04h08m55_LVL2.fits'.format(corr1)}

    bkg_imgs = {"1A":lvl2path +'FM1T00011285{}/MIRFM1T00011285_1_495_SE_2011-05-31T05h06m47_LVL2.fits'.format(corr1),
                "1B":lvl2path +'FM1T00011286{}/MIRFM1T00011286_1_495_SE_2011-05-31T06h03m43_LVL2.fits'.format(corr1),
                "1C":lvl2path +'FM1T00011287{}/MIRFM1T00011287_1_495_SE_2011-05-31T07h00m44_LVL2.fits'.format(corr1),
                "2A":lvl2path +'FM1T00011285{}/MIRFM1T00011285_1_495_SE_2011-05-31T05h06m47_LVL2.fits'.format(corr1),
                "2B":lvl2path +'FM1T00011286{}/MIRFM1T00011286_1_495_SE_2011-05-31T06h03m43_LVL2.fits'.format(corr1),
                "2C":lvl2path +'FM1T00011287{}/MIRFM1T00011287_1_495_SE_2011-05-31T07h00m44_LVL2.fits'.format(corr1),
                "3A":lvl2path +'FM1T00011285{}/MIRFM1T00011285_1_494_SE_2011-05-31T05h06m17_LVL2.fits'.format(corr1),
                "3B":lvl2path +'FM1T00011286{}/MIRFM1T00011286_1_494_SE_2011-05-31T06h03m14_LVL2.fits'.format(corr1),
                "3C":lvl2path +'FM1T00011287{}/MIRFM1T00011287_1_494_SE_2011-05-31T07h00m15_LVL2.fits'.format(corr1),
                "4A":lvl2path +'FM1T00011285{}/MIRFM1T00011285_1_494_SE_2011-05-31T05h06m17_LVL2.fits'.format(corr1),
                "4B":lvl2path +'FM1T00011286{}/MIRFM1T00011286_1_494_SE_2011-05-31T06h03m14_LVL2.fits'.format(corr1),
                "4C":lvl2path +'FM1T00011287{}/MIRFM1T00011287_1_494_SE_2011-05-31T07h00m15_LVL2.fits'.format(corr1)}
    if output == 'filename':
        return sci_imgs[band],bkg_imgs[band]
    elif output == 'img':
        from astropy.io import fits
        hdulist_sci,hdulist_bkg = fits.open(sci_imgs[band]), fits.open(bkg_imgs[band])
        sci_data,bkg_data = hdulist_sci[int_ramp].data[0,:,:],hdulist_bkg[int_ramp].data[0,:,:]
        hdulist_sci.close() ; hdulist_bkg.close()
        return sci_data,bkg_data
    elif output == 'img_error':
        from astropy.io import fits
        hdulist_sci,hdulist_bkg = fits.open(sci_imgs[band]), fits.open(bkg_imgs[band])
        sci_data,bkg_data = hdulist_sci[int_ramp].data[1,:,:],hdulist_bkg[int_ramp].data[1,:,:]
        hdulist_sci.close() ; hdulist_bkg.close()
        return sci_data,bkg_data
