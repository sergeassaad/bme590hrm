![alt text](https://travis-ci.org/sergeassaad/bme590hrm.svg?branch=master)

CloudECG
========

Web server implementation using Flask. Uses the HRM class for calculations.

URL: http://vcm-1834.vm.duke.edu:5000

Routes:
=======

- /heart_rate/summary:
    - input: time array, voltage array
    - output: time array, instantaneous HR array, tachy- and bradycardia annotations

- /heart_rate/average:
    - input: time array, voltage array, averaging period
    - output: averaging period, time array, average HR array, tachy- and bradycardia annotations

- /api/requests:
    - output: number of requests to server since last reboot


Heart Rate Monitor (HRM) Class
==================

Heart Rate Monitor which takes in time and voltage data and outputs instantaneous HR, average HR, and diagnoses bradycardia and tachycardia.



Subfunctions
============
readcsv function:

- Input: csv file
- Output: time vector, voltages vector

avghr function:

-	Input: Lists of times, list of voltages, lower time bound, upper time bound
-	Output: 1 value for average heart rate for the specified time range

ihr function:

-	Located in InstHR.py
-	Input: List of times and corresponding list of voltages
-	Output: List of tuples with the start-end time of each heartbeat, and a list of corresponding heartrate calculations for each heartbeat

detect_cardia function:

-	User inputs: bradycardia and tachycardia thresholds
-   Other inputs: list of instantaneous heart rates and list of average heart rates
-   Outputs: bradycardia and tachycardia annotations of average and instantaneous heart rates

License
=======

MIT License

Copyright (c) [2017] [Serge Assaad, Joseph Cobb, Hala El-Nahal]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contributors
============
- Serge Assaad (serge.assaad@duke.edu)
- Joseph Cobb (joseph.cobb@duke.edu)
- Hala El-Nahal (hala.el.nahal@duke.edu)
