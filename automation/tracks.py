
# exec(open("/home/jacob/pontech/kicad/KiCadLibrary/automation/tracks.py").read())

from pcbnew import *
# import numpy

# from wxPython import *

class SimplePlugin(ActionPlugin):
    def defaults(self):
        self.name = "Track Lengths"
        self.category = "A non descriptive category name"
        self.description = "Get the lengths of tracks in track list"
        self.show_toolbar_button = True  # Optional, defaults to False

    def Run(self):
        print("Running Track Lengths")

        # set_of_nets_of_interest = [
        #     {"id": "R0", "nets": ["/Microcontroller/R0", "/LCD/LCD.R0"], "length": 0},
        #     {"id": "R1", "nets": ["/Microcontroller/R1", "/LCD/LCD.R1"], "length": 0},
        #     {"id": "R2", "nets": ["/Microcontroller/R2", "/LCD/LCD.R2"], "length": 0},
        #     {"id": "R3", "nets": ["/Microcontroller/R3", "/LCD/LCD.R3"], "length": 0},
        #     {"id": "R4", "nets": ["/Microcontroller/R4", "/LCD/LCD.R4"], "length": 0},
        #     {"id": "R5", "nets": ["/Microcontroller/R5", "/LCD/LCD.R5"], "length": 0},
        #     {"id": "R6", "nets": ["/Microcontroller/R6", "/LCD/LCD.R6"], "length": 0},
        #     {"id": "R7", "nets": ["/Microcontroller/R7", "/LCD/LCD.R7"], "length": 0},
        #     {"id": "G0", "nets": ["/Microcontroller/G0", "/LCD/LCD.G0"], "length": 0},
        #     {"id": "G1", "nets": ["/Microcontroller/G1", "/LCD/LCD.G1"], "length": 0},
        #     {"id": "G2", "nets": ["/Microcontroller/G2", "/LCD/LCD.G2"], "length": 0},
        #     {"id": "G3", "nets": ["/Microcontroller/G3", "/LCD/LCD.G3"], "length": 0},
        #     {"id": "G4", "nets": ["/Microcontroller/G4", "/LCD/LCD.G4"], "length": 0},
        #     {"id": "G5", "nets": ["/Microcontroller/G5", "/LCD/LCD.G5"], "length": 0},
        #     {"id": "G6", "nets": ["/Microcontroller/G6", "/LCD/LCD.G6"], "length": 0},
        #     {"id": "G7", "nets": ["/Microcontroller/G7", "/LCD/LCD.G7"], "length": 0},
        #     {"id": "B0", "nets": ["/Microcontroller/B0", "/LCD/LCD.B0"], "length": 0},
        #     {"id": "B1", "nets": ["/Microcontroller/B1", "/LCD/LCD.B1"], "length": 0},
        #     {"id": "B2", "nets": ["/Microcontroller/B2", "/LCD/LCD.B2"], "length": 0},
        #     {"id": "B3", "nets": ["/Microcontroller/B3", "/LCD/LCD.B3"], "length": 0},
        #     {"id": "B4", "nets": ["/Microcontroller/B4", "/LCD/LCD.B4"], "length": 0},
        #     {"id": "B5", "nets": ["/Microcontroller/B5", "/LCD/LCD.B5"], "length": 0},
        #     {"id": "B6", "nets": ["/Microcontroller/B6", "/LCD/LCD.B6"], "length": 0},
        #     {"id": "B7", "nets": ["/Microcontroller/B7", "/LCD/LCD.B7"], "length": 0},
        #     {"id": "HSYNC", "nets": ["/Microcontroller/HSYNC", "/LCD/LCD.HSYNC"], "length": 0},
        #     {"id": "VSYNC", "nets": ["/Microcontroller/VSYNC", "/LCD/LCD.VSYNC"], "length": 0},
        #     {"id": "CLK", "nets": ["/Microcontroller/CLK", "/LCD/LCD.CLK"], "length": 0},
        # ]

        # set_of_nets_of_interest = [
        #     {"id": "SPI-P1.IO0", "nets": ["/Memory/OCTO-SPI-P1.IO0"], "length": 0},
        #     {"id": "SPI-P1.IO1", "nets": ["/Memory/OCTO-SPI-P1.IO1"], "length": 0},
        #     {"id": "SPI-P1.IO2", "nets": ["/Memory/OCTO-SPI-P1.IO2"], "length": 0},
        #     {"id": "SPI-P1.IO3", "nets": ["/Memory/OCTO-SPI-P1.IO3"], "length": 0},
        #     {"id": "SPI-P1.IO4", "nets": ["/Memory/OCTO-SPI-P1.IO4"], "length": 0},
        #     {"id": "SPI-P1.IO5", "nets": ["/Memory/OCTO-SPI-P1.IO5"], "length": 0},
        #     {"id": "SPI-P1.IO6", "nets": ["/Memory/OCTO-SPI-P1.IO6"], "length": 0},
        #     {"id": "SPI-P1.IO7", "nets": ["/Memory/OCTO-SPI-P1.IO7"], "length": 0},
        #
        #     {"id": "SPI-P1.~{CS}", "nets": ["/Memory/OCTO-SPI-P1.~{CS}"], "length": 0},
        #     {"id": "SPI-P1.CLK", "nets": ["/Memory/OCTO-SPI-P1.CLK"], "length": 0},
        #     {"id": "SPI-P1.NCLK", "nets": ["/Memory/OCTO-SPI-P1.NCLK"], "length": 0},
        #     {"id": "SPI-P1.DQS", "nets": ["/Memory/OCTO-SPI-P1.DQS"], "length": 0},
        #
        # ]

        set_of_nets_of_interest = [
            {"id": "SPI-P2.IO0", "nets": ["/Memory/OCTO-SPI-P2.IO0"], "length": 0},
            {"id": "SPI-P2.IO1", "nets": ["/Memory/OCTO-SPI-P2.IO1"], "length": 0},
            {"id": "SPI-P2.IO2", "nets": ["/Memory/OCTO-SPI-P2.IO2"], "length": 0},
            {"id": "SPI-P2.IO3", "nets": ["/Memory/OCTO-SPI-P2.IO3"], "length": 0},

            {"id": "SPI-P2.~{CS}", "nets": ["/Memory/OCTO-SPI-P2.~{CS}"], "length": 0},
            {"id": "SPI-P2.CLK", "nets": ["/Memory/OCTO-SPI-P2.CLK"], "length": 0},

        ]


        board = GetBoard()
        for track in board.GetTracks():
            netname = track.GetNetname()
            found = False
            for net_set in set_of_nets_of_interest:
                if netname in net_set["nets"]:
                    net_set["length"] += ToMM(track.GetLength())
                    found = True
            if found:
                print("*** ", end="")
            print(netname + " " + str(ToMM(track.GetLength())))

        print("Results....")
        longest = 0
        longest_name = "unknown"
        shortest = 10000000
        shortest_name = "unknown"
        mean = 0
        count = 0
        for net_set in set_of_nets_of_interest:
            length = net_set["length"]
            count = count + 1
            mean = mean + length

            print(net_set["id"] + " = " + str(length))
            if length > longest:
                longest = length
                longest_name = net_set["id"]
            if length < shortest:
                shortest = length
                shortest_name = net_set["id"]

        print("shortest = " + str(shortest) + " (" + shortest_name + ")")
        print("longest = " + str(longest) + " (" + longest_name + ")")
        print("delta = " + str(longest - shortest))
        print("count = " + str(count))
        print("mean = " + str(mean/count))


    # In Python we don't have to worry about the stack vs. the heap, however
    # that means that dialogs do need to be destroyed. The typical pattern for
    # dialog usage looks something like this:
    # def AskUser(self):
    #     try:
    #         dlg = MyAskDialog(self)
    #         if dlg.ShowModal() == wx.ID_OK:
    #             # do something here
    #             print('Hello')
    #         else:
    #             # handle dialog being cancelled or ended by some other button
    #             ...
    #     finally:
    #         # explicitly cause the dialog to destroy itself
    #         dlg.Destroy()

SimplePlugin().register()


  
