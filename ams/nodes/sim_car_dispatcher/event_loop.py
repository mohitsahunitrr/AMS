#!/usr/bin/env python
# coding: utf-8

from ams.nodes.dispatcher import EventLoop as DispatcherEventLoop
from ams.nodes.sim_car import Message as SimCarMessage
from ams.nodes.sim_car_dispatcher import CONST, Structure, Message, Helper, Publisher, StateMachine, Subscriber


class EventLoop(DispatcherEventLoop):

    CONST = CONST
    Structure = Structure
    Message = Message
    Helper = Helper
    Publisher = Publisher
    StateMachine = StateMachine
    Subscriber = Subscriber

    VehicleMessage = SimCarMessage

    def __init__(self, _id, group=CONST.NODE_NAME):
        super().__init__(_id, group)
        self.initials = {
            "config": None,
            "state": self.CONST.STATE.START_PROCESSING,
            "schedules": None
        }

    def set_initial_config(self, targets, active_api_keys=None, inactive_api_keys=None, stop_waypoint_ids=None):
        self.initials["config"] = self.Structure.Config.new_data(
            targets=targets,
            active_api_keys=active_api_keys if active_api_keys is not None else [],
            inactive_api_keys=inactive_api_keys if inactive_api_keys is not None else [],
            stop_waypoint_ids=stop_waypoint_ids if stop_waypoint_ids is not None else []
        )

    def start(self):
        self.__set_dispatcher_subscriber()

        self.__connect_and_set_user_data()

        self.Helper.set_dispatcher_config(self.user_data["kvs_client"], self.target, self.initials["config"])
        self.Helper.set_dispatcher_state(self.user_data["kvs_client"], self.target, self.initials["state"])

    def stop(self):
        self.user_data["mqtt_client"].disconnect()