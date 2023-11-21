from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=120, price=15)

    @property
    def get_added_price(self):
        return self.price * 0.2
      
