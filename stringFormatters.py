#  Implements a superclass `Formatter` which allow for the creation of easily manageable subclasses with customizable string formatting.
class Formatter:
    __slots__= 'rules'

    DEFAULT_FORMATTER_DICT_OPT:dict={
        'width': int,
        'length': int,
        'padding':str,
        'padding_symbols':str,
        'isValid':bool,
        'addTerminator':bool
        }

    def ___catchFormatterDict(self) -> dict:
        return (len(self.DEFAULT_FORMATTER_DICT_OPT),self.DEFAULT_FORMATTER_DICT_OPT);
    
    def __getFormatterDict(self, param:tuple) -> dict:
        w,l,p,ps,isv,at = param;
        self.rules['width'] = w;
        self.rules['length'] = l;
        self.rules['padding'] = p;
        self.rules['padding_symbol'] = ps;
        self.rules['isValid'] = isv;
        self.rules['addTerminator'] = at;
    
    def __init__(self, rules:tuple) -> None:
        try:
            self.rules = {};
            self.__getFormatterDict(rules);
        except Exception as e:
            print(e)            
            self.rules = self.___catchFormatterDict();

    def apply(self, string:str) -> str or None:
        needsPadding=True;

        if(not(isinstance(string,str))):
            return None;
        else:
            if(len(string) >= int(self.rules["width"])):
                string = string[0:int(self.rules['width'])];
                if(self.rules['addTerminator']):
                    string = string[0:-3] + "...";             
            if(needsPadding):
                padding = (int(self.rules['length']) - len(string))*self.rules['padding'];

                if(self.rules['padding_symbol'] == '<'):
                    string = padding + string;

                elif(self.rules['padding_symbol'] == '>'):
                    string = string + padding;

                elif(self.rules['padding_symbol'] == '^'):
                    padding = ((int(self.rules['length']) - len(string)) // 2)*self.rules['padding']

                    string  = padding + string + padding;
                    t       = 1;
                    while(len(string) > int(self.rules['length'])+1):
                        string  = string[0:-t];
                        t       += 1;
        return string;
