// This file can be included several times.

#ifndef CONFIG_DOMAIN
#error "CONFIG_DOMAIN macro not defined"
#define CONFIG_DOMAIN(Name, ConfigPath, HasVars) ;
#endif

CONFIG_DOMAIN(DDNET, "settings_ddnet.cfg", true)
CONFIG_DOMAIN(FX, "settings_fx.cfg", true)
CONFIG_DOMAIN(FXPROFILES, "fx_profiles.cfg", false)
CONFIG_DOMAIN(FXCHATBINDS, "fx_chatbinds.cfg", false)
CONFIG_DOMAIN(FXWARLIST, "fx_warlist.cfg", false)
