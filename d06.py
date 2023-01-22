def character_markers(file_name, detection_size):

    marker_indices = []

    # get and strip line from file
    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip()

    # start queue equals first x elements (detection size)
    queue = list(line[0:detection_size])
    if len(set(queue)) == detection_size:
        print(queue)    # detect if first queue contains all unique

    # proceed through line, keeping a constant queue of detection_size
    #   if queue containing all unique chars occurs, note marker indices
    #   (i.e. last added index)
    for i in range(detection_size, len(line)-1):
        queue.append(line[i])
        del queue[0]
        if len(set(queue)) == detection_size:
            marker_indices.append(i)

    return marker_indices

if __name__ == '__main__':
  print("Numbers as indices (x+1 processed prior to identification of a marker):")
  print(character_markers('input\d6_input.txt', 4)[0])
  print(character_markers('input\d6_input.txt', 14)[0])
