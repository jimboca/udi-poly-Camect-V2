
from polyinterface import Node,LOGGER
from node_funcs import id_to_address,get_valid_node_name
from const import DETECTED_OBJECT_MAP

class DetectedObject(Node):
    id = 'objdet' # Placeholder, gets overwritten in __init__
    drivers = [
        {'driver': 'ST',  'value': 0, 'uom': 2}, # Enabled
    ]

    def __init__(self, controller, primary, otype):
        self.id = otype
        self.map = DETECTED_OBJECT_MAP[otype]
        address = f'{primary.address}{otype[:1]}'
        name    = f'{primary.name} {otype}'
        super(DetectedObject, self).__init__(controller, primary.address, address, name)
        self._mydrivers = {}
        self.dname_to_driver = {}
        self.lpfx = '%s:%s' % (self.address,self.name)
        for obj_name in self.map:
            dv = 'GV' + str(self.map[obj_name]['num'])
            self.drivers.append({'driver':  dv, 'value': 0, 'uom': 2})
            # Hash of my detected objects to the driver
            self.dname_to_driver[obj_name] = dv

    def start(self):
        LOGGER.debug(f'{self.lpfx}')
        self.setDriver('ST',0)
        for dn in self.dname_to_driver:
            self.setDriver(self.dname_to_driver[dn], 0)

    def shortPoll(self):
        pass

    def longPoll(self):
        pass

    def clear(self):
        if int(self.get_driver('ST')) == 1:
            LOGGER.debug(f'{self.lpfx}')
            self.reportCmd("DOF",2)
            for obj in self.dname_to_driver:
                self.set_driver(self.dname_to_driver[obj], 0)

    # This is called by parent when object is detected
    def turn_on(self,obj):
        LOGGER.debug(f"{self.lpfx}")
        self.reportCmd("DON",2)
        self.set_driver(self.dname_to_driver[obj],1)

    # This is called by parent when object is no longer detected
    def turn_off(self,obj):
        LOGGER.debug(f"{self.lpfx}")
        self.reportCmd("DOF",2)
        self.set_driver(self.dname_to_driver[obj],0)

    def cmd_on(self, command=None):
        LOGGER.debug(f"{self.lpfx} command={command} ST={self.get_driver('ST')}")
        self.set_driver('ST', 1)

    def cmd_off(self, command=None):
        LOGGER.debug(f"{self.lpfx} command={command} ST={self.get_driver('ST')}")
        self.set_driver('ST', 1)

    def query(self,command=None):
        LOGGER.debug(f'{self.lpfx}')
        self.reportDrivers()

    def set_driver(self,drv,val):
        self._mydrivers[drv] = val
        self.setDriver(drv,val)

    def get_driver(self,drv):
        if drv in self._mydrivers:
            return self._mydrivers[drv]
        return self.getDriver(drv)

    hint = [1,2,3,4]
    commands = {
                    'DON': cmd_on,
                    'DOF': cmd_off,
                }
