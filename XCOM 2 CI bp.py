import os
import fnmatch

os.chdir("C:/Users/manoh/PycharmProjects/untitled/src/")
# os.chdir("Q:/SteamLibrary/steamapps/workshop/content/268500/1468263798/Localization/")

tier2_weaponBlueprint = 'Requirements=(RequiredTechs[0]="MagnetizedWeapons", RequiredEngineeringScore=10, bVisibleIfPersonnelGatesNotMet=true) \r Cost=(ResourceCosts[0]=(ItemTemplateName="Supplies", Quantity=18), ResourceCosts[1]=(ItemTemplateName="AlienAlloy", Quantity=3))'
tier3_weaponBlueprint = 'Requirements=(RequiredTechs[0]="PlasmaRifle", RequiredEngineeringScore=20, bVisibleIfPersonnelGatesNotMet=true) \r Cost=(ResourceCosts[0]=(ItemTemplateName="Supplies", Quantity=43), ResourceCosts[1]=(ItemTemplateName="AlienAlloy", Quantity=5), ResourceCosts[2]=(ItemTemplateName="EleriumDust", Quantity=3))'
buildable = '+arrMakeItemBuildable="{}"'
killable = '+arrKillItems="{}"'

weapon_blueprints = open("weaponBlueprints.ini", "w+")
for root, dirs, files in os.walk("C:/Users/manoh/PycharmProjects/untitled/src/"):
    for file in files:
        if fnmatch.fnmatch(file, "*.int"):
            print("ROOT: ", root, "\nDIRS: ", dirs, "\nFILE:", file)
            # abs_file_path = os.path.abspath(file)
            file_path = root + "/" + file
            with open(file_path, "r", encoding="utf-8", errors="ignore") as openfile:
                for line in openfile:
                    if line.find("X2WeaponTemplate") > 0 and (line.find("_T2") > 0 or line.find("_MG") or line.find("magnetic")) > 0:
                        weapon_blueprints.write(
                            "[" + line[1:line.find("X2WeaponTemplate")] + " X2WeaponTemplate]" + "\r" + tier2_weaponBlueprint + "\n")
                    elif line.find("X2WeaponTemplate") > 0 and (line.find("_T3") > 0 or line.find("_NM") or line.find("beam") > 0):
                        weapon_blueprints.write(
                            "[" + line[1:line.find("X2WeaponTemplate")] + " X2WeaponTemplate]" + "\r" + tier3_weaponBlueprint + "\n")
                    else:
                        pass
    else:
        pass
weapon_blueprints.close( )

strategy_tuning = open("strategyTuning.ini", "w+")
for root, dirs, files in os.walk("C:/Users/manoh/PycharmProjects/untitled/src/"):
    for file in files:
        if fnmatch.fnmatch(file, "*.int"):
            print("ROOT: ", root, "\nDIRS: ", dirs, "\nFILE:", file)
            # abs_file_path = os.path.abspath(file)
            file_path = root + "/" + file
            with open(file_path, "r", encoding="utf-8", errors="ignore") as openfile:
                for line in openfile:
                    currentItemName = line[1:(line.find("X2WeaponTemplate") - 1)]
                    if line.find("X2WeaponTemplate") > 0 and (line.find("_T2") > 0 or line.find("_MG") or line.find("magnetic")) > 0:
                        strategy_tuning.write(
                            buildable.format(currentItemName) + "\n" + killable.format(currentItemName) + "\n")
                    elif line.find("X2WeaponTemplate") > 0 and (line.find("_T3") > 0 or line.find("_NM") or line.find("beam")) > 0:
                        strategy_tuning.write(
                            buildable.format(currentItemName) + "\n" + killable.format(currentItemName) + "\n")
                    else:
                        pass
strategy_tuning.close()

infiltration_tuning = open("infiltrationTuning.ini", "w+")
for root, dirs, files in os.walk("C:/Users/manoh/PycharmProjects/untitled/src/"):
    for file in files:
        if fnmatch.fnmatch(file, "*.int"):
            print("ROOT: ", root, "\nDIRS: ", dirs, "\nFILE:", file)
            # abs_file_path = os.path.abspath(file)
            file_path = root + "/" + file
            with open(file_path, "r", encoding="utf-8", errors="ignore") as openfile:

                smg_cv = '+InfilModifiers=(Item="{}", HoursAdded=8,  RiskReductionPercent=1)'
                smg_mg = '+InfilModifiers=(Item="{}", HoursAdded=8,  RiskReductionPercent=3)'
                smg_bm = '+InfilModifiers=(Item="{}", HoursAdded=8,  RiskReductionPercent=4)'
                pistol = '+InfilModifiers=(Item="{}", HoursAdded=2)'
                sword = '+InfilModifiers=(Item="{}", HoursAdded=3)'
                launcher = '+InfilModifiers=(Item"{}", HoursAdded=10)'
                assault_rifle_cv = '+InfilModifiers=(Item="{}", HoursAdded=12,  RiskReductionPercent=2)'
                assault_rifle_mg = '+InfilModifiers=(Item="{}", HoursAdded=12,  RiskReductionPercent=4)'
                assault_rifle_bm = '+InfilModifiers=(Item="{}", HoursAdded=12,  RiskReductionPercent=6)'
                shotgun_cv = '+InfilModifiers=(Item="{}", HoursAdded=10,  RiskReductionPercent=2)'
                shotgun_mg = '+InfilModifiers=(Item="{}", HoursAdded=10,  RiskReductionPercent=4)'
                shotgun_bm = '+InfilModifiers=(Item="{}", HoursAdded=10,  RiskReductionPercent=6)'
                sniper_cv = '+InfilModifiers=(Item="{}", HoursAdded=14,  RiskReductionPercent=3)'
                sniper_mg = '+InfilModifiers=(Item="{}", HoursAdded=14,  RiskReductionPercent=5)'
                sniper_bm = '+InfilModifiers=(Item="{}", HoursAdded=14,  RiskReductionPercent=7)'
                cannon_cv = '+InfilModifiers=(Item="{}", HoursAdded=16,  RiskReductionPercent=3)'
                cannon_mg = '+InfilModifiers=(Item="{}", HoursAdded=16,  RiskReductionPercent=5)'
                cannon_bm = '+InfilModifiers=(Item="{}", HoursAdded=16,  RiskReductionPercent=7)'
                bullpup_cv = '+InfilModifiers=(Item="{}", HoursAdded=10,  RiskReductionPercent=1)'
                bullpup_mg = '+InfilModifiers=(Item="{}", HoursAdded=10,  RiskReductionPercent=3)'
                bullpup_bm = '+InfilModifiers=(Item="{}", HoursAdded=10,  RiskReductionPercent=5)'
                vektor_cv = '+InfilModifiers=(Item="{}", HoursAdded=12,  RiskReductionPercent=1)'
                vektor_mg = '+InfilModifiers=(Item="{}", HoursAdded=12,  RiskReductionPercent=3)'
                vektor_bm = '+InfilModifiers=(Item="{}", HoursAdded=12,  RiskReductionPercent=5)'

                for line in openfile:
                    currentItemName = line[1:(line.find("X2WeaponTemplate") - 1)]
                    if line.find("X2WeaponTemplate") > 0 and (line.find("_T1") > 0 or line.find("_CV") or line.find("conventional") > 0) or (line.find("_T2") > 0 or line.find("_MG") > 0) or (line.find("_T3") > 0 or line.find("_BM") > 0):
                        print('The current item is: ' + currentItemName + '.\nWhat type of weapon is this?\nCategories include: Launcher (L), Vektor Rifle (VK), Bullpup (BP), '
                                                                          'Sword (SW), SMG, Pistol (P), Assault Rifle (AR), Sniper (SR), Shotgun (SG), Heavy Weapon (H), Other (O).')
                        weapon_type = input( )
                        if weapon_type == 'SMG' and (line.find("_T1") > 0 or line.find("_CV") or line.find("conventional") or line.find("conventional") > 0):
                            infiltration_tuning.write(smg_cv.format(currentItemName) + "\n")
                        elif weapon_type == 'SMG' and (line.find("_T2") > 0 or line.find("_MG") or line.find("magnetic") > 0):
                            infiltration_tuning.write(smg_mg.format(currentItemName) + "\n")
                        elif weapon_type == 'SMG' and (line.find("_T3") > 0 or line.find("_BM") or line.find("beam") > 0):
                            infiltration_tuning.write(smg_bm.format(currentItemName) + "\n")
                        elif weapon_type == 'P':
                            infiltration_tuning.write(pistol.format(currentItemName) + "\n")
                        elif weapon_type == 'AR' and (line.find("_T1") > 0 or line.find("_CV") or line.find("conventional") > 0):
                            infiltration_tuning.write(assault_rifle_cv.format(currentItemName) + "\n")
                        elif weapon_type == 'AR' and (line.find("_T2") > 0 or line.find("_MG") or line.find("magnetic") > 0):
                            infiltration_tuning.write(assault_rifle_mg.format(currentItemName) + "\n")
                        elif weapon_type == 'AR' and (line.find("_T3") > 0 or line.find("_BM") or line.find("beam") > 0):
                            infiltration_tuning.write(assault_rifle_bm.format(currentItemName) + "\n")
                        elif weapon_type == 'SR' and (line.find("_T1") > 0 or line.find("_CV") or line.find("conventional") > 0):
                            infiltration_tuning.write(sniper_cv.format(currentItemName) + "\n")
                        elif weapon_type == 'SR' and (line.find("_T2") > 0 or line.find("_MG") or line.find("magnetic") > 0):
                            infiltration_tuning.write(sniper_mg.format(currentItemName) + "\n")
                        elif weapon_type == 'SR' and (line.find("_T3") > 0 or line.find("_BM") or line.find("beam") > 0):
                            infiltration_tuning.write(sniper_bm.format(currentItemName) + "\n")
                        elif weapon_type == 'SG' and (line.find("_T1") > 0 or line.find("_CV") or line.find("conventional") > 0):
                            infiltration_tuning.write(shotgun_cv.format(currentItemName) + "\n")
                        elif weapon_type == 'SG' and (line.find("_T2") > 0 or line.find("_MG") or line.find("magnetic") > 0):
                            infiltration_tuning.write(shotgun_mg.format(currentItemName) + "\n")
                        elif weapon_type == 'SG' and (line.find("_T3") > 0 or line.find("_BM") or line.find("beam") > 0):
                            infiltration_tuning.write(shotgun_bm.format(currentItemName) + "\n")
                        elif weapon_type == 'SW':
                            infiltration_tuning.write(sword.format(currentItemName) + "\n")
                        elif weapon_type == 'H' and (line.find("_T1") > 0 or line.find("_CV") or line.find("conventional") > 0):
                            infiltration_tuning.write(cannon_cv.format(currentItemName) + "\n")
                        elif weapon_type == 'H' and (line.find("_T2") > 0 or line.find("_MG") or line.find("magnetic") > 0):
                            infiltration_tuning.write(cannon_mg.format(currentItemName) + "\n")
                        elif weapon_type == 'H' and (line.find("_T3") > 0 or line.find("_BM") or line.find("beam") > 0):
                            infiltration_tuning.write(cannon_bm.format(currentItemName) + "\n")
                        elif weapon_type == 'BP' and (line.find("_T1") > 0 or line.find("_CV") or line.find("conventional") > 0):
                            infiltration_tuning.write(bullpup_cv.format(currentItemName) + "\n")
                        elif weapon_type == 'BP' and (line.find("_T2") > 0 or line.find("_MG") or line.find("magnetic") > 0):
                            infiltration_tuning.write(bullpup_mg.format(currentItemName) + "\n")
                        elif weapon_type == 'BP' and (line.find("_T3") > 0 or line.find("_BM") or line.find("beam") > 0):
                            infiltration_tuning.write(bullpup_bm.format(currentItemName) + "\n")
                        elif weapon_type == 'VK' and (line.find("_T1") > 0 or line.find("_CV") or line.find("conventional") > 0):
                            infiltration_tuning.write(vektor_cv.format(currentItemName) + "\n")
                        elif weapon_type == 'VK' and (line.find("_T2") > 0 or line.find("_MG") or line.find("magnetic") > 0):
                            infiltration_tuning.write(vektor_mg.format(currentItemName) + "\n")
                        elif weapon_type == 'VK' and (line.find("_T3") > 0 or line.find("_BM") or line.find("beam") > 0):
                            infiltration_tuning.write(vektor_bm.format(currentItemName) + "\n")
                        elif weapon_type == 'L' and (line.find("_T1") > 0 or line.find("_CV") or line.find("conventional") > 0):
                            infiltration_tuning.write(launcher.format(currentItemName) + "\n")
                        elif weapon_type == 'L' and (line.find("_T2") > 0 or line.find("_MG") or line.find("magnetic") > 0):
                            infiltration_tuning.write(launcher.format(currentItemName) + "\n")
                        elif weapon_type == 'L' and (line.find("_T3") > 0 or line.find("_BM") or line.find("beam") > 0):
                            infiltration_tuning.write(launcher.format(currentItemName) + "\n")
                        elif weapon_type == 'O':
                            pass
                        elif weapon_type == 'end':
                            infiltration_tuning.close()
                            break
                    else:
                        pass


infiltration_tuning.close()
#or (line.find("_T2") > 0 or line.find("_MG") or line.find("magnetic")) or (line.find("_T3") > 0 or line.find("_NM") or line.find("beam")):