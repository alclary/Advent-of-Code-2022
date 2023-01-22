def decrypt_elf_code_p1(file_name):
    score_key = {'X':1,'A':1,'Y':2,'B':2,'Z':3,'C':3,'win':6,'draw':3,'loss':0}
    player_score = 0

    with open(file_name, 'r') as infile:
        for line in infile:
            line_split = line.strip().split(' ')
            elf_cast = line_split[0]
            player_cast = line_split[1]

            cast_points = score_key[player_cast]
            outcome_points = score_key[player_outcome(score_key[elf_cast], score_key[player_cast])]

            player_score += cast_points + outcome_points

    return player_score

def player_outcome(elf_cast, player_cast):
    if elf_cast == player_cast:
        return 'draw'
    elif player_cast == 1 and elf_cast == 2 or \
        (player_cast == 2 and elf_cast == 3) or \
        (player_cast == 3 and elf_cast == 1):
        return 'loss'
    else:
        return 'win'

def decrypt_elf_code_p2(file_name):
    score_key = {'X':1,'A':1,'Y':2,'B':2,'Z':3,'C':3,'win':6,'draw':3,'loss':0}
    translate_outcome = {'X':'loss','Y':'draw','Z':'win'}
    player_score = 0

    with open(file_name, 'r') as infile:
        for line in infile:
            line_split = line.strip().split(' ')
            elf_cast = line_split[0]
            needed_outcome = line_split[1]
            translated_outcome = translate_outcome[needed_outcome]

            player_cast = determine_player_cast(elf_cast, translated_outcome)

            cast_points = score_key[player_cast]
            outcome_points = score_key[translated_outcome]

            player_score += cast_points + outcome_points

    return player_score

def determine_player_cast(elf_cast, needed_outcome):
    equivalents = {'A':'X','B':'Y','C':'Z'}
    win_equivalents = {'A':'Y','B':'Z','C':'X'}
    loss_equivalents = {'A':'Z','B':'X','C':'Y'}
    if needed_outcome == 'draw':
        return equivalents[elf_cast]
    elif needed_outcome == 'loss':
        return loss_equivalents[elf_cast]
    else:
        return win_equivalents[elf_cast]

if __name__ == '__main__':
  player_score_p1 = decrypt_elf_code_p1('input\d2_input.txt')
  print(player_score_p1)
  player_score_p2 = decrypt_elf_code_p2('input\d2_input.txt')
  print(player_score_p2)
