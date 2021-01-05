from iqoptionapi2.ws.chanels.base import Base
import time
import iqoptionapi2.global_value as global_value
class GetDeferredOrders(Base):
    
    name = "sendMessage"

    def __call__(self,instrument_type):
     
        data = {"name":"get-deferred-orders",
                "version":"1.0",
                "body":{
                        "user_balance_id":int(global_value.balance_id),
                        "instrument_type":instrument_type                 
                     
                        }
                }

        self.send_websocket_request(self.name, data)
