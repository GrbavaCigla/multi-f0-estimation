Multiple Fundamental Frequency Estimation
-----------------------------------------

Multiple F0 estimation based on Anssi Klapuri's 2006 paper, "Multiple Fundamental Frequency Estimation by Summing Harmonic Amplitudes". Implemented in Python using NumPy.

Fork changes
-------------

I made minimal code changes to make it work on modern python versions.  
What have I done
- Removed Mei, added simple print instead
- Replaced scikits with scipy for reading wav files


Current Status
--------------

I should point out that my implementation never achieved the results stated in Klapuri's paper. I think the issue is with the method of spectral estimation of the found fundamental frequency and its harmonics, which is vaguely described in the paper. I have since moved institutions and no longer have the time to troubleshoot. If anyone else would like to take a crack at it, there is a good code base here to work with.

Authors
-------
Gregory Burlet 2012
