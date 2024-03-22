import mesa
from .agent import TreeCell
from PIL import Image

original_image = Image.open("C:/Users/maxwe/Documents/Grad/Classes/Fall 2022/SimTech/assignment3-abm-mstolarenko/"
                            "images/st.louis.png")
myImage = original_image.convert('RGB')

class ForestFire(mesa.Model):
    """
    Simple Forest Fire model.
    """

    def __init__(self, width=100, height=100, density=0.65):
        """
        Create a new forest fire model.

        Args:
            width, height: The size of the grid to model
            density: What fraction of grid cells have a tree in them.
        """
        # Set up model objects
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.Grid(width, height, torus=False)

        self.datacollector = mesa.DataCollector(
            {
                "Fine": lambda m: self.count_type(m, "Fine"),
                "On Fire": lambda m: self.count_type(m, "On Fire"),
                "Burned Out": lambda m: self.count_type(m, "Burned Out"),
            }
        )

        # Place a tree in each cell with Prob = density
        for (contents, x, y) in self.grid.coord_iter():
            r, g, b = myImage.getpixel((x, y))
            if (g > 50) and (b < 48):
                new_tree = TreeCell((x, y), self)
            # if self.random.random() < density:
                # Create a tree
            #    new_tree = TreeCell((x, y), self)
                # Set all trees in the first column on fire.
                if (x, y) == (80, 10):
                    new_tree.condition = "On Fire"
                self.grid.place_agent(new_tree, (x, y))
                self.schedule.add(new_tree)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        """
        Advance the model by one step.
        """
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

        # Halt if no more fire
        if self.count_type(self, "On Fire") == 0:
            self.running = False

    @staticmethod
    def count_type(model, tree_condition):
        """
        Helper method to count trees in a given condition in a given model.
        """
        count = 0
        for tree in model.schedule.agents:
            if tree.condition == tree_condition:
                count += 1
        return count
