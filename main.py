# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.intent is not None:
            return
        ball_distance = abs(self.ball.location.y - self.foe_goal.location.y)
        self_distance = abs(self.me.location.y - self.foe_goal.location.y)
        is_in_front_of_ball = ball_distance > self_distance
        if self.kickoff_flag:
            # set_intent tells the bot what it's trying to do
            self.set_intent(kickoff())
            return
        
        # if we are in front of the ball, retreat
        if is_in_front_of_ball:
            self.set_intent(goto(self.friend_goal.location))
            return
        self.set_intent(short_shot(self.foe_goal.location))

        #playing around with lists
        targets = {
            'at_opponent goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post) 
        }
        hits = find_hits(self, targets)
        if len(hits['at_opponent goal']) > 0
            self.set_intent(hits['at opponent goal'][0])
            return
        if len(hits['away_from_our_net']) > 0
            self.set_intent(hits['away_from_our_net'][0])
            return
