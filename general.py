class General():
    @staticmethod
    def validateInput(input_message, error_message, val_type, maxlength=0):
        return InputValidator(input_message, error_message, val_type, maxlength).getResult()
    @staticmethod
    def timeToStr(fhours):
        ihours = int(fhours)
        return "%02d:%02d" % (ihours,(fhours-ihours)*60)
    @staticmethod
    def dictToPrintable(dict, formatDecimal=False):
        result = ''
        for key, value in dict.items():
            if formatDecimal == True and type(value) == float:
                value = round(value, 1)
            if key == "Assignment":
                value = str(value)+"%"
            result += (str(key) + ': ').ljust(14) + str(value).rjust(8) + '\n'
        return result

class InputValidator():
    def __init__(self, input_message, error_message, val_type, maxlength=0):
        self.input_message = input_message
        self.error_message = error_message
        self.val_type = val_type
        self.maxlength = maxlength
        self.result = self.ask()
    
    def ask(self):
        _input = input(self.input_message)
        return self.defaultValidation(_input)
    
    def defaultValidation(self, _input):
        if(len(_input) < 1):
            print("Input is empty")
            return self.ask()
        if(self.maxlength != 0 and len(_input) > self.maxlength):
            print("Input is too long")
            return self.ask()
        return self.customValidation(_input)
        
    def customValidation(self, _input):
        if(self.val_type == "alphanumeric" ):
            if(_input.isalnum()):
                return _input
        elif(self.val_type == "alpha"):
            if(_input.isalpha()):
                return _input
        elif(self.val_type == "digit"):
            if(_input.isdigit()):
                return _input
        elif(self.val_type == "numeric"):
            if(_input.isnumeric()):
                return _input
        elif(self.val_type == "alphaspaces"):
            if(_input.replace(" ", "").isalpha()):
                return _input
        else:
            return ''
        
        print(self.error_message)
        return self.ask()

    def getResult(self):
        return self.result
