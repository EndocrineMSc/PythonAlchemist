# Shop Condition Module
import Upgrade

class Shop:
    # total current amounts
    gold = 0
    lead = 100
    
    # generation rates
    gold_rate = 0
    lead_rate = 100
    conversion_per_click = 1
    
    # all available upgrades with unlock status
    remaining_upgrades = [Upgrade.donkey, Upgrade.lead_shipping]
    unlocked_upgrades = []
    
    # counters
    lead_counter = 0
    lead_counter_max = 10
    gold_counter = 0
    gold_counter_max = 10

    # methods for changes to resources and upgrades
    def add_gold(self, amount=1):
        self.gold += amount

    def add_lead(self, amount=100):
        self.lead += amount

    def remove_gold(self, amount=1):
        self.gold -= amount
        
    def remove_lead(self, amount=1):
        self.lead -= amount
        
    def converse_lead(self):
        if self.lead >= self.conversion_per_click:
            self.add_gold(self.conversion_per_click)
            self.remove_lead(self.conversion_per_click)
        else:
            print("Not enough lead remaining!")
        
    def unlock_upgrade(self, upgrade_index):
        if upgrade_index >= 0 and upgrade_index - 1 < len(self.remaining_upgrades):
            upgrade = self.remaining_upgrades[upgrade_index - 1]
            
            if (self.gold >= upgrade.cost):
                self.remove_gold(upgrade.cost)
                
                if upgrade.effect == "gold":
                    self.gold_rate += upgrade.effect_amount
                else:
                    self.lead_rate += upgrade.effect_amount
                    
                self.remaining_upgrades.remove(upgrade)
                self.unlocked_upgrades.append(upgrade)
                
                print("You bought: " + upgrade.name + ". \n" + upgrade.description)
                
            else:
                print("Not enough gold to buy this upgrade!")
        else:
            print("Chosen upgrade does not exist!")
            
    def generate_lead(self):
        self.lead_counter += 1
        if self.lead_counter >= self.lead_counter_max:
            self.lead += self.lead_rate
            self.lead_counter = 0
            
    def generate_gold(self):
        self.gold_counter += 1
        if self.gold_counter >= self.gold_counter_max:
            self.gold += self.gold_rate
            self.gold_counter = 0
            
        


        
            

                
                



        