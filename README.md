EBAC
====

An Estimator of Blood Alcohol Content

https://github.com/direvus/ebac

Background
----------

This repository contains software tools for conveniently estimating blood
alcohol level based on:

  * the drinker's sex,
  * the drinker's body mass,
  * the number of drinks consumed, and
  * the time period of drinking.

It is particularly aimed at making it easier to figure out whether you are too
drunk to drive.

The repository provides two tools:

  * **ebac.py** is a Python module and command-line tool, and
  * **ebac.html** is a standalone HTML/JavaScript webapp.

Installation
------------

To install **ebac.py**, just copy the file into your local Python site-packages
area.  It is known to be compatible with at least Python 2.7, and probably
Python 2.5 also.

To install **ebac.html**, just point your web browser at it.  It has no
external dependencies and will run just fine from anywhere.  I have [an
instance][1] on my personal website.

Formula
-------

The formula for estimating blood alcohol content used in these tools is derived
from the 2009 paper [*Alcohol use among university students in Sweden measured
by an electronic screening instrument*][2]:

  EBAC = (0.806 × D × 1.2) / (BM × W) - (MR × P)
  
where:

  * 0.806 is the constant for body water in blood,
  * 1.2 is a scaling factor defined by the Swedish National Institute of Public Health,
  * D is the number of standard drinks (10 grams ethanol) consumed,
  * BM is the drinker's body mass in kilograms,
  * W is the body water constant (0.49 for women and 0.58 for men),
  * MR is the metabolic rate constant (0.017 for women and 0.015 for men),
  * P is the drinking period in hours.

License
-------

EBAC is released under the "BSD 2-clause license", the full text of which can
be found in the header comments of all source files.

  [1]: http://swords.id.au/ebac
  [2]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2724514/
