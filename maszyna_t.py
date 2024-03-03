class Touringmachine:
    def __init__(self, Tfile):
        f = open(Tfile)
        self.Alphabet = list(f.readline()[:-1])
        self.Mailinput = list(f.readline()[:-1])
        print(self.Mailinput)
        self.Marker = f.readline()[:-1]
        self.Start_state = f.readline()[:-1]
        self.End_states = dict()
        self.Graph_states = dict()

        #CZYTANIE WSZYTSKIEGO
        while True:
            Line = f.readline()
            if not Line:
                break
            else:
                if Line[0:6] == "koniec":
                    end_index, number_of_end_states = Line[:-1].split(" : ")
                    self.num_of_end_states = int(number_of_end_states)
                    for i in range(int(number_of_end_states)):
                        Line = f.readline()[:-1]
                        End_state_name, move, result = Line.split(" : ")
                        self.End_states[End_state_name] = [move, result]
                        #print(End_state_name, move, result)
                    Line = f.readline()[:-1]
                if Line[0:4] == "graf":
                    graph_index, number_of_graph_states = Line[:-1].split(" : ")
                    self.num_of_graph_states = int(number_of_graph_states)
                    for i in range(int(number_of_graph_states) - int(number_of_end_states)):
                        Line = f.readline()[:-2]
                        Graph_state_name = Line
                        self.Graph_states[Graph_state_name] = list()
                        for i in range(len(self.Alphabet)):
                            Line = f.readline()[:-1]
                            letter, action, write_letter, move, next_state = Line.split(" : ")
                            self.Graph_states[Graph_state_name].append({letter : [action, write_letter, move, next_state]})
                        Line = f.readline()

        #print(self.Graph_states)
        #print(self.End_states)
        f.close()

    
    def Start(self):
        self.Current_state=self.Graph_states[self.Start_state]
        self.Current_number=0

        if self.Mailinput[0] == self.Marker:
            print("Obecna pozycja: " + str(self.Current_number) + " - Marker na właściwym miejscu.")
            self.Current_number += 1
        else:
            print("cos jest nie tak gagadku!")
            return 0

        while self.Mailinput[self.Current_number] != 0:       
            self.instruct=list()
#            for i in range(len(self.Alphabet)):
#                if self.Mailinput[self.Current_number] == list(self.Current_state[i].keys())[0]:

            self.instruct=self.Current_state[self.Alphabet.index(self.Mailinput[self.Current_number])][self.Mailinput[self.Current_number]]
                

            if self.instruct[0] == "napisz":
                self.Mailinput[self.Current_number] = self.instruct[1]    
            else:
                continue
            print("Obecna pozycja: "+ str(self.Current_number))

            if self.instruct[2] == "P":
                self.Current_number += 1
            if self.instruct[2] == "L":
                self.Current_number -= 1

            self.Current_state = self.instruct[3]

            if self.Current_state in self.End_states:
                print(self.End_states[self.Current_state][1])
                print(self.Mailinput)
                break
            else:
                self.Current_state = self.Graph_states[self.Current_state]

            #print(self.Current_number)
            print("Instrukcja na obecny krok: " + str(self.instruct))
            print(str(self.Mailinput))


if __name__ == "__main__":
    print("Mail: ")
    T1 = Touringmachine("turing.txt")
    T1.Start()
    print("Palindrom: ")
    T2 = Touringmachine("palindrom.txt")
    T2.Start()
    
    '''
    #LISTA ALFABETU:
    Alphabet = []
    End_states = dict()
    Graph_states = dict()

    f = open("turing.txt")
    Line = list(f.readline())
    for znak in range(len(Line) -1):
        Alphabet.append(Line[znak])
    print(Alphabet)

    Mailinput = f.readline()[:-1]
    print(Mailinput)

    Marker = f.readline()[:-1]
    print(Marker)

    Start_state = f.readline()[:-1]
    print(Start_state)

    #CZYTANIE WSZYTSKIEGO
    while True:
        Line = f.readline()
        if not Line:
            break
        else:
            if Line[0:6] == "koniec":
                end_index, number_of_end_states = Line[:-1].split(" : ")
                for i in range(int(number_of_end_states)):
                    Line = f.readline()[:-1]
                    End_state_name, move, result = Line.split(" : ")
                    End_states[End_state_name] = [move, result]
                    #print(End_state_name, move, result)
                Line = f.readline()[:-1]
            if Line[0:4] == "graf":
                graph_index, number_of_graph_states = Line[:-1].split(" : ")
                for i in range(int(number_of_graph_states) - int(number_of_end_states)):
                    Line = f.readline()[:-2]
                    Graph_state_name = Line
                    Graph_states[Graph_state_name] = list()
                    for i in range(len(Alphabet)):
                        Line = f.readline()[:-1]
                        letter, action, write_letter, move, next_state = Line.split(" : ")
                        Graph_states[Graph_state_name].append({letter : [action, write_letter, move, next_state]})
                    Line = f.readline()
        #a = 0

    print(End_states)
    print(Graph_states)

    f.close()'''