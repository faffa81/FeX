#ifndef MACRO_CONFIG_INT
#error "The config macros must be defined"
// This helps IDEs properly syntax highlight the uses of the macro below.
#define MACRO_CONFIG_INT(Name, ScriptName, Def, Min, Max, Save, Desc)
#define MACRO_CONFIG_COL(Name, ScriptName, Def, Save, Desc)
#define MACRO_CONFIG_STR(Name, ScriptName, Len, Def, Save, Desc)
#endif

#define cfgint(Name, ScriptName, Def, Desc) \
	MACRO_CONFIG_INT(Name, ScriptName, Def, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, Desc)
#define cfgintex(Name, ScriptName, Def, Min, Max, Flags, Desc) \
	MACRO_CONFIG_INT(Name, ScriptName, Def, Min, Max, Flags, Desc)
#define cfgcol(Name, ScriptName, Def, Desc) \
	MACRO_CONFIG_COL(Name, ScriptName, Def, CFGFLAG_CLIENT | CFGFLAG_SAVE, Desc)
#define cfgcolex(Name, ScriptName, Def, Flags, Desc) \
	MACRO_CONFIG_COL(Name, ScriptName, Def, Flags, Desc)
#define cfgstr(Name, ScriptName, Len, Def, Desc) \
	MACRO_CONFIG_STR(Name, ScriptName, Len, Def, CFGFLAG_CLIENT | CFGFLAG_SAVE, Desc)
#define cfgstrex(Name, ScriptName, Len, Def, Flags, Desc) \
	MACRO_CONFIG_STR(Name, ScriptName, Len, Def, Flags, Desc)


// client

// War List
MACRO_CONFIG_INT(FXWarList, fx_warlist, 1, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Toggles war list visuals")
MACRO_CONFIG_INT(FXWarListShowClan, fx_warlist_show_clan_if_war, 0, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Show clan in nameplate if there is a war")
MACRO_CONFIG_INT(FXWarListReason, fx_warlist_reason, 1, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Show war reason")
MACRO_CONFIG_INT(FXWarListChat, fx_warlist_chat, 1, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Show war colors in chat")
MACRO_CONFIG_INT(FXWarListScoreboard, fx_warlist_scoreboard, 1, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Show war colors in scoreboard")
MACRO_CONFIG_INT(FXWarListAllowDuplicates, fx_warlist_allow_duplicates, 1, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Allow duplicate war entries")
MACRO_CONFIG_INT(FXWarListSpectate, fx_warlist_spectate, 1, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Show war colors in spectator menu")

MACRO_CONFIG_INT(FXWarListIndicator, fx_warlist_indicator, 0, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Use warlist for indicator")
MACRO_CONFIG_INT(FXWarListIndicatorColors, fx_warlist_indicator_colors, 0, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Show warlist colors instead of freeze colors")
MACRO_CONFIG_INT(FXWarListIndicatorAll, fx_warlist_indicator_all, 1, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Show all groups")
MACRO_CONFIG_INT(FXWarListIndicatorEnemy, fx_warlist_indicator_enemy, 1, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Show players from the first group")
MACRO_CONFIG_INT(FXWarListIndicatorTeam, fx_warlist_indicator_team, 1, 0, 1, CFGFLAG_CLIENT | CFGFLAG_SAVE, "Show players from second group")