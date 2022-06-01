from pyamaze import maze,agent
# pip install pyamaze

m=maze(20,20)

m.CreateMaze(loopPercent=50)        #max broj putanja 50,from source to destination

a=agent(m,filled=True,footprints=True)

m.tracePath({a:m.path})

m.run()