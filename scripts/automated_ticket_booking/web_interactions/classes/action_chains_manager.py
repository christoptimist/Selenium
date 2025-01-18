from web_interactions.classes.action_chains_factory import ActionChainsFactory
from web_interactions.interfaces.i_action_chains import IActionChains


class ActionChainsManager(IActionChains):
    def __init__(self, action_chains_factory: ActionChainsFactory):
        self._action_chains_factory = action_chains_factory

    def create_action_chains(self):
        return self._action_chains_factory.create_action_chains()