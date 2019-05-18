"""
Restaurant module
"""
import numpy as np
from group import Group
from headwaiter import Headwaiter
from buffet import Buffet
from queue import Queue
from table import Table
from waiter import Waiter
from cashier import Cashier


class Restaurant:
    """
    Restaurant stores all the data that the other classes need

    """
    def __init__(self):
        self.simulation_time = 0
        self.queue_buffet = Queue()
        self.queue_headwaiter = Queue()
        self.queue_cashiers = Queue()
        self.buffet = Buffet()
        self.headwaiter = Headwaiter()
        self.table_1 = Table(1, 2)
        self.table_2 = Table(2, 2)
        self.table_3 = Table(3, 3)
        self.table_4 = Table(4, 4)
        self.waiter_1 = Waiter(1)
        self.waiter_2 = Waiter(2)
        self.waiter_3 = Waiter(3)
        self.waiter_4 = Waiter(4)
        self.waiter_5 = Waiter(5)
        self.waiter_6 = Waiter(6)
        self.waiter_7 = Waiter(7)
        self.cashier_1 = Cashier(1)
        self.cashier_2 = Cashier(2)
        self.cashier_3 = Cashier(3)
        self.cashier_4 = Cashier(4)
        self.waiters = [self.waiter_1, self.waiter_2, self.waiter_3,
                        self.waiter_4, self.waiter_5, self.waiter_6,
                        self.waiter_7]
        self.cashiers = [self.cashier_1, self.cashier_2, self.cashier_3,
                         self.cashier_4]
        self.tables = [self.table_1, self.table_2, self.table_3, self.table_4]
        self.group_quant = []
        self.next_appearance_time = 0
