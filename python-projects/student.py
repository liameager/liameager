class Students:

    def __init__(self, fname, lname, id, energy_level = 10):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level
    
    def __str__(self):
        return f"{self.lname}: {self.id}"
    
    def greeting(self, fname):
        return F"Hello my guy, whats good? My name is {fname}"
    
    def take_exam(self, energy_level):
        energy_level -= 1

    def get_energy_level(self, energy_level):
        return F"Energy level: {energy_level}"