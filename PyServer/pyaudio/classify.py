from pyAudioAnalysis import audioTrainTest as aT
[Result, P, classNames] = aT.fileClassification("Hello.wav", "svmGyungmin","svm")
print(Result)
print(P)
print(classNames)
