class PupThing():

    def __init__(self):
        #Uncomment this (and comment the other one) to change the dictionary
        #self.pupdict = {"toy":"squeaky","bark":"borf","tail":"unknown"}
        #Whatever goes up here is availbale to the entire class
        self.pupdict = {"toy":"bone","bark":"borf","tail":"unknown"}

    def loop_me(self,somevalue):
        if self.pupdict["toy"] == somevalue:
            #Self refers to any variable, function, object within the same class
            status = True
        else:
            status = False
        #Return lets the function emit something back to the function which called
        #it
        return status

    def run(self):
        if self.loop_me("bone") and self.pupdict["bark"] == "borf":
            #self.loop_me is a function which returns a True|False status based
            #on the logic contained within it. It accepts a parameter, which it
            #sets as teh variable 'somevalue'

            #Test the dictionary, then update it!
            self.pupdict["tail"] = "wag"
        else:
            #Pup wants a bone, not a squeaky
            self.pupdict["tail"] = "nowag"
        #return the updated pupdict to the print function which called it.
        return self.pupdict

if __name__ == "__main__":
    #If the program is being run as itself, do this:
    print PupThing().run()
