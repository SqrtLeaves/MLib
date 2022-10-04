class MathNode:
    ID = -1
    Type = ""
    From = ""
    Keyword = []
    Intro = ""
    OtherContents = []

    def print(self):
        print(self.info())

    def info(self):
        return "{}\n{}\n{}\n{}\n{}\n{}".format(self.ID, self.Type, self.From, self.Keyword, self.Intro, self.OtherContents)

