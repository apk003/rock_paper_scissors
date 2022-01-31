def player(prev_play, opponent_history=[], player_history=[]):
  win_set = {'R':'P', 'P':'S', 'S':'R'}

  if prev_play == '':
    guess = "R"
    player_history.append(guess)
    return guess

  else:
    opponent_history.append(prev_play)

    model = {"RR":{"R":0,"P":0,"S":0},
             "RP":{"R":0,"P":0,"S":0},
             "RS":{"R":0,"P":0,"S":0},
             "PR":{"R":0,"P":0,"S":0},
             "PP":{"R":0,"P":0,"S":0},
             "PS":{"R":0,"P":0,"S":0},
             "SR":{"R":0,"P":0,"S":0},
             "SP":{"R":0,"P":0,"S":0},
             "SS":{"R":0,"P":0,"S":0},         
            }

    hist_len = -1*min([len(opponent_history),25])

    for (i,move) in enumerate(opponent_history[hist_len:-1]):

      state=move+player_history[i+hist_len]
      opponent_next_move=opponent_history[i+1+hist_len]
      model[state][opponent_next_move]+=1

    state=prev_play+player_history[-1]
    prediction=max(model[state],key=model[state].get)
    guess = win_set[prediction]

    player_history.append(guess)
    return guess
