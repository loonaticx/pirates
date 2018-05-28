# uncompyle6 version 3.2.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.piratesbase.TODData
from pandac.PandaModules import Point3, VBase3, Vec4, Vec3
from pirates.piratesbase.TODDefs import *
ENV_SETTINGS_DEFAULT = {'BASE': {'Direction': Vec3(0, 30, 245), 'LightSwitch': [1, 1, 1], 'FrontColor': Vec4(0, 0, 0, 1), 'BackColor': Vec4(0, 0, 0, 1), 'AmbientColor': Vec4(0, 0, 0, 1), 'FogType': FOG_EXP, 'FogColor': Vec4(0.25, 0.25, 0.25, 0), 'FogExp': 0.0001, 'FogLinearRange': (500.0, 750.0), 'SkyType': SKY_DAY, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.2, 0.2, 0.2, 1), 'SeaColorShader': Vec4(0.2, 0.2, 0.2, 1), 'SeaFactor': Vec3(1.0, 1.0, 1.0), 'EnvEffect': 0}, 'Dawn': {'Direction': Vec3(0, 35, 330), 'FrontColor': Vec4(1.5, 1.2, 0.9, 1), 'BackColor': Vec4(0.35, 0.42, 0.72, 1), 'AmbientColor': Vec4(0.38, 0.53, 0.68, 1), 'FogColor': Vec4(0.29, 0.32, 0.44, 0), 'FogExp': 0.004, 'SkyType': SKY_DAWN, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.35, 0.5, 0.62, 1), 'SeaColorShader': Vec4(0.35, 0.35, 0.2, 1)}, 'Day': {'FrontColor': Vec4(2, 1.79, 1.47, 1), 'BackColor': Vec4(0.35, 0.41, 0.62, 1), 'AmbientColor': Vec4(0.8, 0.88, 0.93, 1), 'FogColor': Vec4(0.6, 0.7, 0.9, 0), 'FogExp': 0.000600000028498, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.3, 0.75, 1, 1), 'SeaColorShader': Vec4(0.1, 0.25, 0.15, 1)}, 'Dusk': {'Direction': Vec3(0, 35, 175), 'FrontColor': Vec4(1.71, 1.36, 1.15, 1), 'BackColor': Vec4(0.59, 0.59, 0.88, 1), 'AmbientColor': Vec4(0.52, 0.39, 0.42, 1), 'FogColor': Vec4(0.46, 0.38, 0.43, 0), 'FogExp': 0.000600000028498, 'SkyType': SKY_DUSK, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.35, 0.5, 0.62, 1), 'SeaColorShader': Vec4(0.25, 0.25, 0.15, 1)}, 'Night': {'Direction': Vec3(0, 40, 90), 'FrontColor': Vec4(0.3, 0.45, 0.58, 1), 'BackColor': Vec4(0.84, 1.02, 1.5, 1), 'AmbientColor': Vec4(0.43, 0.66, 0.92, 1), 'FogColor': Vec4(0.02, 0.04, 0.15, 0), 'FogExp': 0.00300000002608, 'SkyType': SKY_NIGHT, 'StarColor': Vec4(1, 1, 1, 0.25), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.15, 0.4, 0.45, 1), 'SeaColorShader': Vec4(0.1, 0.2, 0.15, 1)}, 'Stars': {'Direction': Vec3(0, 40, 20), 'FrontColor': Vec4(0.39, 0.49, 0.91, 1), 'BackColor': Vec4(0.78, 1, 1.22, 1), 'AmbientColor': Vec4(0.51, 0.58, 0.82, 1), 'FogColor': Vec4(0, 0, 0, 0), 'FogExp': 0.0010000000475, 'SkyType': SKY_STARS, 'StarColor': Vec4(1, 1, 1, 1), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.15, 0.35, 0.55, 1), 'SeaColorShader': Vec4(0.1, 0.15, 0.1, 1)}, 'Halloween': {'Direction': Vec3(0, 300, 70), 'FrontColor': Vec4(0.3, 0.2, 0.53, 1), 'BackColor': Vec4(0.42, 0.63, 0.38, 1), 'AmbientColor': Vec4(0.75, 0.82, 0.57, 1), 'FogColor': Vec4(0.08, 0.05, 0.11, 0), 'FogExp': 0.001200000057, 'SkyType': SKY_HALLOWEEN, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.4, 0.6, 0.6, 1), 'SeaColorShader': Vec4(0.1, 0.15, 0.1, 1)}, 'FullMoon': {'Direction': Vec3(0, 300, 110), 'FrontColor': Vec4(0.3, 0.2, 0.53, 1), 'BackColor': Vec4(0.48, 1.06, 0.76, 1), 'AmbientColor': Vec4(0.38, 0.65, 0.77, 1), 'FogColor': Vec4(0.11, 0.08, 0.14, 0), 'FogExp': 0.0, 'SkyType': SKY_HALLOWEEN, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.4, 0.6, 0.6, 1), 'SeaColorShader': Vec4(0.1, 0.15, 0.1, 1)}, 'HalfMoon': {'Direction': Vec3(0, 300, 110), 'FrontColor': Vec4(0.3, 0.2, 0.53, 1), 'BackColor': Vec4(0.385827, 0.346457, 0.267717, 1), 'AmbientColor': Vec4(0.66, 0.69, 0.99, 1), 'FogColor': Vec4(0.07, 0.05, 0.09, 0), 'FogExp': 0.00025, 'SkyType': SKY_HALLOWEEN, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 0.0, 'SeaColor': Vec4(0.4, 0.6, 0.6, 1), 'SeaColorShader': Vec4(0.1, 0.15, 0.1, 1)}, 'HalfMoon2': {'Direction': Vec3(0, 300, 110), 'FrontColor': Vec4(0.3, 0.2, 0.53, 1), 'BackColor': Vec4(0.57, 0.67, 0.4, 1), 'AmbientColor': Vec4(0.66, 0.76, 0.41, 1), 'FogColor': Vec4(0.08, 0.05, 0.09, 0), 'FogExp': 0.00025, 'SkyType': SKY_HALLOWEEN, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 0.0, 'SeaColor': Vec4(0.4, 0.6, 0.6, 1), 'SeaColorShader': Vec4(0.1, 0.15, 0.1, 1)}, 'Invasion': {'Direction': Vec3(0, 300, 110), 'FrontColor': Vec4(0.3, 0.24, 0.67, 1), 'BackColor': Vec4(0.74, 0.85, 0.52, 1), 'AmbientColor': Vec4(0.66, 0.76, 0.41, 1), 'FogColor': Vec4(0.1, 0.12, 0.03, 0), 'FogExp': 0.00025, 'SkyType': SKY_INVASION, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.5, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.4, 0.6, 0.6, 1), 'SeaColorShader': Vec4(0.1, 0.15, 0.1, 1)}}
ENV_SETTINGS_OPENSKY = {}
ENV_SETTINGS_NO_HOLIDAY = {}
ENV_SETTINGS_FOREST = {'BASE': {'FrontColor': Vec4(1.87, 1.51, 1.25, 1), 'BackColor': Vec4(0.34, 0.72, 0.42, 1), 'AmbientColor': Vec4(0.62, 0.78, 0.88, 1), 'FogColor': Vec4(0.21, 0.28, 0.22, 0), 'FogExp': 0.00179999996908}, 'Dawn': {'Direction': Vec3(0, 35, 210), 'FrontColor': Vec4(1.51, 1.5, 1.01, 1), 'BackColor': Vec4(0.29, 0.54, 0.39, 1), 'AmbientColor': Vec4(0.22, 0.35, 0.54, 1), 'FogColor': Vec4(0.27, 0.44, 0.45, 0), 'FogExp': 0.003, 'SkyType': SKY_DAWN}, 'Day': {'FrontColor': Vec4(2, 1.79, 1.68, 1), 'BackColor': Vec4(0.24, 0.49, 0.42, 1), 'AmbientColor': Vec4(0.67, 0.85, 0.91, 1), 'FogColor': Vec4(0.6, 0.7, 0.9, 0), 'FogExp': 0.000600000028498}, 'Dusk': {'Direction': Vec3(0, 35, 15), 'FrontColor': Vec4(1.73, 1.04, 0.93, 1), 'BackColor': Vec4(0.49, 0.66, 0.42, 1), 'AmbientColor': Vec4(0.38, 0.3, 0.44, 1), 'FogColor': Vec4(0.36, 0.29, 0.12, 0), 'FogExp': 0.002, 'SkyType': SKY_DUSK}, 'Night': {'Direction': Vec3(0, 40, 90), 'FrontColor': Vec4(0.26, 0.61, 0.48, 1), 'BackColor': Vec4(0.5, 0.92, 1.42, 1), 'AmbientColor': Vec4(0.37, 0.62, 0.68, 1), 'FogColor': Vec4(0, 0.07, 0.07, 0), 'FogExp': 0.00200000009499, 'SkyType': SKY_NIGHT}, 'Stars': {'Direction': Vec3(0, 40, 160), 'FrontColor': Vec4(0.26, 0.49, 0.56, 1), 'BackColor': Vec4(0.95, 0.95, 1.15, 1), 'AmbientColor': Vec4(0.25, 0.59, 0.59, 1), 'FogColor': Vec4(0, 0, 0, 0), 'FogExp': 0.00079999997979, 'SkyType': SKY_NIGHT}}
ENV_SETTINGS_SWAMP = {'BASE': {'FrontColor': Vec4(1.7, 1.7, 1.4, 1), 'BackColor': Vec4(0.6, 0.9, 1.5, 1), 'AmbientColor': Vec4(0.9, 0.9, 0.8, 1), 'FogColor': Vec4(0.2, 0.25, 0.3, 0), 'FogExp': 0.005, 'SkyType': SKY_SWAMP, 'StarColor': Vec4(1, 1, 1, 0)}, 'Dawn': {'Direction': Vec3(0, 35, 210), 'FrontColor': Vec4(1.79, 1.8, 1.25, 1), 'BackColor': Vec4(0.42, 0.66, 0.36, 1), 'AmbientColor': Vec4(0.78, 0.89, 0.89, 1), 'FogColor': Vec4(0.13, 0.29, 0.3, 0), 'FogExp': 0.008, 'FogLinearRange': (0.0, 250.0), 'SkyType': SKY_DUSK}, 'Day': {'FrontColor': Vec4(1.84, 1.85, 1.58, 1), 'BackColor': Vec4(0.57, 0.89, 0.62, 1), 'AmbientColor': Vec4(0.78, 0.89, 0.92, 1), 'FogColor': Vec4(0.29, 0.35, 0.38, 0), 'SkyType': SKY_DAY}, 'Dusk': {'Direction': Vec3(0, 35, 15), 'FrontColor': Vec4(1.76, 1.4, 1.31, 1), 'BackColor': Vec4(0.39, 0.53, 0.75, 1), 'AmbientColor': Vec4(0.85, 0.89, 0.8, 1), 'SkyType': SKY_DUSK}, 'Night': {'Direction': Vec3(0, 40, 90), 'FrontColor': Vec4(0.42, 0.57, 0.54, 1), 'BackColor': Vec4(0.94, 1.16, 1.51, 1), 'AmbientColor': Vec4(0.42, 0.71, 0.75, 1), 'FogColor': Vec4(0.11, 0.13, 0.18, 0), 'FogExp': 0.00499999988824, 'SkyType': SKY_NIGHT}, 'Stars': {'Direction': Vec3(0, 40, 160), 'FrontColor': Vec4(0.43, 0.5, 0.96, 1), 'BackColor': Vec4(1.04, 1.23, 1.7, 1), 'AmbientColor': Vec4(0.55, 0.83, 0.85, 1), 'FogColor': Vec4(0, 0, 0, 0), 'FogExp': 0.00300000002608, 'SkyType': SKY_STARS}}
ENV_SETTINGS_CAVE = {'BASE': {'Direction': Vec3(0, 0, 270), 'LightSwitch': [0, 1, 0], 'FrontColor': Vec4(0, 0, 0, 1), 'BackColor': Vec4(0, 0, 0, 1), 'AmbientColor': Vec4(0.25, 0.25, 0.25, 1), 'FogType': FOG_LINEAR, 'FogColor': Vec4(0.15, 0.15, 0.05, 0), 'FogExp': 0.002, 'FogLinearRange': (0.0, 400.0), 'SkyType': SKY_OFF, 'StarColor': Vec4(1, 1, 1, 0)}}
ENV_SETTINGS_INTERIOR = {'BASE': {'Direction': Vec3(0, 0, 270), 'LightSwitch': [0, 0, 0], 'FrontColor': Vec4(0, 0, 0, 1), 'BackColor': Vec4(0, 0, 0, 1), 'AmbientColor': Vec4(1, 0.25, 0.25, 1), 'FogType': FOG_OFF, 'FogColor': Vec4(0.25, 0.25, 0.25, 0), 'FogExp': 0.0001, 'FogLinearRange': (0.0, 100.0), 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.2, 0.2, 0.2, 1), 'SeaColorShader': Vec4(0.2, 0.2, 0.2, 1)}}
ENV_SETTINGS_SAILING = {'Dawn': {'FogColor': Vec4(0.29, 0.32, 0.44, 0), 'FogExp': 0.0015}, 'Day': {'FogColor': Vec4(0.6, 0.7, 0.9, 0), 'FogExp': 0.0009}, 'Dusk': {'FogExp': 0.0005}, 'Night': {'FrontColor': Vec4(0.3, 0.45, 0.58, 1), 'BackColor': Vec4(1.33, 1.5, 1.62, 1), 'AmbientColor': Vec4(0.19, 0.51, 0.87, 1), 'FogColor': Vec4(0.11, 0.18, 0.33, 0), 'FogExp': 0.001}, 'Stars': {'FrontColor': Vec4(0.39, 0.49, 0.91, 1), 'BackColor': Vec4(1.28, 1.39, 1.52, 1), 'AmbientColor': Vec4(0.42, 0.51, 0.79, 1), 'FogColor': Vec4(0.09, 0.09, 0.24, 0), 'FogExp': 0.001}}
ENV_SETTINGS_CLOUDY = {'BASE': {'FrontColor': Vec4(1.7, 1.7, 1.4, 1), 'BackColor': Vec4(0.6, 0.9, 1.5, 1), 'AmbientColor': Vec4(0.9, 0.9, 0.8, 1), 'FogColor': Vec4(0.2, 0.25, 0.3, 0), 'FogExp': 0.005, 'SkyType': SKY_SWAMP, 'StarColor': Vec4(1, 1, 1, 0)}}
ENV_SETTINGS_INVASION = {'BASE': {'Direction': Vec3(0, 300, 110), 'FrontColor': Vec4(0.3, 0.24, 0.67, 1), 'BackColor': Vec4(0.74, 0.85, 0.52, 1), 'AmbientColor': Vec4(0.66, 0.76, 0.41, 1), 'FogColor': Vec4(0.1, 0.12, 0.03, 0), 'FogExp': 0.00025, 'SkyType': SKY_INVASION, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.5, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.4, 0.6, 0.6, 1), 'SeaColorShader': Vec4(0.1, 0.15, 0.1, 1)}}
ENV_SETTINGS_SAINT_PATRICKS = {'BASE': {'SeaColor': Vec4(0.25, 0.9, 0.2, 1.0), 'SeaColorShader': Vec4(0.22, 0.56, 0.15, 1), 'SeaFactor': Vec3(0.4, 1.0, 0.3)}}
ENV_SETTINGS_VALENTINES = {'Day': {'FrontColor': Vec4(1.71, 1.36, 1.15, 1), 'BackColor': Vec4(0.59, 0.59, 0.88, 1), 'AmbientColor': Vec4(0.52, 0.39, 0.42, 1), 'FogColor': Vec4(0.46, 0.38, 0.43, 0), 'FogExp': 0.000600000028498, 'SkyType': SKY_DUSK, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.35, 0.5, 0.62, 1), 'SeaColorShader': Vec4(0.25, 0.25, 0.15, 1)}}
ENV_SETTINGS_HALLOWEEN = {'Dusk': {'FrontColor': Vec4(1.7, 1.7, 1.4, 1), 'BackColor': Vec4(0.6, 0.9, 1.5, 1), 'AmbientColor': Vec4(0.9, 0.9, 0.8, 1), 'FogColor': Vec4(0.2, 0.25, 0.3, 0), 'FogExp': 0.005, 'SkyType': SKY_OVERCAST, 'StarColor': Vec4(1, 1, 1, 0)}, 'Night': {'FrontColor': Vec4(0.3, 0.2, 0.53, 1), 'BackColor': Vec4(0.42, 0.63, 0.38, 1), 'AmbientColor': Vec4(0.75, 0.82, 0.57, 1), 'FogColor': Vec4(0.08, 0.05, 0.11, 0), 'FogExp': 0.001200000057, 'SkyType': SKY_HALLOWEEN, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.4, 0.6, 0.6, 1), 'SeaColorShader': Vec4(0.1, 0.15, 0.1, 1)}, 'Stars': {'FrontColor': Vec4(0.3, 0.2, 0.53, 1), 'BackColor': Vec4(0.42, 0.63, 0.38, 1), 'AmbientColor': Vec4(0.75, 0.82, 0.57, 1), 'FogColor': Vec4(0.08, 0.05, 0.11, 0), 'FogExp': 0.001200000057, 'SkyType': SKY_HALLOWEEN, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.4, 0.6, 0.6, 1), 'SeaColorShader': Vec4(0.1, 0.15, 0.1, 1)}}
ENV_SETTINGS_CURSED_NIGHT = {'Dawn': {'MoonPhase': 0.0}, 'Dusk': {'Direction': Vec3(0, 65, 90), 'SkyType': SKY_HALLOWEEN, 'FogColor': Vec4(0.08, 0.05, 0.11, 0), 'MoonPhase': 0.0, 'MoonSize': 1.4}, 'Night': {'Direction': Vec3(0, 65, 90), 'FrontColor': Vec4(0.3, 0.2, 0.53, 1), 'BackColor': Vec4(0.42, 0.63, 0.38, 1), 'AmbientColor': Vec4(0.75, 0.82, 0.57, 1), 'FogColor': Vec4(0.08, 0.05, 0.11, 0), 'FogExp': 0.001200000057, 'SkyType': SKY_HALLOWEEN, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.8, 'MoonOverlay': 0.0, 'MoonPhase': 0.0, 'SeaColor': Vec4(0.4, 0.6, 0.6, 1), 'SeaColorShader': Vec4(0.1, 0.15, 0.1, 1)}, 'Stars': {'Direction': Vec3(0, 65, 90), 'FrontColor': Vec4(0.3, 0.2, 0.53, 1), 'BackColor': Vec4(0.42, 0.63, 0.38, 1), 'AmbientColor': Vec4(0.75, 0.82, 0.57, 1), 'FogColor': Vec4(0.08, 0.05, 0.11, 0), 'FogExp': 0.001200000057, 'SkyType': SKY_HALLOWEEN, 'StarColor': Vec4(1, 1, 1, 0), 'MoonSize': 1.8, 'MoonOverlay': 0.0, 'MoonPhase': 0.0, 'SeaColor': Vec4(0.4, 0.6, 0.6, 1), 'SeaColorShader': Vec4(0.1, 0.15, 0.1, 1)}}
ENV_SETTINGS_EVER_NIGHT = {'BASE': {'Direction': Vec3(0, 40, 90), 'FrontColor': Vec4(0.3, 0.45, 0.58, 1), 'BackColor': Vec4(0.84, 1.02, 1.5, 1), 'AmbientColor': Vec4(0.43, 0.66, 0.92, 1), 'FogColor': Vec4(0.02, 0.04, 0.15, 0), 'FogExp': 0.00300000002608, 'SkyType': SKY_NIGHT, 'StarColor': Vec4(1, 1, 1, 0.25), 'MoonSize': 1.0, 'MoonOverlay': 0.0, 'MoonPhase': 1.0, 'SeaColor': Vec4(0.15, 0.4, 0.45, 1), 'SeaColorShader': Vec4(0.1, 0.2, 0.15, 1)}}
ENV_SETTINGS_CANNONGAME = {'Dawn': {'FogExp': 0.0009, 'Direction': Vec3(0, 30, 245), 'LightSwitch': [1, 1, 1]}, 'Night': {'FogExp': 9e-05, 'Direction': Vec3(0, 30, 245), 'LightSwitch': [1, 1, 1]}, 'Stars': {'FogExp': 9e-05, 'Direction': Vec3(0, 30, 245), 'LightSwitch': [1, 1, 1]}}