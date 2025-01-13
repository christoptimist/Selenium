from typing import List
from fake_useragent import UserAgent
import random

class UserAgents:
    def __init__(self, user_agent_list: List[str] = None):
        self._user_agent_list = user_agent_list or self._generate_random_user_agents()

    def _generate_random_user_agents(self, num_agents: int = 10) -> List[str]:
        ua = UserAgent()
        return [ua.random for _ in range(num_agents)]

    def get_random_user_agent(self) -> str:
        return random.choice(self._user_agent_list)