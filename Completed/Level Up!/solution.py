def xp_to_target_lvl(current_xp: int = -1, target_lvl: int = -1):
    if (not isinstance(current_xp, int) or not isinstance(target_lvl, int)
            or current_xp < 0 or target_lvl < 1 or target_lvl > 170):
        return 'Input is invalid.'
    total_required_xp = 0
    level_required_xp = 0
    for i in range(2, target_lvl + 1):
        if i == 2:
            level_required_xp = 314
        else:
            level_required_xp += int(level_required_xp * (0.25 - 0.01 * ((i - 1) // 10)))
        total_required_xp += level_required_xp
    if current_xp < total_required_xp:
        return total_required_xp - current_xp
    elif current_xp >= total_required_xp:
        return f'You have already reached level {target_lvl}.'
