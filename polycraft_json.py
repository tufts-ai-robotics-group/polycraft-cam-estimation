import json

import numpy as np


def get_p_json_cam(p_json_name):
    with open(p_json_name, "r") as f:
        p_json = json.load(f)
        player_pos = np.array(p_json["player"]["pos"], dtype=float)
        yaw = p_json["player"]["yaw"]
        pitch = p_json["player"]["pitch"]
        return player_pos, yaw, pitch


def get_p_json_pts(p_json_name, ignore_blocks=["air"]):
    ignore_blocks = {"minecraft:" + block for block in ignore_blocks}
    with open(p_json_name, "r") as f:
        p_json = json.load(f)
        pts = np.empty((0, 3))
        for pos, data in p_json["map"].items():
            if data["name"] not in ignore_blocks:
                pts = np.concatenate((pts, np.fromstring(pos, sep=",")[np.newaxis]), axis=0)
        return pts.T
