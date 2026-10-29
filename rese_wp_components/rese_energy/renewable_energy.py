

import numpy as np


class RenewableEnergy:


    def __init__(self):
        # Configuration and inputs
        self.capacity_mw = 100


        self.hourly_cf = None

        #Outputs
        # Computed attributes/values
        self.hourly_output_mw = None #Standard naming
        self.cumulative_energy_gwh = None

        # Results dictionary
        self.results = None #Standard naming


    #------------------------------------------------------------
    # Configuration
    #-------------------------------------------------------------


    def configure(self, config=None):
        if config is None:
            return

        self.capacity_mw = config.get("capacity_mw",self.capacity_mw)

        self.hourly_cf = config.get("hourly_cf", self.hourly_cf)



    #------------------------------------------------------------
    # HELPER METHODS
    #-------------------------------------------------------------

    def _calculate_hourly_output(self, hourly_cf):

        return hourly_cf * self.capacity_mw

    def _calculate_cumulative_energy_gwh(self, hourly_output_mw):

        return np.cumsum(hourly_output_mw) / 1000


    #------------------------------------------------------------
    # Evaluate
    #-------------------------------------------------------------

    
    def evaluate(self):

        if self.hourly_cf is None:
            raise ValueError(
                "hourly_cf must be provided in the configuration."
            )


        # Calculate hourly output
        self.hourly_output_mw = self._calculate_hourly_output(
            self.hourly_cf
        )

        # Calculate cumulative energy
        self.cumulative_energy_gwh_hourly = (
            self._calculate_cumulative_energy_gwh(
                self.hourly_output_mw
            )
        )
        

        self.results = {
            "hourly_output_mw": self.hourly_output_mw,
            "cumulative_energy_gwh_hourly": self.cumulative_energy_gwh_hourly,
        }

        return self.results




hourly_c1 = np.array([0.5, 0.42, 0.55, 0.30, 0.65])
hourly_cf2 = np.array([0.05, 0.42, 0.55, 0.30, 0.65])
hourly_cf3 = df_1["cf"].to_numpy()

#naming a scenario
scenario_1 = RenewableEnergy()

#scenario 2
scenario_2 = RenewableEnergy()

scenario_3 = RenewableEnergy()

#nconfige the scenario. . .  creating an instance
scenario_1.configure({
    "capacity_mw": 100,
    "hourly_cf": hourly_cf3
})


#nconfige the scenario
scenario_2.configure({
    "capacity_mw": 200,
    "hourly_cf": hourly_cf3
})

scenario_3.configure({
    "capacity_mw": 300,
    "hourly_cf": hourly_cf3
})


#save all the outputs to to result
results_scenario_1 =scenario_1.evaluate() # is defined as a dictionary,we save all the outputs in that dictionary

results_scenario_2 =scenario_2.evaluate()

results_scenario_3 =scenario_3.evaluate()

#accessing a dictionary value
print("Hourly output (MW) Scenario 1:", results_scenario_1["hourly_output_mw"])
print("Hourly output (MW) Scenario 2:", results_scenario_2["hourly_output_mw"])
print("Hourly output (MW) Scenario 3:", results_scenario_3["hourly_output_mw"])
