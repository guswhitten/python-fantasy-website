# Football API
import matplotlib as mpl
import bar_chart_race as bcr
import pandas as pd


# CONSTANTS
IMG_WIDTH = 70
IMG_HEIGHT = 70
            
def create_chart_race(league):
    hash_wins = {}
    hash_points = {}
    weeks = list(range(0,16))
    # build wins hash
    for each_team in league.teams:
        wins_by_week = [0]
        list_of_outcomes = each_team.outcomes
        wins = 0
        for result in list_of_outcomes:
            if result == 'W':
                wins += 1
            wins_by_week.append(wins)
        hash_wins[each_team.team_name] = wins_by_week
        
    # build points hash
    for each_team in league.teams:
        pts_by_week = [0]
        scores = each_team.scores
        pts = 0
        for result in scores:
            pts += result
            pts_by_week.append(pts)
        hash_points[each_team.team_name] = pts_by_week

    league_size = int(len(league.teams))
    df = pd.DataFrame(hash_points)

    bcr.bar_chart_race(
        df=df,
        filename='static/img/fantasy.mp4',
        orientation='h',
        sort='desc',
        n_bars=league_size,
        fixed_order=False,
        fixed_max=True,
        steps_per_period=10,
        interpolate_period=False,
        label_bars=True,
        bar_size=.95,
        period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
        period_fmt='Week{x:10.1f}',
        perpendicular_bar_func='max',
        period_length=800,
        figsize=(5, 3),
        dpi=144,
        cmap='dark24',
        title=league.settings.name,
        bar_label_size=7,
        tick_label_size=9,
        shared_fontdict={'family' : 'Courier New', 'color' : '.1', 'weight': 'bold'},
        bar_kwargs={'alpha': .7, 'ec': 'black'},
        filter_column_colors=False)
        

    
    



