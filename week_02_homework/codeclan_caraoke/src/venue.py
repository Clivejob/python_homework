class Venue:

    def __init__(self, name, entry_fee, till):
        self.name = name
        self.entry_fee = entry_fee
        self.till = till
        self.rooms = []
        self.hub_guests = []
        self.stock = {}

    def add_rooms_to_venue(self, room):
            self.rooms.append(room)

    def add_customer_to_venue(self, guest):
         if guest.guest_can_afford_entry(self):
              guest.guest_buy_entry(self)
              self.till += self.entry_fee
              self.hub_guests.append(guest)

    def add_customer_to_room(self, room):
        for guest in self.hub_guests:
            if len(room.attendance) < room.capacity:
                room.add_guest_to_list(guest)

    def add_drink_to_stock(self, drink, quantity):
        if drink in self.stock:
            self.stock[drink] += quantity
        else:
            self.stock[drink] = quantity

    def venue_can_sell_drink(self, guest, drink):
        if drink.name in self.stock:
            if guest.guest_can_afford_drink(drink):
                guest.guest_buy_drink(drink)
                self.till += drink.price
                # self.stock[drink] -= quantity

    # def remove_drink_from_stock(self, drink, quantity):
    #     for booze in self.stock:
    #         if drink == self.stock[booze]:
    #             self.stock[booze] - quantity
    #         else:
    #             self.stock[drink] = quantity

    # def guest_can_afford_entry(self, item):
    #     if self.cash >= item.entry_fee:
    #         return self.cash 

    # def guest_buy_entry(self, venue):
    #     if self.guest_can_afford_entry(venue):
    #         self.cash -= venue.entry_fee

    # def guest_can_buy_entry(self, venue):
    #     if self.guest_can_afford(venue.price):
    #         self.cash -= venue.entry_fee

    # def guest_can_buy_drink(self, drink):
    #     if self.guest_can_afford(drink.price):
    #         self.cash -= drink.price

    # def guest_can_afford(self, item):
    #     return self.cash >= item.price

            # guest_can_afford_entry
            # guest_can_buy_entry

        #   if  customer.customer_can_buy_entry(self):
        # def customer_can_buy_entry(self, venue):
        # if self.cash >= venue.entry_fee:
        #     self.cash -= venue.entry_fee

              

    



         
    

    

    