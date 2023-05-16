class Model:
    def __init__(self, name):
        self.name = name
    
    def fit(self, positive_class):
        print("Training model...")
        print("Model: {}".format(self.name))
        attr_len = positive_class.shape[1] - 1
        h0 = ["0"] * attr_len
        for i in range(positive_class.shape[0]):
            currRow = positive_class.values.tolist()[i]
            for j in range(attr_len):
                if h0[j] == currRow[j]:
                    continue
                else:
                    if i == 0:
                        h0[j] = currRow[j]
                    else:
                        h0[j] = "?"

        return h0
    
    def fit(self,concepts,target):
        specific_h = concepts[0].copy()
        print("\nInitialization of specific_h and genearal_h")
        print("\nSpecific Boundary: ", specific_h)
        general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
        print("\nGeneric Boundary: ",general_h)  

        for i, h in enumerate(concepts):
            print("\nInstance", i+1 , "is ", h)
            if target[i] == "yes":
                print("Instance is Positive ")
                for x in range(len(specific_h)): 
                    if h[x]!= specific_h[x]:                    
                        specific_h[x] ='?'                     
                        general_h[x][x] ='?'
                    
            if target[i] == "no":            
                print("Instance is Negative ")
                for x in range(len(specific_h)): 
                    if h[x]!= specific_h[x]:                    
                        general_h[x][x] = specific_h[x]                
                    else:                    
                        general_h[x][x] = '?'        
            
            print("Specific Bundary after ", i+1, "Instance is ", specific_h)         
            print("Generic Boundary after ", i+1, "Instance is ", general_h)
            print("\n")

        indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]    
        for i in indices:   
            general_h.remove(['?', '?', '?', '?', '?', '?']) 
        return specific_h, general_h 