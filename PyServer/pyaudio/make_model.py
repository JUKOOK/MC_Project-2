from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(["/Users/BinGyungmin/Desktop/pyserver/pyaudio/Gyungmin_wav/", "/Users/BinGyungmin/Desktop/pyserver/pyaudio/Jukook/", "/Users/BinGyungmin/Desktop/pyserver/pyaudio/HH/","/Users/BinGyungmin/Desktop/pyserver/pyaudio/SH/"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmGyungmin", True)
