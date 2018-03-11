## Python Practice 2

### Introduction
	Implement a GPS message (only GPRMC model msg) decoder. Don't use any existed package

### Sample Message
* Message `$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A`
* Where
```
	123519       Fix taken at 12:35:19 UTC
	A            Status A=active or V=Void.
	4807.038,N   Latitude 48 deg 07.038' N
	01131.000,E  Longitude 11 deg 31.000' E
	022.4        Speed over the ground in knots
	084.4        Track angle in degrees True
	230394       Date - 23rd of March 1994
	003.1,W      Magnetic Variation
	*6A          The checksum data, always begins with *
```
### Sample Output

```
	UTC Time:     12:35.19
	Local Time:   (converted time)
	Latitude:     48 deg 07.038' N
	Longitude:    11 deg 31.000' E
	Date:		  3/23/1994


