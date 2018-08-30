#!/usr/bin/env python
# coding: utf-8

from ams import get_namedtuple_from_dict
from ams.nodes.base.const import const as base_const


topic = {
    "CATEGORIES": {}
}
topic["CATEGORIES"].update(base_const["TOPIC"]["CATEGORIES"])
topic["CATEGORIES"].update({
    "CONFIG": ["config"],
    "STATUS": ["status"],
    "SCHEDULES": ["schedules"],
})

mission_event = {
    "START_MISSION": "start_mission",
    "END_MISSION": "end_mission"
}

event = {
    "START": "start",
    "INITIALIZE": "initialize",
    "ACTIVATE": "activate",
    "DEACTIVATE": "deactivate",
    "END": "end"
}
event.update(mission_event)

state = {
    "START_PROCESSING": "start_processing",
    "INITIALIZED": "initialized",
    "ACTIVE": "active",
    "MISSION_STARTED": "mission_started",
    "MISSION_ENDED": "mission_ended",
    "INACTIVE": "inactive",
    "END_PROCESSING": "end_processing"
}

const = {}
const.update(base_const)
const.update({
    "NODE_NAME": "infra",
    "ROLE_NAME": "infra",
    "TOPIC": topic,
    "EVENT": event,
    "STATE": state,
    "MISSION_EVENTS": mission_event.values(),
})

CONST = get_namedtuple_from_dict("CONST", const)
