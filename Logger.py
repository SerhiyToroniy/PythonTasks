class Logger:
    _file_name = "logs.txt"

    def printToFile(self, state = "", pos = None, newList = None, resultList = None):
        File = open(self._file_name, "a")
        line = [str(state),str(pos),str(newList),str(resultList)]
        File.writelines(str(line)+"\n")
        File.close()
