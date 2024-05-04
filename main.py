from ui.portfolio import PortfolioPage
from agents.manager import ManagerAgent
from agents.collector import CollectorAgent
from agents.mapper import MapperAgent
from agents.caller import CallerAgent
from agents.manager import ManagerAgent
from agents.broker import BrokerAgent
from spade import quit_spade
from ui.ui import MainPage
import time


XMPP_SERVER = 'localhost'
PASSWORD = 'admin'

if __name__ == "__main__":
    caller = CallerAgent(f"caller@{XMPP_SERVER}", PASSWORD)
    mapper = MapperAgent(f"mapper@{XMPP_SERVER}", PASSWORD)
    broker = BrokerAgent(f"broker@{XMPP_SERVER}", PASSWORD)
    manager = ManagerAgent(f"manager@{XMPP_SERVER}", PASSWORD)

    res_manager = manager.start(auto_register=True)
    res_manager.result()

    time.sleep(1)

    res_mapper = mapper.start(auto_register=True)
    res_mapper.result()

    time.sleep(1)

    res_broker = broker.start(auto_register=True)
    res_broker.result()

    time.sleep(1)

    res_caller = caller.start(auto_register=True)
    res_caller.result()

    time.sleep(1)

    app = MainPage(manager)
    app.root.mainloop()

    # Handle interruption of all agents
    while manager.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            # stop all agents
            caller.stop()
            manager.stop()
            broker.stop()
            mapper.stop()

            break

    print("Agents finished")

    quit_spade()
    