# Import necessary modules
import matplotlib.pyplot as plt, numpy as np
from config import configuration as c

# Chart printing Class
class Plot:
    def plot_single_algorithm(self, dt, problem):
        """
        This method plots the performance of each single algorithm, in terms of path cost and number of expanded nodes.

        Parameters:
        - dt (dict): A dictionary containing algorithm performance data.
        - problem (object): The problem instance.

        """
        # Plotting path cost performance data
        plt.figure()
        plt.bar(dt.keys(), [data['c_path'] for data in dt.values()])
        plt.xlabel('Algorithm')
        plt.ylabel('Cost of the Path')
        plt.title('Cost of the Path Performance of Algorithms')
        plt.savefig('./'+c.DEFAULT_IMAGES_FOLDER+'/Path_Cost'+ str(hex(id(problem))) +".jpg", format='jpg')
        plt.show(block=False)
        plt.pause(1)
        plt.close()

        # Plotting the expanded nodes performance data
        plt.figure()
        plt.bar(dt.keys(), [data['expanded_nodes'] for data in dt.values()])
        plt.xlabel('Algorithm')
        plt.ylabel('Expanded Nodes')
        plt.title('Expanded Nodes in Algorithms')
        plt.savefig('./'+c.DEFAULT_IMAGES_FOLDER+'/Expanded_nodes'+ str(hex(id(problem))) +".jpg", format='jpg')
        plt.show(block=False)
        plt.pause(1)
        plt.close()


    def plot_average (self, dt):
        """
        This method calculates and plots the average performance of algorithms in terms of average path cost and the
        average number of expanded nodes.
        It additionally creates pie charts to show the percentage of the best and worst overall average algorithms.

        Parameters:
        - dt (dict): A dictionary containing algorithm performance data.

        """

        # Calculate average c_path and expanded_nodes for each algorithm
        algorithm_avg_c_path = {}
        algorithm_avg_expanded_nodes = {}

        for data_key, data in dt.items():
            performance_data = data['Performance Data']
            for algorithm, metrics in performance_data.items():
                if algorithm not in algorithm_avg_c_path:
                    algorithm_avg_c_path[algorithm] = []
                    algorithm_avg_expanded_nodes[algorithm] = []

                algorithm_avg_c_path[algorithm].append(metrics['c_path'])
                algorithm_avg_expanded_nodes[algorithm].append(metrics['expanded_nodes'])

        # Calculate the averages
        for algorithm in algorithm_avg_c_path:
            algorithm_avg_c_path[algorithm] = np.mean(algorithm_avg_c_path[algorithm])
            algorithm_avg_expanded_nodes[algorithm] = np.mean(algorithm_avg_expanded_nodes[algorithm])

        # Create bar plots for the visualization of the algorithms' average path cost
        plt.figure()
        plt.bar(algorithm_avg_c_path.keys(), algorithm_avg_c_path.values())
        plt.xlabel('Algorithm')
        plt.ylabel('Average Cost of the Path')
        plt.title('Average Cost of the Path Performance of Algorithms')
        plt.savefig('./'+c.DEFAULT_IMAGES_FOLDER+'/Average_Cost.jpg', format='jpg')
        plt.show(block=False)
        plt.pause(1)
        plt.close()

        # Create bar plots for the visualization of the algorithms' average number of expanded nodes
        plt.figure()
        plt.bar(algorithm_avg_expanded_nodes.keys(), algorithm_avg_expanded_nodes.values())
        plt.xlabel('Algorithm')
        plt.ylabel('Average Expanded Nodes')
        plt.title('Average Expanded Nodes in Algorithms')
        plt.savefig('./'+c.DEFAULT_IMAGES_FOLDER+'/Average_Expanded_Nodes.jpg', format='jpg')
        plt.show(block=False)
        plt.pause(1)
        plt.close()

        # Find the best and worst average algorithms based on path cost
        best_avg_algorithm_c_path = min(algorithm_avg_c_path, key=lambda x: algorithm_avg_c_path[x])
        worst_avg_algorithm_c_path = max(algorithm_avg_c_path, key=lambda x: algorithm_avg_c_path[x])

        # Calculate the percentage for the best average algorithm evaluated on path cost
        best_avg_percentage_c_path = (algorithm_avg_c_path[best_avg_algorithm_c_path] / sum(
            algorithm_avg_c_path.values())) * 100

        # Create a pie chart for the visualization of the best average algorithm evaluated on path cost
        plt.figure()
        plt.pie([100 - best_avg_percentage_c_path, best_avg_percentage_c_path],
                labels=[best_avg_algorithm_c_path, 'Others'], autopct='%1.1f%%')
        plt.title('Percentage of Best Average Cost Path Algorithm')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.savefig('./'+c.DEFAULT_IMAGES_FOLDER+'/Percentage_Best_Average_Algorithm.jpg', format='jpg')
        plt.show(block=False)
        plt.pause(1)
        plt.close()

        # Calculate the percentage for the worst average algorithm evaluated on path cost
        worst_avg_c_path_percentage = (algorithm_avg_c_path[worst_avg_algorithm_c_path] / sum(
            algorithm_avg_c_path.values())) * 100

        # Create a pie chart for the visualization of the worst average algorithm evaluated on path cost
        plt.figure()
        plt.pie([100 - worst_avg_c_path_percentage, worst_avg_c_path_percentage],
                labels=[worst_avg_algorithm_c_path, 'Others'], autopct='%1.1f%%')
        plt.title('Percentage of Worst Average Algorithm')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.savefig('./'+c.DEFAULT_IMAGES_FOLDER+'/Percentage_Worst_Average_Algorithm.jpg', format='jpg')
        plt.show(block=False)
        plt.pause(1)
        plt.close()

        # Find the best and worst average algorithms based on the number of expanded nodes
        best_avg_algorithm_expanded_nodes = min(algorithm_avg_expanded_nodes,
                                                key=lambda x: algorithm_avg_expanded_nodes[x])
        worst_avg_algorithm_expanded_nodes = max(algorithm_avg_expanded_nodes,
                                                 key=lambda x: algorithm_avg_expanded_nodes[x])

        # Print the best and worst average algorithms with their associated performance average values
        print("Best Average Cost of the Path Algorithm:", best_avg_algorithm_c_path)
        print("Average Cost of the Path for Best Algorithm:", algorithm_avg_c_path[best_avg_algorithm_c_path])
        print("Best Average Expanded Nodes Algorithm:", best_avg_algorithm_expanded_nodes)
        print("Average Expanded Nodes for Best Algorithm:",
              algorithm_avg_expanded_nodes[best_avg_algorithm_expanded_nodes])

        print("\nWorst Average Cost of the Path Algorithm:", worst_avg_algorithm_c_path)
        print("Average Cost of the Path for Worst Algorithm:", algorithm_avg_c_path[worst_avg_algorithm_c_path])
        print("Worst Average Expanded Nodes Algorithm:", worst_avg_algorithm_expanded_nodes)
        print("Average Expanded Nodes for Worst Algorithm:",
              algorithm_avg_expanded_nodes[worst_avg_algorithm_expanded_nodes])

        # Calculate the percentage for the best average algorithm evaluated on the number of expanded nodes
        best_avg_percentage_expanded_nodes = (algorithm_avg_expanded_nodes[best_avg_algorithm_expanded_nodes] / sum(
            algorithm_avg_expanded_nodes.values())) * 100


        # Create a pie chart for the visualization of the best average algorithm evaluated on the number of expanded
        # nodes
        plt.figure()
        plt.pie([100 - best_avg_percentage_expanded_nodes, best_avg_percentage_expanded_nodes],
                labels=[best_avg_algorithm_expanded_nodes, 'Others'],
                autopct='%1.1f%%')
        plt.title('Percentage of Best Average Expanded Nodes Algorithm')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.savefig('./'+c.DEFAULT_IMAGES_FOLDER+'/Percentage_Best_Average_Expanded_Nodes_Algorithm.jpg', format='jpg')
        plt.show(block=False)
        plt.pause(1)
        plt.close()

        # Calculate the percentage for the worst average algorithm evaluated on the number of expanded nodes
        worst_avg_expanded_nodes_percentage = (algorithm_avg_expanded_nodes[worst_avg_algorithm_expanded_nodes] / sum(
            algorithm_avg_expanded_nodes.values())) * 100

        # Create a pie chart for the visualization of the worst average algorithm evaluated on the number of expanded
        # nodes
        plt.figure()
        plt.pie([100 - worst_avg_expanded_nodes_percentage, worst_avg_expanded_nodes_percentage],
                labels=[worst_avg_algorithm_expanded_nodes, 'Others'],
                autopct='%1.1f%%')
        plt.title('Percentage of Worst  Average  Expanded Nodes Algorithm')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.savefig('./'+c.DEFAULT_IMAGES_FOLDER+'/Percentage_Worst_Average_Expanded_Nodes_Algorithm.jpg', format='jpg')
        plt.show(block=False)
        plt.pause(1)
        plt.close()
