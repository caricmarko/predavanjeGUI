from pyamaze import maze,agent
# pip install pyamaze

m=maze(20,20)

m.CreateMaze(loopPercent=50)

a=agent(m,filled=True,footprints=True)

m.tracePath({a:m.path})

m.run()