
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(name):

            from emojis import emojis
            # :tiger:
            emojized = emojis.encode(greet + " :" + sep + ": " + name)
            print(emojized)

        return innerMostFun

    return innerFun

engGrt = outerFun("Welcome")

tgrenGrt = engGrt("tiger")
linenGrt = engGrt("lion")

linenGrt("Micheal")
tgrenGrt("Sheroff")







"""
engGrt = outerFun("Welcome")


engSngArw = engGrt("---->")
engDblArw = engGrt("=====>")

engSngArw("Henry")
engDblArw("Jack")
"""