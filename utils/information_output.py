from utils.show_seria_a import show_matches, show_link_matches

def send_information_seria_a():
    tmp_list = []
    data, time_list, home_team_list, guest_team_list = show_matches()
    link_list = show_link_matches()
    for time, home_teams, guest_team, link in zip(time_list, home_team_list, guest_team_list, link_list):
        s  = ''
        s += '{}: {} - {}\n{}\n'.format(time.strip(), home_teams.strip(), guest_team.strip(), link.strip())
        tmp_list.append(s)
    return data, tmp_list