#!/usr/bin/env python
# encoding: utf-8
#
# EBAC is a calculator for Estimated Blood Alcohol Content.
#
# It helps you figure out if you're too drunk to drive, and is based on the
# formula given in the paper 'Alcohol use among university students in Sweden
# measured by an electronic screening instrument' by Andersson, WirÃ©hn,
# Olvander, Ekman, and Bendtsen [1].
# 
# Copyright (c) 2014, Brendan Jurd <bj@swords.id.au>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# [1] http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2724514/
"""usage: ebac.py drinks period male mass

    drinks  number of standard drinks (10g ethanol).
    period  period of drinking (hours).
    male    whether the drinker is male (0 or 1).
    mass    drinker's body mass (kg).
"""


FACTOR = 1.2
BLOOD_WATER = 0.806
BODY_WATER = (0.49, 0.58)   # female, male
METABOLISM = (0.017, 0.015) # female, male


def ebac(drinks, period, male, mass):
    """Return the EBAC in grams alcohol per decilitre blood.

    'drinks' is the number of standard drinks consumed, where each standard
    drink contains 10 grams of pure ethanol.
    
    'period' is the drinking period in hours.

    'male' is whether the drinker's sex is male, as a boolean.

    'mass' is the drinker's body mass in kilograms.
    """
    water = BODY_WATER[male]
    meta = METABOLISM[male]
    result = (BLOOD_WATER * drinks * FACTOR) / (water * mass) - (meta * period)
    return max(0, result)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 5:
        print __doc__
        sys.exit(1)
    drinks = float(sys.argv[1])
    period = float(sys.argv[2])
    male = bool(int(sys.argv[3]))
    mass = float(sys.argv[4])
    print ebac(drinks, period, male, mass)
    sys.exit(0)
