class Upgrade:
    buy_index = 0
    def __init__(self, name: str, description: str, cost: int, effect: str, effect_amount: int):
        self.name = name
        self.description = description
        self.cost = cost
        Upgrade.buy_index += 1
        self.shop_index = Upgrade.buy_index
        self.effect = effect
        self.effect_amount = effect_amount

donkey = Upgrade("Old Donkey", "An old, bad smelling donkey with yellow teeth. But basically free. Increases your gold generation rate by 1.", 10
                 , "gold", 1)

lead_shipping = Upgrade("Lead Shipping", "A steady supply of lead from the closest mine - it's not a big one, though. Increases your lead generation rate by 10", 50
                        , "lead", 10)