def multi_tap(keys, times):
    keypad_dict = {0: [' '],
                   2: ['A', 'B', 'C'],
                   3: ['D', 'E', 'F'],
                   4: ['G', 'H', 'I'],
                   5: ['J', 'K', 'L'],
                   6: ['M', 'N', 'O'],
                   7: ['P', 'Q', 'R', 'S'],
                   8: ['T', 'U', 'V'],
                   9: ['W', 'X', 'Y', 'Z']
                   }
    previous_time = None

    for index, (key, time) in enumerate(zip(keys, times)):
        if previous_time is not None:
            time_difference = abs(time - previous_time)
            if time_difference > .5:
                print(f"Index-0.5: {index}, Key: {key}, Time: {time}, Time Difference: {time_difference}")
            else:
                print(f"Index: {index}, Key: {key}, Time: {time}, Time Difference: {time_difference}")
        else:
            print(f"Index: {index}, Key: {key}, Time: {time}")
        previous_time = time
    print(previous_time)

    # output = []
    # for i in range(len(keys)):
    #     key = keys[i]
    #     time = times[i]
    #     time_index = 0
    #     if key in keypad_dict:
    #         if i > 0 and (time - times[i - 1]) > 0.5:
    #             time_index += 1
    #             output.append(keypad_dict[key][times.index(time)])
    #             print("sddsdadasd", times.index(time))
    #         else:
    #             print("nnoo")
    #             output.append(keypad_dict[key][time_index])
    # print(output)


if __name__ == "__main__":
    # keys = [7, 7, 7]
    # times = [0.1, 0.8, 0.9]
    # output = PRO
    keys = [7, 7, 7, 7, 6, 6, 6]
    times = [0, 0.7, 0.8, 0.9, 1, 1.1, 1.2]
    multi_tap(keys, times)
