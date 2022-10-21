import pickle

with open("log_reg", "rb") as f:    
            model = pickle.load(f)
            return model
