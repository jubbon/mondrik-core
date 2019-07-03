#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

from ansible.module_utils.common.collections import ImmutableDict
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.host import Host
from ansible.inventory.manager import InventoryManager
from ansible.playbook import Playbook
from ansible.playbook.play import Play
from ansible.playbook.play_context import PlayContext
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase
from ansible import context as ctx
import ansible.constants as C


class ResultCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin
    """

    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        # print(json.dumps({host.name: result._result}, indent=4))

        stdout_lines = result._result
        print(stdout_lines)
        print("-----")


def execute(playbooks: list, context: dict):
    '''
    '''
    assert playbooks

    os.environ["ANSIBLE_CONDITIONAL_BARE_VARS"] = "False"

    # ctx._init_global_context({})
    # since the API is constructed for CLI it expects certain options to always be set in the context object
    ctx.CLIARGS = ImmutableDict(connection='local',
                                    module_path=['./playbooks/roles'],
                                    forks=1,
                                    become=False,
                                    become_method="sudo",
                                    syntax=False,
                                    start_at_task=None,
                                    diff=False,
                                    verbosity=0)

    # initialize needed objects
    loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
    # passwords = dict(become_pass="password")
    passwords = dict()

    # Instantiate our ResultCallback for handling results as they come in. Ansible expects this to be one of its main display outlets
    results_callback = ResultCallback()

    # create inventory, use path to host config file as source or hosts in a comma separated string
    inventory = InventoryManager(loader=loader, sources='localhost,')

    host = Host(name="localhost")
    # variable manager takes care of merging all the different sources to give you a unified view of variables available in each context
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    variable_manager.set_host_variable(host, "current_directory", context.get("current_directory", ""))

    pbex = PlaybookExecutor(playbooks=playbooks,
                            inventory=inventory,
                            variable_manager=variable_manager,
                            loader=loader,
                            passwords=passwords)
    return pbex.run()