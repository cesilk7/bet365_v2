# login
login = '//div[contains(@class, "hm-MainHeaderRHSLoggedOutWide_Login")]'
login_user = '//input[contains(@class, "lms-StandardLogin_Username")]'
login_pass = '//input[contains(@class, "lms-StandardLogin_Password")]'
login_btn = '//div[contains(@class, "lms-LoginButton")]'

football_icon = '//div[contains(@class, "cil-ClassificationIconLarge-1")]'

top_game = '//div[contains(@class, "ovm-FixtureDetailsTwoWay ovm-FixtureDetailsTwoWay-1")]'
closed_league = '//div[contains(@class, "ipn-Competition ipn-Competition-closed")]'

game_timer = '//div[contains(@class, "ipn-Fixture_TimerContainer")]'
game_scores = '//div[contains(@class, "ScoresDefault")]/div/div'

fulltime_result_text = '//div[contains(text(), "Fulltime Result")]'
number_of_amg = '//div[contains(text(), "Alternative Match Goals")]/parent::node()/following-sibling::div[1]/div/div/div[contains(@class, "srb-ParticipantLabelCentered")]'

# stats info
stats_tag = '//div[contains(@class, "ml-StatButtons_Button-stats")]'
attacks_1 = '//div[contains(text(), "Attacks") and not(contains(text(), "Dangerous Attacks"))]/following-sibling::div[1]/div[1]'
attacks_2 = '//div[contains(text(), "Attacks") and not(contains(text(), "Dangerous Attacks"))]/following-sibling::div[1]/div[3]'
d_attacks_1 = '//div[contains(text(), "Dangerous Attacks")]/following-sibling::div[1]/div[1]'
d_attacks_2 = '//div[contains(text(), "Dangerous Attacks")]/following-sibling::div[1]/div[3]'
possession_1 = '//div[contains(text(), "Possession %")]/following-sibling::div[1]/div[1]'
possession_2 = '//div[contains(text(), "Possession %")]/following-sibling::div[1]/div[3]'
yellow_card_1 = '//div[contains(@class, "ml1-StatsLower")]/div[1]/div/div/div[1]/div[2]'
yellow_card_2 = '//div[contains(@class, "ml1-StatsLower")]/div[3]/div/div/div[3]/div[2]'
red_card_1 = '//div[contains(@class, "ml1-StatsLower")]/div[1]/div/div/div[2]/div[2]'
red_card_2 = '//div[contains(@class, "ml1-StatsLower")]/div[3]/div/div/div[2]/div[2]'
corner_kick_1 = '//div[contains(@class, "ml1-StatsLower")]/div[1]/div/div/div[3]/div[2]'
corner_kick_2 = '//div[contains(@class, "ml1-StatsLower")]/div[3]/div/div/div[1]/div[2]'
on_target_1 = '//div[contains(@class, "ml1-StatsLower_MiniBarsCollection")]/div[1]/div/div/b[1]'
on_target_2 = '//div[contains(@class, "ml1-StatsLower_MiniBarsCollection")]/div[1]/div/div/b[2]'
off_target_1 = '//div[contains(@class, "ml1-StatsLower_MiniBarsCollection")]/div[2]/div/div/b[1]'
off_target_2 = '//div[contains(@class, "ml1-StatsLower_MiniBarsCollection")]/div[2]/div/div/b[2]'

# summary info
summary_tag = '//div[contains(@class, "ml-StatButtons_Button-summary")]'
show_more = '//div[contains(@class, "ml-Summary_Link")]'
play_time = '//span[contains(@class, "ml1-SoccerClock_Clock")]'
shifts_1 = '//div[contains(@class, "ml1-StatBoardColumn_Icon-9")]/following-sibling::div[1]'
shifts_2 = '//div[contains(@class, "ml1-StatBoardColumn_Icon-9")]/following-sibling::div[2]'
pk_1 = '//div[contains(@class, "ml1-StatBoardColumn_Icon-8")]/following-sibling::div[1]'
pk_2 = '//div[contains(@class, "ml1-StatBoardColumn_Icon-8")]/following-sibling::div[2]'
goal_1 = '//div[contains(@class, "ml1-StatBoardColumn_Icon-1")]/following-sibling::div[1]'
goal_2 = '//div[contains(@class, "ml1-StatBoardColumn_Icon-1")]/following-sibling::div[2]'
home_goals = '//div[contains(@class, "ml-SummaryRow_TextIcon-1")]/span[contains(@class, "ml1-SoccerSummaryRow_GoalText")]/../following-sibling::div[1]'
away_goals = '//div[contains(@class, "ml-SummaryRow_TextIcon-2")]/span[contains(@class, "ml1-SoccerSummaryRow_GoalText")]/../preceding-sibling::div[1]'
