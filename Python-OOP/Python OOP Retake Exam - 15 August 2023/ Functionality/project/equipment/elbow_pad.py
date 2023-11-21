from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=90, price=25)

    @property
    def get_added_price(self):
        return self.price * 0.1
      
