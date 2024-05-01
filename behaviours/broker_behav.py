import jsonpickle
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class BrokerBehaviour(CyclicBehaviour):
    async def on_start(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : starting behaviour...")

    async def run(self):
        print(f"{str(self.agent.jid).partition('@')[0]} : behaviour running...")

        msg = await self.receive(timeout=10)

        if msg:
           performative = msg.get_metadata("performative")
           msg_to_manager = Message(to=str(msg.sender)) 

           if performative == "request":
               request = jsonpickle.decode(msg.body)
               decision = request.getDecision()
               if decision == "buy":
                   message = f"{str(self.agent.jid).partition('@')[0]} : buying {request.getQuantity()} of {request.getCrypto()} at {request.getValue()}"
                   print(message)
                   request.setMessage(message)
                    
               else:
                   message = f"{str(self.agent.jid).partition('@')[0]} : selling {request.getQuantity()} of {request.getCrypto()} at {request.getValue()}"
                   print(message)
                   request.setMessage(message)
                   
               msg_to_manager.body = jsonpickle.encode(request)
               msg_to_manager.set_metadata("performative", "confirm") 
               
           else:
                msg_to_manager.set_metadata("performative", "refuse") 
                
           await self.send(msg_to_manager)
                

        else:
            print(f"{str(self.agent.jid).partition('@')[0]} : message timeout after 10 seconds")