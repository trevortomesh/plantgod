from God import God
from Artist import PixelArtist

# Epics
# @TODO: find a way to prevent reaching sub-optimal peaks

# Tasks
# @TODO: try cubing nutriets
# @TODO: what if all the parents died each generatation
# @TODO: Try asexual mutation where only one parent from a population produced
#   offspring per tick, and then most fit from set pop size selected
# @TODO: switch mutations to being only by a max increase or decrease of val 1
# @TODO: roots should be most optimanl if they have exactly 2 siblings
# @TODO: give points for closely valued siblings (right now its exact)
# @TODO: adjust criteria to prevent checkerboards

# Default settings
generations = 100
initialPopSize = 50
survivalSize = 8
plantWidth = 16
plantHeight = 32
rootStart = 0.8

# Create the almighty creator
print "Initializing God."
god = God(
            firstGenerationSize=initialPopSize,
            lifeFormWidth = plantWidth,
            lifeFormHeight = plantHeight,
            rootStartPercent = rootStart
         )

# Initializes PixelArtist
pixelArtist = PixelArtist()

# generate initial population
initialPop = god.createLife()
print "Initial pop created!"

parents = god.pickMostFit(initialPop, survivalSize)
parentGen = parents
print "Starting generation selected."

print "TODO: Save image starting generation"
# Generations should be drawn together as a single image
# With the point value of the plant underneath it

for i in range(0, generations):
    print "----------------------------------"
    print "Starting generation: ", i
    offspring = god.breed(parents)
    offspring = god.mutate(offspring)
    offspring = god.trimDeadCells(offspring)
    allLife = offspring + god.trimDeadCells(parents)
    parents = god.pickMostFit(allLife, survivalSize)
    print "TODO: Save image for survivors"
    if i % 10 == 0 or i == generations - 1:
        pixelArtist.drawPlantGeneration(lifeforms=parents, filename='untouched_parents_squared_success_gen_{0}'.format(i), columns=plantWidth)

print "Initial Scores:"
for p in parentGen:
    print god.judgeLifeform(p)

print "Final Scores:"
finalForms = parents
for p in finalForms:
    print god.judgeLifeform(p)
