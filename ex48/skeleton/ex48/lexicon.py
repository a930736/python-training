class lexicon(object):
    def convert_number(s):
        try:
            return int(s)
        except ValueError:
            return None

    def scan(s):
        directions = ["north", "south", "west", "east","up","left","right","down"]
        verb = ["go", "kill", "eat"]
        stop = ["the", "in", "of","from","at", "it"]
        noun = ["bear", "princess","door"]


        result = []
        words = s.lower().split()

        for word in words:
            if word in directions:
                result.append(("direction",word))
            elif word in verb:
                result.append(("verb",word))
            elif word in stop:
                result.append(("stop",word))
            elif word in noun:
                result.append(("noun",word))
            elif lexicon.convert_number(word):
                result.append(("number",int(word)))
            else:
                result.append(("error",word))
        return result

