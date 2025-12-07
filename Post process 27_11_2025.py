import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.integrate as sp


SubDataFrame = []
for i in range(0, 298):

    if i == 253:
        debug = pd.DataFrame({'debug': [1]})
        SubDataFrame.append(debug)
        pass
    else :
        indice = str(i).zfill(3)
        nom_fichier = "DonneesVol_27_11_2025/REC_" + indice + ".csv"
        data = pd.read_csv(nom_fichier)
        SubDataFrame.append(data)

DataFrame = pd.concat(SubDataFrame, ignore_index=True)

"""
*******************************************************************************
*                           1. Affichage des deltaT                           *
*******************************************************************************
"""
# deltaT = []
# deltaTbig = []
# deltaTbigx = []
# deltaTx = []
# for i in range(1, len(DataFrame)):
#     val = DataFrame.iloc[i]['time_us']/10**6 - DataFrame.iloc[i-1]['time_us']/10**6
#     if val < 0.4:
#         deltaT.append(val)
#         deltaTx.append(i)
#     if val < 10:
#         deltaTbig.append(val)
#         deltaTbigx.append(i)

# Affichage des delta T
# plt.figure()
# plt.plot(deltaTx, deltaT)
# plt.title("Delta T Pour comprarer le système d'écriture des données")
# plt.xlabel("Nombre de mesures")
# plt.ylabel("Delta T (s)")
# plt.grid()

# Affichage des pic delta T
# plt.figure()
# plt.plot(deltaTbigx, deltaTbig, 'r')
# plt.title("Pic de Delta T Pour comprarer le système d'écriture des données")
# plt.xlabel("Nombre de mesures")
# plt.ylabel("Delta T (s)")
# plt.grid()
# plt.show()

"""
*******************************************************************************
*                          2. Affichage des gouvernes                         *
*******************************************************************************
"""
# AileronD = []
# t_aileronD = []
# AileronG = []
# t_aileronG = []
# Gaz = []
# t_gaz = []
# Profondeur = []
# t_profondeur = []
# Dérive = []
# t_dérive = []
# Orientation_moteur = []
# t_orientation_moteur = []
# fenetre = 500
# for j in range (1, 7):
#     for i in range(1, len(DataFrame)):
#         val = DataFrame.iloc[i][f'raw{j}']
#         if j == 1:
#             AileronD.append(val)
#             t_aileronD.append(DataFrame.iloc[i]['time_us']/10**6)
#         if j == 2:
#             AileronG.append(val)
#             t_aileronG.append(DataFrame.iloc[i]['time_us']/10**6)
#         if j == 3:
#             Gaz.append(val)
#             t_gaz.append(DataFrame.iloc[i]['time_us']/10**6)
#         if j == 4:
#             Profondeur.append(val)
#             t_profondeur.append(DataFrame.iloc[i]['time_us']/10**6)
#         if j == 5:
#             Dérive.append(val)
#             t_dérive.append(DataFrame.iloc[i]['time_us']/10**6)
#         if j == 6:
#             Orientation_moteur.append(val)
#             t_orientation_moteur.append(DataFrame.iloc[i]['time_us']/10**6)

#     if j == 1 and len(AileronD) > 0:
#         plt.subplot(2, 3, j)
#         plt.plot(t_aileronD, AileronD, alpha=0.3, color='gray', label='Brut')
#         lisse = pd.Series(AileronD).rolling(window=fenetre, min_periods=1).mean()
#         plt.plot(t_aileronD, lisse, color='blue', label='Lissé')
#         plt.title("Aileron Droit")
#         plt.xlabel("temps (s)")
#         plt.ylabel("Mouvement aileron droit")
#         plt.legend()
#         plt.grid()

#     if j == 2 and len(AileronG) > 0:
#         plt.subplot(2, 3, j)
#         plt.plot(t_aileronG, AileronG, alpha=0.3, color='gray', label='Brut')
#         lisse = pd.Series(AileronG).rolling(window=fenetre, min_periods=1).mean()
#         plt.plot(t_aileronG, lisse, color='orange', label='Lissé')
#         plt.title("Aileron Gauche")
#         plt.xlabel("temps (s)")
#         plt.ylabel("Mouvement aileron gauche")
#         plt.legend()
#         plt.grid() 

#     if j == 3 and len(Gaz) > 0:
#         plt.subplot(2, 3, j)
#         plt.plot(t_gaz, Gaz, alpha=0.3, color='gray', label='Brut')
#         lisse = pd.Series(Gaz).rolling(window=fenetre, min_periods=1).mean()
#         plt.plot(t_gaz, lisse, color='green', label='Lissé')
#         plt.title("Puissance des gaz")
#         plt.xlabel("temps (s)")
#         plt.ylabel("Puissance des gaz")
#         plt.legend()
#         plt.grid()

#     if j == 4 and len(Profondeur) > 0:
#         plt.subplot(2, 3, j)
#         plt.plot(t_profondeur, Profondeur, alpha=0.3, color='gray', label='Brut')
#         lisse = pd.Series(Profondeur).rolling(window=fenetre, min_periods=1).mean()
#         plt.plot(t_profondeur, lisse, color='red', label='Lissé')
#         plt.title("Gouverne de Profondeur")
#         plt.xlabel("temps (s)")
#         plt.ylabel("Mouvement profondeur")
#         plt.legend()
#         plt.grid()

#     if j == 5 and len(Dérive) > 0:
#         plt.subplot(2, 3, j)
#         plt.plot(t_dérive, Dérive, alpha=0.3, color='gray', label='Brut')
#         lisse = pd.Series(Dérive).rolling(window=fenetre, min_periods=1).mean()
#         plt.plot(t_dérive, lisse, color='purple', label='Lissé')
#         plt.title("Dérive")
#         plt.xlabel("temps (s)")
#         plt.ylabel("Mouvement dérive")
#         plt.legend()
#         plt.grid()

#     if j == 6 and len(Orientation_moteur) > 0:
#         plt.subplot(2, 3, j)
#         plt.plot(t_orientation_moteur, Orientation_moteur, alpha=0.3, color='gray', label='Brut')
#         lisse = pd.Series(Orientation_moteur).rolling(window=fenetre, min_periods=1).mean()
#         plt.plot(t_orientation_moteur, lisse, color='brown', label='Lissé')
#         plt.title("Orientation des moteurs")
#         plt.xlabel("temps (s)")
#         plt.ylabel("Mouvement moteurs")
#         plt.legend()
#         plt.grid()

# plt.tight_layout()
# plt.show()

"""
*******************************************************************************
*                          3. Affichage des altitudes                         *
*******************************************************************************
"""
Altitude_infrarouge = []
t_altitude_infrarouge = []
Altitude_ultrasons = []
t_altitude_ultrasons = []
fenetre = 200

for i in range(1, len(DataFrame)):
    val_infra = DataFrame.iloc[i]['vl53_mm']
    if val_infra == "nan":
        val_infra = -1
    else:
        Altitude_infrarouge.append(val_infra)
        t_altitude_infrarouge.append(DataFrame.iloc[i]['time_us']/10**6)
    
    val_ultra = DataFrame.iloc[i]['ultrason_mm']
    if val_ultra == "nan":
        val_ultra = -1
    else:
        Altitude_ultrasons.append(val_ultra)
        t_altitude_ultrasons.append(DataFrame.iloc[i]['time_us']/10**6)

plt.subplot(2, 1, 1)
plt.plot(t_altitude_infrarouge, Altitude_infrarouge, alpha=0.3, color='gray', label='Brut')
lisse = pd.Series(Altitude_infrarouge).rolling(window=fenetre, min_periods=1).mean()
plt.plot(t_altitude_infrarouge, lisse, color='orange', label='Lissé')
plt.axhline(173, alpha = 0.5, color='blue', linestyle='--', label='Altitude de décollage')
plt.axhline(153, alpha = 0.5, color='red', linestyle='--', label='Hauteur de référence')
plt.title("Altitude mesurée capteur infrarouge")
plt.ylim(0, 400)
plt.xlabel("temps (s)")
plt.ylabel("Altitude (mm)")
plt.legend()
plt.grid() 

plt.subplot(2, 1, 2)
plt.plot(t_altitude_ultrasons, Altitude_ultrasons, alpha=0.3, color='gray', label='Brut')
lisse = pd.Series(Altitude_ultrasons).rolling(window=fenetre, min_periods=1).mean()
plt.plot(t_altitude_ultrasons, lisse, color='magenta', label='Lissé')
plt.axhline(160, alpha = 0.5, color='blue', linestyle='--', label='Altitude de décollage')
plt.axhline(140, alpha = 0.5, color='red', linestyle='--', label='Hauteur de référence')
plt.title("Altitude mesurée capteur ultrasons")
plt.xlabel("temps (s)")
plt.ylim(0, 400)
plt.ylabel("Altitude (mm)")
plt.legend()
plt.grid() 
plt.tight_layout()
plt.show() 

"""
*******************************************************************************
*                         4. Affichage pitot + vitesse                        *
*******************************************************************************
"""
# Pitot = []
# t_pitot = []
# Vitesse = []
# t_vitesse = []
# fenetre = 200

# temps_debug = None 

# for i in range(1, len(DataFrame)):
#     val_pitot = DataFrame.iloc[i]['pitot_pa']
#     Pitot.append(val_pitot)
#     t_actuel = DataFrame.iloc[i]['time_us']/10**6 
#     t_pitot.append(t_actuel)
    
#     val_vitesse = DataFrame.iloc[i]['air_speed']
#     Vitesse.append(val_vitesse)
#     t_vitesse.append(t_actuel)

#     if DataFrame.iloc[i]['time_us'] == 1278488712:
#         temps_debug = t_actuel

# plt.subplot(2, 1, 1)
# plt.plot(t_pitot, Pitot, alpha=0.3, color='gray', label='Brut')
# lisse_pitot = pd.Series(Pitot).rolling(window=fenetre, min_periods=1).mean()
# plt.plot(t_pitot, lisse_pitot, color='orange', label='Lissé')

# if temps_debug is not None:
#     plt.axvline(x=temps_debug, color='red', linestyle='--', label='Debug Event')

# plt.title("Valeur de la sonde pitot")
# plt.xlabel("temps (s)")
# plt.ylabel("Pression (Pa)")
# plt.legend()
# plt.grid()

# plt.subplot(2, 1, 2)
# plt.plot(t_vitesse, Vitesse, alpha=0.3, color='gray', label='Brut')
# lisse_vitesse = pd.Series(Vitesse).rolling(window=fenetre, min_periods=1).mean()
# plt.plot(t_vitesse, lisse_vitesse, color='blue', label='Lissé')

# if temps_debug is not None:
#     plt.axvline(x=temps_debug, color='red', linestyle='--', label='Debug Event')

# plt.title("Vitesse mesurée")
# plt.xlabel("temps (s)")
# plt.ylabel("Vitesse (m/s)")
# plt.legend()
# plt.grid()

# plt.tight_layout()
# plt.show()

"""
*******************************************************************************
*                      5. Affichage accélération x, y et z                    *
*******************************************************************************
"""
# acc_x = []
# t_acc_x = []
# acc_y = []
# t_acc_y = []
# acc_z = []
# t_acc_z = []

# fenetre = 1000

# for i in range(1, len(DataFrame)):
#     val_acc_x = DataFrame.iloc[i]['accX']
#     acc_x.append(val_acc_x)
#     t_acc_x.append(DataFrame.iloc[i]['time_us']/10**6)
    
#     val_acc_y = DataFrame.iloc[i]['accY']
#     acc_y.append(val_acc_y)
#     t_acc_y.append(DataFrame.iloc[i]['time_us']/10**6)
    
#     val_acc_z = DataFrame.iloc[i]['accZ']
#     acc_z.append(val_acc_z)
#     t_acc_z.append(DataFrame.iloc[i]['time_us']/10**6)

# # plt.subplot(3, 1, 1)
# # plt.plot(t_acc_x, acc_x, alpha=0.3, color='gray', label='Brut')
# # lisse_x = pd.Series(acc_x).rolling(window=fenetre, min_periods=1).mean()
# # plt.plot(t_acc_x, lisse_x, color='orange', label='Lissé')
# # plt.title("Accélération en X")
# # plt.xlabel("temps (s)")
# # plt.ylabel("Accélération (mg)")
# # plt.legend()
# # plt.grid()

# # plt.subplot(3, 1, 2)
# # plt.plot(t_acc_y, acc_y, alpha=0.3, color='gray', label='Brut')
# # lisse_y = pd.Series(acc_y).rolling(window=fenetre, min_periods=1).mean()
# # plt.plot(t_acc_y, lisse_y, color='blue', label='Lissé')
# # plt.title("Accélération en Y")
# # plt.xlabel("temps (s)")
# # plt.ylabel("Accélération (mg)")
# # plt.legend()
# # plt.grid()

# # plt.subplot(3, 1, 3)
# # plt.plot(t_acc_z, acc_z, alpha=0.3, color='gray', label='Brut')
# # lisse_z = pd.Series(acc_z).rolling(window=fenetre, min_periods=1).mean()
# # plt.plot(t_acc_z, lisse_z, color='green', label='Lissé')
# # plt.title("Accélération en Z")
# # plt.xlabel("temps (s)")
# # plt.ylabel("Accélération (mg)")
# # plt.legend()
# # plt.grid()

# # plt.tight_layout()
# # plt.show()

"""
*******************************************************************************
*                6. Affichage accélération gyroX, gyroY et gyroZ              *
*******************************************************************************
"""
# gyro_x = []
# t_gyro_x = []
# gyro_y = []
# t_gyro_y = []
# gyro_z = []
# t_gyro_z = []

# fenetre = 50

# for i in range(1, len(DataFrame)):
#     val_gyro_x = DataFrame.iloc[i]['gyroX']
#     gyro_x.append(val_gyro_x)
#     t_gyro_x.append(DataFrame.iloc[i]['time_us']/10**6)
    
#     val_gyro_y = DataFrame.iloc[i]['gyroY']
#     gyro_y.append(val_gyro_y)
#     t_gyro_y.append(DataFrame.iloc[i]['time_us']/10**6)
    
#     val_gyro_z = DataFrame.iloc[i]['gyroZ']
#     gyro_z.append(val_gyro_z)
#     t_gyro_z.append(DataFrame.iloc[i]['time_us']/10**6)

# plt.subplot(3, 1, 1)
# plt.plot(t_gyro_x, gyro_x, alpha=0.3, color='gray', label='Brut')
# lisse_x = pd.Series(gyro_x).rolling(window=fenetre, min_periods=1).mean()
# plt.plot(t_gyro_x, lisse_x, color='orange', label='Lissé')
# plt.title("Gyroscope en X")
# plt.xlabel("temps (s)")
# plt.ylabel("Vitesse angulaire (mdps)")
# plt.legend()
# plt.grid()

# plt.subplot(3, 1, 2)
# plt.plot(t_gyro_y, gyro_y, alpha=0.3, color='gray', label='Brut')
# lisse_y = pd.Series(gyro_y).rolling(window=fenetre, min_periods=1).mean()
# plt.plot(t_gyro_y, lisse_y, color='blue', label='Lissé')
# plt.title("Gyroscope en Y")
# plt.xlabel("temps (s)")
# plt.ylabel("Vitesse angulaire (mdps)")
# plt.legend()
# plt.grid()

# plt.subplot(3, 1, 3)
# plt.plot(t_gyro_z, gyro_z, alpha=0.3, color='gray', label='Brut')
# lisse_z = pd.Series(gyro_z).rolling(window=fenetre, min_periods=1).mean()
# plt.plot(t_gyro_z, lisse_z, color='green', label='Lissé')
# plt.title("Gyroscope en Z")
# plt.xlabel("temps (s)")
# plt.ylabel("Vitesse angulaire (mdps)")
# plt.legend()
# plt.grid()

# plt.tight_layout()
# plt.show()

"""
*******************************************************************************
*                   7. Affichage accélération roll, pitch, yaw                *
*******************************************************************************
"""
# roll = []
# t_roll = []
# pitch = []
# t_pitch = []
# yaw = []
# t_yaw = []

# fenetre = 50

# for i in range(1, len(DataFrame)):
#     val_roll = DataFrame.iloc[i]['roll']
#     roll.append(val_roll)
#     t_roll.append(DataFrame.iloc[i]['time_us']/10**6)
    
#     val_pitch = DataFrame.iloc[i]['pitch']
#     pitch.append(val_pitch)
#     t_pitch.append(DataFrame.iloc[i]['time_us']/10**6)
    
#     val_yaw = DataFrame.iloc[i]['yaw']
#     yaw.append(val_yaw)
#     t_yaw.append(DataFrame.iloc[i]['time_us']/10**6)

# plt.subplot(3, 1, 1)
# plt.plot(t_roll, roll, alpha=0.3, color='gray', label='Brut')
# lisse_roll = pd.Series(roll).rolling(window=fenetre, min_periods=1).mean()
# plt.plot(t_roll, lisse_roll, color='orange', label='Lissé')
# plt.title("Angle de roulis")
# plt.xlabel("temps (s)")
# plt.ylabel("Angle (°)")
# plt.legend()
# plt.grid()

# plt.subplot(3, 1, 2)
# plt.plot(t_pitch, pitch, alpha=0.3, color='gray', label='Brut')
# lisse_pitch = pd.Series(pitch).rolling(window=fenetre, min_periods=1).mean()
# plt.plot(t_pitch, lisse_pitch, color='blue', label='Lissé')
# plt.title("Angle de tangage")
# plt.xlabel("temps (s)")
# plt.ylabel("Angle (°)")
# plt.legend()
# plt.grid()

# plt.subplot(3, 1, 3)
# plt.plot(t_yaw, yaw, alpha=0.3, color='gray', label='Brut')
# lisse_yaw = pd.Series(yaw).rolling(window=fenetre, min_periods=1).mean()
# plt.plot(t_yaw, lisse_yaw, color='green', label='Lissé')
# plt.title("Angle de lacet")
# plt.xlabel("temps (s)")
# plt.ylabel("Angle (°)")
# plt.legend()
# plt.grid()

# plt.tight_layout()
# plt.show()