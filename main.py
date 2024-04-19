#from agents import trendScrapper
from agents.collector import CollectorAgent
from agents.mapper import MapperAgent
from agents.caller import CallerAgent
from agents.manager import ManagerAgent
from spade import quit_spade
import time

XMPP_SERVER = 'localhost'
PASSWORD = 'admin'

if __name__ == "__main__":
    caller = CallerAgent(f"caller@{XMPP_SERVER}", PASSWORD)
    manager = ManagerAgent(f"manager@{XMPP_SERVER}", PASSWORD)

    res_manager = manager.start(auto_register=True)
    res_manager.result()

    time.sleep(1)

    res_caller = caller.start(auto_register=True)
    res_caller.result()
    
    time.sleep(1)

        # Handle interruption of all agents
    while manager.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            # stop all agents
            caller.stop()
            manager.stop()

            break

    print("Agents finished")

    quit_spade()

