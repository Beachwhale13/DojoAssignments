my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}

def making_tuples():
    tuple_array = [];
    for key, value in my_dict.items():
        pair = (key, value)
        tuple_array.append(pair)
    print tuple_array

making_tuples()
