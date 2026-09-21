```python
# ... (previous code)

REWARD_TYPES = [
    "CALIBRATION",
    "AMMO",
    "WEAPON"
]

REWARD_CHOICES = [
    "CALIBRATION",
    "AMMO",
    "WEAPON"
]

def SelectRewards(seed, profile, previous_choices):
    current_choices = []
    for reward in REWARD_CHOICES:
        if reward not in previous_choices:
            current_choices.append(reward)
    return current_choices

def ApplyCalibration():
    current_weapon = GetEquippedWeapon()
    current_weapon.damage_multiplier *= 1.1
    current_weapon.is_calibrated = True
    AddHUDString("Weapon is calibrated.")

def GetEquippedWeapon():
    # Returns the currently equipped weapon
    pass

def DamageCalculation():
    current_weapon = GetEquippedWeapon()
    if current_weapon.is_calibrated:
        damage *= current_weapon.damage_multiplier
    return damage

# ... (remaining code)
```