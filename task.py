import sys

class Footer:

    @classmethod
    def __init__(self, total_pages, current_page, boundaries, around):
        self.total_pages = total_pages
        self.current_page = current_page
        self.boundaries = boundaries
        self.around = around


    @classmethod
    def isValid(self, x):
        if (type(x) == int) and (x >= 0):
            return True
        else:
            return False

    @classmethod
    def calc(self):
        self.endbound = self.total_pages - self.boundaries
        self.lside = self.current_page - self.around
        self.rside = self.current_page + self.around
        return self.endbound, self.lside, self.rside


    @classmethod
    def footerOutput(self):
        strFooter = "1"
        counter = 1
        while (counter < self.total_pages):
            counter = counter + 1
            if (counter > self.rside and counter < self.endbound):
                counter = self.endbound
            elif (counter > self.boundaries and counter < self.lside and counter < self.current_page ):
                counter = self.lside - 1
                strFooter += (' ... ')
            if (self.boundaries < counter and self.endbound >= counter and self.current_page != counter):
                if (self.lside <= counter and self.rside >= counter):
                    strFooter += str(counter) + ('')
                elif (counter == self.endbound or counter == self.boundaries+1):
                    strFooter += (' ... ')
            else:
                strFooter += str(counter) + ('')
        return str(strFooter)