from otree.api import *


doc = """
Stage One
"""


class C(BaseConstants):
    NAME_IN_URL = 'stageone'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    price = models.IntegerField(min=0, max=10) 
    tech = models.IntegerField(choices=[[1, 'low'],[2, 'high']])
    payment = models.CurrencyField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['price', 'tech']


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        total_prices = sum([p.price for p in group.get_players()])
        for p in group.get_players():
            p.payment = 2*p.price + (total_prices)/2

# Page Class
class Results(Page):
    # Function - Passes variables to the
    # template
    def vars_for_template(player):
        # Returning a dictionary with the
        # key (price) as the label
        # value as the key value
        return {
            'price': player.price,
            'payment': player.payment,
        }


page_sequence = [MyPage, ResultsWaitPage, Results]
