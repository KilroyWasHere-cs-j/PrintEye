# Handles file reading and writing

configPath = 'config.txt'
logPath = 'Log.txt'
metricPath = 'Metric.txt'


def Update_Log(message):
    file1 = open(logPath, 'r')
    fileContext = file1.read()
    file1.close()
    file2 = open(logPath, 'w')
    file2.write(str(fileContext))
    file2.write("\n")
    file2.write(message)
    file2.close()


def Update_Metrics(metric):
    MFile = open(metricPath, 'r')
    fileContext = MFile.read()
    MFile.close()
    MFile2 = open(metricPath, 'w')
    MFile2.write(str(fileContext))
    MFile2.write("\n")
    MFile2.write(metric)
    MFile2.close()


def Update_Config(update):
    CFile = open(configPath, 'r')
    fileContext = CFile.read()
    CFile.close()
    CFile2 = open(configPath, 'w')
    CFile2.write(fileContext)
    CFile2.write("\n")
    CFile2.write(update)
    CFile.close()


def Open_Metrics():
    MFile = open(metricPath, 'r')
    fileContext = MFile.read()
    MFile.close()
    return fileContext

