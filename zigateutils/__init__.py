"""
ZiGate Utils component.
"""

import logging
import voluptuous as vol
from homeassistant.const import ATTR_ENTITY_ID
import homeassistant.helpers.config_validation as cv

# from homeassistant.helpers.entity_component import EntityComponent
# from .frontend.views.nework import (
    # ZigateNetworkView,
# )

DOMAIN = 'zigateutils'
ZIGATE_DOMAIN = 'zigate'
GROUP_NAME_ALL_ZIGATEUTILS = 'all zigateutils'

_LOGGER = logging.getLogger(__name__)

ADDR = 'addr'
IEEE = 'ieee'

LEAVE_AND_REJOIN_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
	vol.Optional('rejoin'): cv.boolean,
	vol.Optional('remove_children'): cv.boolean,
})

def setup(hass, config):
    myzigate = hass.data[ZIGATE_DOMAIN]
    # component = EntityComponent(_LOGGER, DOMAIN, hass,
    #                             group_name=GROUP_NAME_ALL_ZIGATEUTILS)

    # Register views
    # hass.http.register_view(ZigateNetworkView())

    def _get_addr_from_service_request(service):
        entity_id = service.data.get(ATTR_ENTITY_ID)
        ieee = service.data.get(IEEE)
        addr = service.data.get(ADDR)
        if entity_id:
            entity = component.get_entity(entity_id)
            if entity:
                addr = entity._device.addr
        elif ieee:
            device = myzigate.get_device_from_ieee(ieee)
            if device:
                addr = device.addr
        return addr

    def leave_and_rejoin(service):
        addr = service.data.get('addr')
        ieee = service.data.get('ieee', None)
        if addr:
          myzigate.permit_join()
          myzigate.leave_request(addr, ieee=ieee, rejoin=True, remove_children=False)

    hass.services.register(DOMAIN, 'leave_and_rejoin', leave_and_rejoin,
                           schema=LEAVE_AND_REJOIN_SCHEMA)

    return True