if __name__ == "__main__":
    final_list = []
    entry = ''
    ind_list = []
    singles = []

    node_names = input("Enter the node names as comma separate values: ")
    try:
        node_list = node_names.split(",")
    except IndexError:
        print("Provide a comma separated list of values")
    else:
        if node_list[0] != '':
            while len(node_list) > 0:
                singles = []
                common = node_list[0].split("n")[0] + "n"
                new_list = [item for item in node_list if (item.split("n")[0] + "n") == common]
                if len(new_list) > 0:
                    new_list.sort(key=lambda x: x.split("n")[1])
                    ind_list = new_list.copy()
                    while len(new_list) > 1:
                        entry = None
                        first_number = new_list[0][new_list[0].index('n') + 1:]
                        prev_number = first_number
                        k = 1
                        entry_deleted = False
                        while k < len(new_list):
                            next_number = new_list[k][new_list[k].index('n') + 1:]
                            if int(next_number) == int(prev_number) + 1:
                                entry = common + f"[{first_number}-{next_number}]"
                                prev_number = next_number
                            else:
                                if entry is not None:
                                    final_list.append(entry)
                                else:
                                    singles.append(first_number)
                                del new_list[:k]
                                entry_deleted = True
                            k = k + 1
                        if not entry_deleted:
                            final_list.append(entry)
                            del new_list[:k]
                    if len(new_list) == 1:
                        singles.append(new_list[0][new_list[0].index('n') + 1:])
                    if singles:
                        print(singles)
                        final = f"{common}["
                        for item in singles:
                            final = final + item + ","
                        final = list(final)
                        final[-1] = ']'
                        final = "".join(final)
                        final_list.append(final)
                node_list = [item for item in node_list if item not in ind_list]
                singles = []
            print(final_list)
