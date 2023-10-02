from search_problem import maze_problem as m, search_strategy as s
from graphical_mode import plotting, performance
from config import configuration as c


def generate_maze_instances(num_instances):
    """Generate a list of random maze instances of length num_instances."""
    problem_instances = []
    for _ in range(num_instances):
        problem = m.Maze()  # Create a new maze instance
        problem_instances.append(problem)
    return problem_instances

def main():
    """Main function."""

    # After maze instances generation, run algorithms and measure their performance
    problem = generate_maze_instances(int(c.N_MAZE_INSTANCES))
    global_performance_data = {}
    for i in range(len(problem)):
        strategies = {
            "GREEDY": s.GREEDY_Strategy(),
            "A_Star": s.ASTAR_Strategy(),
            "BFS": s.BFS_Strategy(),
            "DFS": s.DFS_Strategy(),
            "UCS": s.UCS_Strategy()
        }

        performance_data = {}  # Store performance data for each algorithm

        # Iterate through each algorithm and calculate performance
        for algorithm, strategy in strategies.items():  # Use items() for both key and value
            p = performance.Performance(algorithm, problem[i])
            for node in problem[i].goal_nodes_list:
                partial_path, partial_expanded_nodes = problem[i].process_input(strategy, node)
                p.calculate_performance(partial_path, partial_expanded_nodes)

            p.show_performance(algorithm)
            strategies[algorithm] = [p.c_path, p.expanded_nodes]

            # Store performance data for plotting
            performance_data[algorithm] = {
                'c_path': p.c_path,
                'expanded_nodes': p.expanded_nodes
            }

        plotting.Plot.plot_single_algorithm(plotting.Plot, performance_data, problem[i])

        best_algorithm = min(strategies, key=lambda x: strategies[x][0])
        worst_algorithm = max(strategies, key=lambda x: strategies[x][0])

        for key, value in performance_data.items():
            print('\033[34m', key, value)

        print('\u001b[92m', 'Best performing algorithm:', best_algorithm)
        print('\033[91m', 'Worst performing algorithm:', '\033[0m', worst_algorithm)
        print("\n")
        global_performance_data[problem[i]] = {"Performance Data": performance_data,"best_algorithm":best_algorithm,"worst_algorithm":worst_algorithm}

    for key, value in global_performance_data.items():
        print(f'\033[34m {key.__class__.__name__}: {hex(id(key))}  {value} \033[0m')

    plotting.Plot.plot_average(plotting.Plot, global_performance_data)

# Start
if __name__ == "__main__":
    main()
