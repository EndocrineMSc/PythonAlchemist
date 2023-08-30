import sched, time
from ShopCondition import Shop
from pynput.mouse import Listener
from Upgrade import Upgrade
import threading

class LoopHandler():
    alchemist_shop = Shop()

    # visualization and game-loop
    scheduler = sched.scheduler(time.time, time.sleep)
    
    def on_click(self, x, y, button, pressed):
        if pressed:
            self.alchemist_shop.converse_lead()
    
    def start_mouse_listener(self):
        listener_thread = threading.Thread(target=self.run_listener)
        listener_thread.start()
        
    def run_listener(self):    
        with Listener(on_click=self.on_click) as listener:
            listener.join()

    def new_timed_call(self, calls_per_second, callback, *args, **kw):
        period = 1.0 / calls_per_second
        def reload():
            callback(*args, **kw)
            self.scheduler.enter(period, 0, reload, ())
        self.scheduler.enter(period, 0 , reload, ())
        
    def generate_resources(self):
        self.alchemist_shop.generate_lead()
        self.alchemist_shop.generate_gold()

    def purchase_upgrade(self):
        def input_thread():
           try:
               upgrade_choice = int(input("Enter the number of the upgrade you want to purchase: "))
               if upgrade_choice >= 0 and upgrade_choice <= len(self.alchemist_shop.remaining_upgrades):
                   self.alchemist_shop.unlock_upgrade(upgrade_choice)
               self.purchase_upgrade()
           except ValueError:
               print("Invalid input. Please enter a valid number")
               self.purchase_upgrade()
        input_thread = threading.Thread(target=input_thread)
        input_thread.start()
                       
    def clear_terminal(self):
        print("\n" * 10)
        
    def print_intro(self):
        print("You are an alchemist, converting lead to gold. Click with your mouse to do so, while this program runs.")
        print("You can purchase upgrades to your shop by entering the corresponding number into the terminal (given that you have enough gold)")
        print("\n")
        
    def print_resources(self):
        print("Gold: " + str(self.alchemist_shop.gold))
        print("Lead: " + str(self.alchemist_shop.lead))
        print("Gold auto-generation rate per 10 seconds: " + str(self.alchemist_shop.gold_rate))
        print("Lead auto-generation rate per 10 seconds: " + str(self.alchemist_shop.lead_rate))
        print("\n")
        
    def print_upgrades(self):
        upgrades = self.alchemist_shop.remaining_upgrades
        print("Available upgrades: ")
        for item in upgrades:
            print("Upgrade number: " + str(upgrades.index(item) + 1) + " // Name: " + item.name + " // Cost: " + str(item.cost))
        print("\n")
        bought_upgrades = self.alchemist_shop.unlocked_upgrades
        print("Bought_upgrades: ")
        for item in bought_upgrades:
            print(item.name + ": " + item.description)
        print("\n")

# actual actions
game_loop = LoopHandler()
game_loop.new_timed_call(1, game_loop.print_intro)
game_loop.new_timed_call(1, game_loop.print_resources)
game_loop.new_timed_call(1, game_loop.generate_resources)
game_loop.new_timed_call(1, game_loop.print_upgrades)
game_loop.purchase_upgrade()
game_loop.start_mouse_listener()
game_loop.scheduler.run()
