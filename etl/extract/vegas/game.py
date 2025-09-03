def scrape_team_code(team_tr: str) -> str:
    """Method that extracts Veges Insider team code"""
    try:
        return team_tr.find("td", class_="game-team").find("div", class_="team-plate").find("span").find("a")["data-abbr"]
    except:
        return None


def scrape_team_win_percentage(team_tr: str) -> str:
    """Method that extracts Vegas Insider team win percentage"""
    # ex: <tr> <td class="game-team"> <div class="team-plate"> <img width="25" height="25" data-role="imagable" data-src="https://static.sprtactn.co/teamlogos/ncaaf/100/boise.png" src="https://bctn-vi.s3.amazonaws.com/img/favicon.svg?v=09c6937" alt="Boise State Broncos"> <span> <span> 143 </span> <a href="/college-football/teams/boise-state/" class="team-name " data-abbr="BOISE" aria-label="Boise State"> <span> Boise State </span> </a> </span> </div> </td> <td> <div class="mobile-wrap"> <span class="pill bold highlight">70%</span></div></td>   <td> <div class="mobile-wrap"> <span class="pill bold matte">41%</span></div></td>   <td> <div class="mobile-wrap"> <span class="small"> 0-0 SU </span> <span class="pill bold highlight">90%</span></div></td>   </tr>
    try:
        return team_tr.find_all("td")[3].find("div").find_all("span")[-1].get_text()
    except:
        return None


def scrape_team_spread(consensus_tr: str) -> str:
    """Method that extract Vegas Insider team win percentage"""
    pass


