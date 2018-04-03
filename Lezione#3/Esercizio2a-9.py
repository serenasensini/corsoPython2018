#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def meterToInches(meters):
	converted = meters *  39.3701
	return converted
	
def metersToMiles(meters):
	converted = meters *  0.000621371
	return converted
	
print meterToInches(1)
print metersToMiles(1)

print meterToInches(13)
print metersToMiles(17)